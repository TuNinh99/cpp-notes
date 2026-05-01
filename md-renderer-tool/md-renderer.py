import os
import pandas as pd
from slugify import slugify
import re

INPUT_FILE = "cpp-docs.xlsx"
OUTPUT_DIR = "../docs"

def clean_text(text):
    if pd.isna(text):
        return ""
    return str(text).strip()

def format_note(note: str) -> str:
    if not note:
        return ""

    note = note.replace("Ưu điểm", "### ✅ Ưu điểm")
    note = note.replace("Nhược điểm", "### ❌ Nhược điểm")

    return note

def escape_mdx(text: str) -> str:
    # chỉ escape khi là kiểu C++ template
    text = re.sub(r"<([a-zA-Z0-9_,:\s]+)>", r"&lt;\1&gt;", text)
    return text

def escape_braces(text: str) -> str:
    if not text:
        return ""

    text = text.replace("{", "&#123;").replace("}", "&#125;")
    return text

def sanitize_mdx(text: str) -> str:
    if not text:
        return ""

    text = text.replace("•", "-")

    # escape nguy hiểm cho MDX
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    text = text.replace("{", "&#123;").replace("}", "&#125;")

    return text

def wrap_code(text: str) -> str:
    if "std::" in text or "<" in text:
        return f"\n```cpp\n{text}\n```\n"
    return text

def structure_content(content: str) -> str:
    lines = content.split("\n")

    new_lines = []
    for line in lines:
        line = line.strip()

        if line.startswith("1."):
            new_lines.append(f"### {line}")
        elif line.startswith("-"):
            new_lines.append(line)
        else:
            new_lines.append(line)

    return "\n".join(new_lines)

def format_code_blocks(text: str) -> str:
    if "std::" in text:
        return text.replace(
            "std::lock_guard<std::mutex> lock(mtx);",
            "\n```cpp\nstd::lock_guard<std::mutex> lock(mtx);\n```\n"
        )
    return text

def format_content(content: str) -> str:
    if not content:
        return ""

    # bullet đẹp hơn
    content = content.replace("•", "-")

    # fix spacing
    content = content.replace("\r\n", "\n").strip()

    return content

def generate_markdown(no, title, content, note):
    content = sanitize_mdx(content)
    # content = format_code_blocks(content)
    # content = structure_content(content)

    note = sanitize_mdx(note)
    content = wrap_code(content)

    return f"""---
title: "{title}"
---

# {no}. {title}

## 🧾 Content

{content}

## 📝 Note

{note}
"""

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    xls = pd.ExcelFile(INPUT_FILE)

    for sheet_name in xls.sheet_names:
        df = xls.parse(sheet_name)

        # Tạo folder cho sheet
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

            file_name = f"{no}-{slugify(title)}.md"
            file_path = os.path.join(folder_path, file_name)

            md_content = generate_markdown(no, title, content, note)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(md_content)

            print(f"✔ Generated: {file_path}")


if __name__ == "__main__":
    main()