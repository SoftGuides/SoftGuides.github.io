from pathlib import Path
import re

root = Path('.')
nav_html = '''    <nav>
      <a href="../index.html">Home</a>
      <a href="../AI-Software/index.html">AI Software</a>
      <a href="../Microsoft-Office/index.html">Microsoft Office</a>
      <a href="../Google-Workspace/index.html">Google Workspace</a>
      <a href="../Design-Tools/index.html">Design Tools</a>
      <a href="../Video-Editing/index.html">Video Editing</a>
      <a href="../PDF-Tools/index.html">PDF Tools</a>
      <a href="../Web-Blogging/index.html">Web & Blogging</a>
      <a href="../Productivity/index.html">Productivity</a>
      <a href="../Communication/index.html">Communication</a>
      <a href="../Browser/index.html">Browser</a>
      <a href="../Operating-Systems/index.html">Operating Systems</a>
      <a href="../Developer-Tools/index.html">Developer Tools</a>
    </nav>'''

for path in sorted(root.glob('*/*.html')):
    text = path.read_text(encoding='utf-8')
    if '<nav>' in text:
        new_text = re.sub(r'<nav>[\s\S]*?</nav>', nav_html, text, count=1)
        if new_text != text:
            path.write_text(new_text, encoding='utf-8')
            print(f'Updated nav in {path}')
    elif '</header>' in text:
        new_text = text.replace('</header>', nav_html + '\n  </header>', 1)
        path.write_text(new_text, encoding='utf-8')
        print(f'Inserted nav in {path}')
    else:
        print(f'No header/nav found in {path}')
