import os
import re
import pandas as pd
from slugify import slugify

INPUT_FILE = "cpp-docs.xlsx"
OUTPUT_DIR = "../docs"

# =========================
# TEXT HELPERS
# =========================

def clean_text(value) -> str:
    if pd.isna(value):
        return ""

    text = str(value)

    # normalize newline
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    return text.strip()


def capitalize_first(text: str) -> str:
    """
    Viết hoa chữ cái đầu tiên.
    """
    if not text:
        return ""

    return text[0].upper() + text[1:]


def capitalize_bullet_items(text: str) -> str:
    """
    Viết hoa chữ cái đầu của:
    - bullet list
    - numbered list
    """

    lines = text.split("\n")
    result = []

    for line in lines:
        stripped = line.strip()

        # bullet list
        bullet_match = re.match(r"^([-*])\s+(.*)", stripped)

        # numbered list
        numbered_match = re.match(r"^(\d+\.)\s+(.*)", stripped)

        if bullet_match:
            prefix = bullet_match.group(1)
            content = capitalize_first(bullet_match.group(2))

            result.append(f"{prefix} {content}")

        elif numbered_match:
            prefix = numbered_match.group(1)
            content = capitalize_first(numbered_match.group(2))

            result.append(f"{prefix} {content}")

        else:
            result.append(line)

    return "\n".join(result)


# =========================
# MDX SANITIZE
# =========================

def escape_html(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def escape_mdx(text: str) -> str:
    """
    Escape các ký tự gây lỗi MDX
    """
    if not text:
        return ""

    text = escape_html(text)

    text = (
        text.replace("{", "&#123;")
        .replace("}", "&#125;")
    )

    return text


# =========================
# CONTENT FORMAT
# =========================

CPP_KEYWORDS = [
    "std::",
    "#include",
    "int main",
    "cout",
    "cin",
    "mutex",
    "template",
    "::",
    "->",
]


def is_code_block(text: str) -> bool:
    return any(keyword in text for keyword in CPP_KEYWORDS)


def wrap_code_block(text: str) -> str:
    if is_code_block(text):
        return f"```cpp\n{text}\n```"

    return text


def format_headings(text: str) -> str:
    """
    Convert:
    Ưu điểm
    Nhược điểm
    => markdown heading
    """

    replacements = {
        "Ưu điểm": "### ✅ Ưu điểm",
        "Nhược điểm": "### ❌ Nhược điểm",
        "Ví dụ": "### 📌 Ví dụ",
        "Lưu ý": "### ⚠️ Lưu ý",
    }

    for old, new in replacements.items():
        text = re.sub(rf"^{old}$", new, text, flags=re.MULTILINE)

    return text


def normalize_bullets(text: str) -> str:
    """
    Convert bullet unicode sang markdown
    """

    bullet_chars = ["•", "●", "▪", "◦"]

    for bullet in bullet_chars:
        text = text.replace(bullet, "-")

    return text


def format_content(text: str) -> str:
    if not text:
        return ""

    text = normalize_bullets(text)

    text = capitalize_bullet_items(text)

    text = format_headings(text)

    text = escape_mdx(text)

    text = wrap_code_block(text)

    # remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


# =========================
# MARKDOWN GENERATION
# =========================

def generate_markdown(no, title, content, note):
    title = capitalize_first(title)

    content = format_content(content)

    note = format_content(note)

    return f"""---
title: "{title}"
---

# {no}. {title}

## 🧾 Content

{content}

## 📝 Note

{note}
"""


# =========================
# FILE GENERATION
# =========================

def generate_file(folder_path, no, title, markdown_content):
    filename = f"{no}-{slugify(title)}.md"

    filepath = os.path.join(folder_path, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"✔ Generated: {filepath}")


def process_sheet(xls, sheet_name):
    df = xls.parse(sheet_name)

    folder_name = slugify(sheet_name)

    folder_path = os.path.join(OUTPUT_DIR, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    for _, row in df.iterrows():
        no = clean_text(row.get("No."))
        title = clean_text(row.get("Title"))
        content = clean_text(row.get("Content"))
        note = clean_text(row.get("Note"))

        if not no or not title:
            continue

        markdown_content = generate_markdown(
            no,
            title,
            content,
            note,
        )

        generate_file(
            folder_path,
            no,
            title,
            markdown_content,
        )


# =========================
# MAIN
# =========================

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    xls = pd.ExcelFile(INPUT_FILE)

    for sheet_name in xls.sheet_names:
        print(f"\n📘 Processing sheet: {sheet_name}")

        process_sheet(xls, sheet_name)

    print("\n✅ Done.")


if __name__ == "__main__":
    main()