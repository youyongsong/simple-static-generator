#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil, os
import markdown


BASE_DIR = os.getcwd()

MARKDOWN_EXT = ['.md', '.markdown', '.mk']
HTML_EXT = '.html'

HTML_WRAPPER = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="{path}/static/vendor/jquery/jquery-ui.min.css">
  <link rel="stylesheet" href="{path}/static/vendor/bootstrap/css/bootstrap.min.css">
  <link rel="stylesheet" href="{path}/static/vendor/pygments/github.css">
  <title> {title} </title>
</head>
<body>
  <main class="container">
  {content}
  </main>
<script src="{path}/static/vendor/jquery/jquery-2.1.3.min.js"></script>
<script src="{path}/static/vendor/jquery/jquery-ui.min.js"></script>
<script src="{path}/static/app.js"></script>
</body>
</html>
'''

LI_WRAPPER = '''
<li><a href="{href}">{li_name}</a></li>
'''

ACCORDION_WRAPPER = '''
<div class="accordion">
{content}
</div>
'''

def generate_index(path_name):
    htm = []
    for file_name in os.listdir(path_name):
        file_name = os.path.join(path_name, file_name)
        if os.path.isdir(file_name):
            htm.append('<h3>' + os.path.basename(file_name) + '</h3>')
            htm.append(generate_index_core(file_name))
        if file_name.endswith('.html'):
            htm.append(
                LI_WRAPPER.format(
                    href = file_name,
                    li_name = os.path.basename(file_name)[:-5])
            )
    return ACCORDION_WRAPPER.format(content=os.linesep.join(htm))


def generate_index_core(path_name):
    htm = '<div class="accordion">'
    for file_name in os.listdir(path_name):
        file_name = os.path.join(path_name, file_name)
        if os.path.isdir(file_name):
            htm += '<h3>' + os.path.basename(path_name) + '</h3>'
            htm += generate_index_core(file_name)
        if file_name.endswith('.html'):
            htm += LI_WRAPPER.format(
                href = file_name,
                li_name = os.path.basename(file_name)[:-5]
            )
    htm += '</div>'
    return htm


if __name__ == '__main__':
    if not os.path.isdir('src'):
        print('No src directory detected.')

    elif os.path.isdir('build'):
        print('Please delete the build diectory and try again.')

    else:
        shutil.copytree('src', 'build')
        for current_dir, sub_dirs, file_names in os.walk('build'):
            for file_name in file_names:
                old_name = os.path.join(current_dir, file_name)
                base, ext = os.path.splitext(old_name)
                if ext in MARKDOWN_EXT:
                    with open(old_name, 'r+') as f:
                        content = markdown.markdown(
                            f.read(),
                            extensions = [
                                'markdown.extensions.fenced_code',
                                'markdown.extensions.codehilite'
                            ],
                            safe_mode=True,
                            enable_attributes=False,
                        )
                        html = HTML_WRAPPER.format(
                            path = BASE_DIR,
                            title = os.path.basename(base),
                            content = content
                        )
                        f.truncate(0)
                        f.write(html)
                    new_name = base + HTML_EXT
                    os.rename(old_name, new_name)

        with open('index.html', 'w') as f:
            html = HTML_WRAPPER.format(
                path = BASE_DIR,
                title = 'Index',
                content = generate_index('build')
            )
            f.write(html)
