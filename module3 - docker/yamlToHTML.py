import yaml
import os
from jinja2 import Template

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def render_html(template_path, data):
    with open(template_path, 'r') as file:
        template_content = file.read()
    template = Template(template_content)
    html_output = template.render(data)
    return html_output

def save_html(html_content, output_path):
    with open(output_path, 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    yaml_file_path = "resume.yaml"
    html_template_path = "template.html"
    output_html_path = "/build/output.html"

    resume_data = load_yaml(yaml_file_path)
    html_content = render_html(html_template_path, resume_data)
    save_html(html_content, output_html_path)
