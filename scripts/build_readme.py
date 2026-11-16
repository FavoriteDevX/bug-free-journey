import os
import re

ROOT_DIR = "."
README_PATH = "README.md"
EXCLUDED_DIRS = {".git", ".github", "scripts", "templates"}

def get_title_from_md(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.basename(filepath)

def generate_index():
    categories = {}

    for item in sorted(os.listdir(ROOT_DIR)):
        item_path = os.path.join(ROOT_DIR, item)
        if os.path.isdir(item_path) and item not in EXCLUDED_DIRS and not item.startswith("."):
            entries = []
            for file in sorted(os.listdir(item_path)):
                if file.endswith(".md"):
                    filepath = os.path.join(item_path, file)
                    title = get_title_from_md(filepath)
                    rel_path = f"{item}/{file}"
                    entries.append(f"- [{title}]({rel_path})")
            if entries:
                categories[item.capitalize()] = entries

    index_lines = []
    for category, entries in categories.items():
        index_lines.append(f"### {category}")
        index_lines.extend(entries)
        index_lines.append("")

    return "\n".join(index_lines).strip()

def update_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_index = generate_index()
    pattern = r"(<!-- INDEX_START -->)(.*?)(<!-- INDEX_END -->)"
    replacement = f"\\1\n{new_index}\n\\3"

    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    update_readme()
    print("README.md index updated successfully!")
