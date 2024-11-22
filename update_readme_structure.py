import os

def generate_repo_structure(path="."):
    """
    Генерирует структуру репозитория в виде отступов для файлов и папок
    """
    repo_structure = []
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        repo_structure.append(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for file in files:
            repo_structure.append(f"{subindent}{file}")
    return '\n'.join(repo_structure)

structure = generate_repo_structure()
with open("README.md", "r", encoding="utf-8") as file:
    readme_content = file.read()

structure_section = "\n## Структура репозитория\n```\n" + structure + "\n```"

if "## Структура репозитория" in readme_content:
    updated_readme = readme_content.replace("## Структура репозитория", structure_section)
else:
    updated_readme = readme_content + structure_section

with open("README.md", "w", encoding="utf-8") as file:
    file.write(updated_readme)

print("README обновлен с автоматической структурой репозитория!")