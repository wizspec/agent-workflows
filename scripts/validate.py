#!/usr/bin/env python3
"""Validate the repository's portable Agent Skills packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
ALLOWED_FIELDS = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
PRIVATE_PATHS = (
    re.compile(r"/Users/[^/\s]+/"),
    re.compile(r"/home/[^/\s]+/"),
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
)


def parse_frontmatter(text: str, path: Path) -> tuple[dict[str, str], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path}: missing or malformed YAML frontmatter")

    fields: dict[str, str] = {}
    lines = match.group(1).splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        index += 1
        if not line.strip() or line.lstrip().startswith("#") or line.startswith((" ", "\t")):
            continue
        key, separator, raw_value = line.partition(":")
        if not separator:
            raise ValueError(f"{path}: malformed frontmatter line: {line!r}")
        key = key.strip()
        if key in fields:
            raise ValueError(f"{path}: duplicate frontmatter field {key!r}")

        value = raw_value.strip()
        if value in {"|", "|-", ">", ">-"}:
            chunks: list[str] = []
            while index < len(lines) and (not lines[index] or lines[index].startswith((" ", "\t"))):
                chunks.append(lines[index].strip())
                index += 1
            value = " ".join(chunk for chunk in chunks if chunk)
        elif len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        fields[key] = value

    return fields, text[match.end() :]


def validate_local_links(boundary: Path, markdown_path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for raw_target in LINK_RE.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        clean_target = target.split("#", 1)[0]
        resolved = (markdown_path.parent / clean_target).resolve()
        try:
            resolved.relative_to(boundary.resolve())
        except ValueError:
            errors.append(f"{markdown_path}: link escapes the skill directory: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{markdown_path}: missing linked file: {target}")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir}: missing SKILL.md"]

    nested = [path for path in skill_dir.rglob("SKILL.md") if path != skill_file]
    if nested:
        errors.extend(f"{path}: nested skills are not allowed" for path in nested)

    text = skill_file.read_text(encoding="utf-8")
    try:
        fields, body = parse_frontmatter(text, skill_file)
    except ValueError as error:
        return [str(error)]

    unexpected = sorted(set(fields) - ALLOWED_FIELDS)
    if unexpected:
        errors.append(f"{skill_file}: unsupported frontmatter fields: {', '.join(unexpected)}")

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append(f"{skill_file}: invalid skill name {name!r}")
    if name != skill_dir.name:
        errors.append(f"{skill_file}: name {name!r} must match directory {skill_dir.name!r}")
    if not description or len(description) > 1024:
        errors.append(f"{skill_file}: description must contain 1-1024 characters")
    if "what this skill does" in description.lower() or "[todo:" in text.lower():
        errors.append(f"{skill_file}: unfinished scaffold placeholder")
    if len(body.splitlines()) > 500:
        errors.append(f"{skill_file}: body exceeds the recommended 500-line limit")

    for markdown_path in skill_dir.rglob("*.md"):
        markdown = markdown_path.read_text(encoding="utf-8")
        errors.extend(validate_local_links(skill_dir, markdown_path, markdown))

    for text_path in skill_dir.rglob("*"):
        if not text_path.is_file() or text_path.suffix not in {".md", ".yaml", ".yml", ".txt"}:
            continue
        content = text_path.read_text(encoding="utf-8")
        for pattern in PRIVATE_PATHS:
            if pattern.search(content):
                errors.append(f"{text_path}: contains a private absolute path")
                break

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("error: skills/ directory is missing", file=sys.stderr)
        return 1

    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    if not skill_dirs:
        print("error: no skills found", file=sys.stderr)
        return 1

    stray_files = sorted(path for path in SKILLS_DIR.iterdir() if path.is_file())
    errors = [f"{path}: skills/ must contain only skill directories" for path in stray_files]
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    readme = ROOT / "README.md"
    if not readme.is_file():
        errors.append(f"{readme}: missing repository catalog")
    else:
        readme_text = readme.read_text(encoding="utf-8")
        errors.extend(validate_local_links(ROOT, readme, readme_text))
        for skill_dir in skill_dirs:
            if f"skills/{skill_dir.name}/" not in readme_text:
                errors.append(f"{readme}: missing catalog entry for {skill_dir.name}")

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(skill_dirs)} skill(s): {', '.join(path.name for path in skill_dirs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
