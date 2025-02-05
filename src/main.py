import os
import shutil

from converters import markdown_to_html_node
from extractors import extract_title
from utilities import copy_directory


current_directory = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_directory)
static_directory = os.path.join(project_root, "static")
public_directory = os.path.join(project_root, "public")
content_directory = os.path.join(project_root, "content")
template_file = os.path.join(project_root, "template.html")

def generate_page_recursively(from_directory, template_path, to_directory):
    for item in os.listdir(from_directory):
        from_path = os.path.join(from_directory, item)
        # Remove the .md extension and add .html
        to_path = os.path.join(to_directory, item.replace(".md", ".html"))
        if os.path.isdir(from_path):
            os.mkdir(to_path)
            generate_page_recursively(from_path, template_path, to_path)
        else:
            if item.endswith(".md"):
                generate_page(from_path, template_path, to_path)
            else:
                shutil.copy(from_path, to_path)

def generate_page(from_path, template_path, destination_path):
    print(f"Generating page from {from_path} to {destination_path} using {template_path}")
    with open(from_path, "r") as markdown_file:
        markdown = markdown_file.read()
    with open(template_path, "r") as html_template:
        template = html_template.read()
    html_node = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    content = html_node.to_html()
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    with open(destination_path, "w") as html_file:
        html_file.write(template)

def main():
    copy_directory(static_directory, public_directory)
    generate_page_recursively(content_directory, template_file, public_directory)

if __name__ == "__main__":
    main()