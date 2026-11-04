"""Builds one ZIP per skill folder for uploading to Claude.ai (Customize > Skills > Upload a skill), plus one ZIP
with every skill for Claude Code and other assistants. Runs in CI on every push to main; locally:
python .github/scripts/build_skill_zips.py dist

<folder>.zip holds <folder>/SKILL.md (the skill folder at the root, as Claude.ai asks), any other files the skill
ships except README.md (its links point back into the repository), and LICENSE with the CC BY 4.0 text the
credit line refers to. In the zipped SKILL.md, the top-level `version` and `tags` keys move under `metadata` as
strings, which is where the Agent Skills spec puts extra fields; the repository files stay as they are.

linkedin-ads-skills-all.zip holds every skill folder the same way. Claude.ai takes one skill per upload, so that
file is for unzipping into ~/.claude/skills or another assistant's skills folder."""
import pathlib
import re
import sys
import zipfile

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "dist").resolve()
STAMP = (2026, 1, 1, 0, 0, 0)  # fixed time inside the archives, so an unchanged skill gives an identical file
LICENSE = (ROOT / "LICENSE").read_text(encoding="utf-8")


def spec_frontmatter(text: str) -> str:
    text = text.replace("\r\n", "\n")
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        raise SystemExit("no frontmatter")
    lines, extra, out = m.group(1).split("\n"), {}, []
    for line in lines:
        k = re.match(r"(version|tags):\s*(.*)$", line)
        if k:
            extra[k.group(1)] = k.group(2).strip().strip("[]").strip("\"'")
        else:
            out.append(line)
    if extra:
        added = [f'  {k}: "{", ".join(x.strip() for x in v.split(","))}"' for k, v in extra.items()]
        if "metadata:" in out:
            i = out.index("metadata:") + 1
            while i < len(out) and out[i].startswith((" ", "\t")):
                i += 1
            out[i:i] = added
        else:
            out += ["metadata:"] + added
    return "---\n" + "\n".join(out) + "\n---\n" + text[m.end():]


def add(z: zipfile.ZipFile, arcname: str, data: bytes) -> None:
    info = zipfile.ZipInfo(arcname, STAMP)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    z.writestr(info, data)


def write_skill(z: zipfile.ZipFile, folder: pathlib.Path) -> None:
    for p in sorted(folder.rglob("*")):
        if p.is_dir() or p.name == "README.md":
            continue
        rel = p.relative_to(ROOT).as_posix()
        data = spec_frontmatter(p.read_text(encoding="utf-8")).encode("utf-8") if p.name == "SKILL.md" else p.read_bytes()
        add(z, rel, data)
    add(z, f"{folder.name}/LICENSE", LICENSE.encode("utf-8"))


OUT.mkdir(parents=True, exist_ok=True)
folders = sorted(p.parent for p in ROOT.glob("*/SKILL.md"))
for f in folders:
    with zipfile.ZipFile(OUT / f"{f.name}.zip", "w") as z:
        write_skill(z, f)
with zipfile.ZipFile(OUT / "linkedin-ads-skills-all.zip", "w") as z:
    for f in folders:
        write_skill(z, f)
print(f"{len(folders)} skill zips and linkedin-ads-skills-all.zip in {OUT}")
