import sys
import os
import re

def render_template(template_path):
    if not os.path.exists(template_path):
        print("Error: File does not exist.")
        return

    if not template_path.endswith('.template'):
        print("Error: Incorrect file extension.")
        return

    with open('settings.py', 'r') as settings_file:
        settings_content = settings_file.read()
        settings = {}
        exec(settings_content, settings)

    with open(template_path, 'r') as file:
        template_content = file.read()

    rendered_content = template_content
    for key, value in settings.items():
        if not key.startswith('__'):
            rendered_content = re.sub(r'\{' + key + r'\}', str(value), rendered_content)

    output_path = template_path.replace('.template', '.html')
    with open(output_path, 'w') as output_file:
        output_file.write(rendered_content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <file.template>")
    else:
        render_template(sys.argv[1])
