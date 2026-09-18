#!/usr/bin/env python3
"""Copy skills from this repository into one or more agent skill directories."""

from __future__ import annotations

import argparse
import filecmp
import os
import shutil
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
AGENT_TARGETS = {
    "codex": Path.home() / ".agents" / "skills",
    "claude": Path.home() / ".claude" / "skills",
}


def available_skills() -> dict[str, Path]:
    return {
        path.name: path
        for path in sorted(SKILLS_DIR.iterdir())
        if path.is_dir() and (path / "SKILL.md").is_file()
    }


def trees_match(left: Path, right: Path) -> bool:
    comparison = filecmp.dircmp(left, right)
    if comparison.left_only or comparison.right_only or comparison.funny_files:
        return False
    if any(not filecmp.cmp(left / name, right / name, shallow=False) for name in comparison.common_files):
        return False
    return all(trees_match(left / name, right / name) for name in comparison.common_dirs)


def install_skill(source: Path, target_root: Path, force: bool) -> str:
    target_root.mkdir(parents=True, exist_ok=True)
    destination = target_root / source.name

    if destination.is_dir() and not destination.is_symlink() and trees_match(source, destination):
        return f"unchanged {source.name} -> {target_root}"
    if destination.exists() and not force:
        raise FileExistsError(
            f"{destination} already exists and differs; rerun with --force to replace it"
        )

    temporary_root = Path(tempfile.mkdtemp(prefix=".agent-skill-install-", dir=target_root))
    staged = temporary_root / source.name
    backup = temporary_root / ".previous"
    try:
        shutil.copytree(source, staged)
        if destination.exists():
            os.replace(destination, backup)
        try:
            os.replace(staged, destination)
        except Exception:
            if backup.exists() and not destination.exists():
                os.replace(backup, destination)
            raise
        if backup.exists():
            shutil.rmtree(backup)
    finally:
        shutil.rmtree(temporary_root, ignore_errors=True)

    return f"installed {source.name} -> {destination}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--skill", action="append", help="skill name; repeat to select several")
    selection.add_argument("--all", action="store_true", help="install every skill")
    parser.add_argument("--list", action="store_true", help="list available skills and exit")
    parser.add_argument(
        "--agent",
        choices=("codex", "claude", "both"),
        help="install to a standard user-level agent directory",
    )
    parser.add_argument(
        "--target",
        action="append",
        type=Path,
        help="install to this skills directory; repeat for multiple targets",
    )
    parser.add_argument("--force", action="store_true", help="replace a differing existing skill")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skills = available_skills()

    if args.list:
        for name in skills:
            print(name)
        return 0

    if not args.all and not args.skill:
        print("error: choose --skill NAME or --all", file=sys.stderr)
        return 2

    selected_names = list(skills) if args.all else list(dict.fromkeys(args.skill))
    unknown = [name for name in selected_names if name not in skills]
    if unknown:
        print(f"error: unknown skill(s): {', '.join(unknown)}", file=sys.stderr)
        return 2

    targets = [path.expanduser().resolve() for path in (args.target or [])]
    if args.agent in {"codex", "both"}:
        targets.append(AGENT_TARGETS["codex"])
    if args.agent in {"claude", "both"}:
        targets.append(AGENT_TARGETS["claude"])
    targets = list(dict.fromkeys(targets))
    if not targets:
        print("error: choose --agent or provide at least one --target", file=sys.stderr)
        return 2

    try:
        for target in targets:
            for name in selected_names:
                print(install_skill(skills[name], target, args.force))
    except (FileExistsError, OSError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
