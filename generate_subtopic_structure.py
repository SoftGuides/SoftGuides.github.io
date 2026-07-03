import os
from pathlib import Path

root = Path('.')

categories = {
    'AI-Software': {
        'title': 'AI Software Tutorials',
        'description': 'AI software step-by-step tutorials for ChatGPT, Claude, Gemini, Copilot, Perplexity, Cursor, Midjourney, and NotebookLM.',
        'subtopics': [
            'ChatGPT', 'Claude', 'Gemini', 'Microsoft Copilot', 'Perplexity', 'Cursor', 'Midjourney', 'NotebookLM'
        ]
    },
    'Microsoft-Office': {
        'title': 'Microsoft Office Tutorials',
        'description': 'Microsoft Office tutorials for Excel, Word, PowerPoint, Outlook, and OneNote.',
        'subtopics': ['Excel', 'Word', 'PowerPoint', 'Outlook', 'OneNote']
    },
    'Google-Workspace': {
        'title': 'Google Workspace Tutorials',
        'description': 'Google Workspace tutorials for Docs, Sheets, Slides, Gmail, Drive, and Forms.',
        'subtopics': ['Google Docs', 'Google Sheets', 'Google Slides', 'Gmail', 'Google Drive', 'Google Forms']
    },
    'Design-Tools': {
        'title': 'Design Tools Tutorials',
        'description': 'Design tool tutorials for Canva, Photoshop, Illustrator, and Figma.',
        'subtopics': ['Canva', 'Adobe Photoshop', 'Adobe Illustrator', 'Figma']
    },
    'Video-Editing': {
        'title': 'Video Editing Tutorials',
        'description': 'Video editing tutorials for CapCut, DaVinci Resolve, and Adobe Premiere Pro.',
        'subtopics': ['CapCut', 'DaVinci Resolve', 'Adobe Premiere Pro']
    },
    'PDF-Tools': {
        'title': 'PDF Tools Tutorials',
        'description': 'PDF tool tutorials for Adobe Acrobat, PDFgear, Smallpdf, and PDF editing workflows.',
        'subtopics': ['Adobe Acrobat', 'PDFgear', 'Smallpdf', 'PDF Editing']
    },
    'Web-Blogging': {
        'title': 'Web & Blogging Tutorials',
        'description': 'Web and blogging tutorials for WordPress, Elementor, Rank Math, Cloudflare, and cPanel.',
        'subtopics': ['WordPress', 'Elementor', 'Rank Math', 'Cloudflare', 'cPanel']
    },
    'Productivity': {
        'title': 'Productivity Tutorials',
        'description': 'Productivity tutorials for Notion, Obsidian, Trello, Asana, and ClickUp.',
        'subtopics': ['Notion', 'Obsidian', 'Trello', 'Asana', 'ClickUp']
    },
    'Communication': {
        'title': 'Communication Tutorials',
        'description': 'Communication tool tutorials for Zoom, Microsoft Teams, Slack, and Discord.',
        'subtopics': ['Zoom', 'Microsoft Teams', 'Slack', 'Discord']
    },
    'Browser': {
        'title': 'Browser Tutorials',
        'description': 'Browser tutorials for Google Chrome, Microsoft Edge, Firefox, and Safari.',
        'subtopics': ['Google Chrome', 'Microsoft Edge', 'Firefox', 'Safari']
    },
    'Operating-Systems': {
        'title': 'Operating Systems Tutorials',
        'description': 'Operating system tutorials for Windows 11, macOS, and Ubuntu.',
        'subtopics': ['Windows 11', 'macOS', 'Ubuntu']
    },
    'Developer-Tools': {
        'title': 'Developer Tools Tutorials',
        'description': 'Developer tools tutorials for Git, GitHub, VS Code, and Docker.',
        'subtopics': ['Git', 'GitHub', 'VS Code', 'Docker']
    },
}

nav_links = [
    ('Home', 'index.html'),
    ('AI Software', 'AI-Software/index.html'),
    ('Microsoft Office', 'Microsoft-Office/index.html'),
    ('Google Workspace', 'Google-Workspace/index.html'),
    ('Design Tools', 'Design-Tools/index.html'),
    ('Video Editing', 'Video-Editing/index.html'),
    ('PDF Tools', 'PDF-Tools/index.html'),
    ('Web & Blogging', 'Web-Blogging/index.html'),
    ('Productivity', 'Productivity/index.html'),
    ('Communication', 'Communication/index.html'),
    ('Browser', 'Browser/index.html'),
    ('Operating Systems', 'Operating-Systems/index.html'),
    ('Developer Tools', 'Developer-Tools/index.html'),
    ('About', 'about.html'),
    ('Contact', 'contact.html'),
    ('Privacy Policy', 'privacy-policy.html'),
]

page_style = '''  <style>
    body { font-family: Arial, sans-serif; margin:0; padding:0; background:#f4f6fb; color:#111; }
    header, main, footer { max-width:980px; margin:0 auto; padding:20px; }
    header { background:#142d56; color:#fff; }
    header h1 { margin:0; font-size:2rem; }
    header p { margin:12px 0 0; font-size:1rem; color:#d3def4; }
    nav { margin-top:18px; line-height:1.8; }
    nav a { color:#c9d8f2; margin-right:14px; text-decoration:none; display:inline-block; margin-bottom:8px; }
    section { background:#fff; border-radius:14px; border:1px solid #d7dee8; padding:22px; box-shadow:0 8px 24px rgba(15,40,80,.08); margin-top:20px; }
    section h2 { margin-top:0; color:#132642; }
    section p { color:#3f4a5a; line-height:1.75; }
    ul { margin:16px 0 20px 20px; }
    li { margin-bottom:10px; }
    .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:18px; margin-top:18px; }
    .card { background:#f8fbff; border:1px solid #dfe6f4; border-radius:12px; padding:18px; }
    .card h3 { margin-top:0; font-size:1.1rem; color:#142642; }
    .card p { color:#4c556a; }
    .ad-block { margin:28px 0; }
    a.button { display:inline-block; padding:10px 16px; margin-top:10px; background:#142d56; color:#fff; border-radius:8px; text-decoration:none; }
  </style>'''

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="https://softguides.github.io/{canonical}" />
{style}
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9374368296307755" crossorigin="anonymous"></script>
</head>
<body>
  <header>
    <h1>{title}</h1>
    <p>{description}</p>
    <nav>
{nav}
    </nav>
  </header>
  <main>
{body}
    <div class="ad-block">
      <ins class="adsbygoogle"
        style="display:block"
        data-ad-client="ca-pub-9374368296307755"
        data-ad-slot="4652042516"
        data-ad-format="auto"
        data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>
  </main>
  <footer>
    <p>SoftGuides · Detailed tutorial and guide pages for software users.</p>
  </footer>
</body>
</html>
'''

subpage_template = '''  <section>
      <h2>{section_title}</h2>
      <p>{section_body}</p>
    </section>
'''

subtopic_url_slug = lambda name: name.lower().replace(' ', '-').replace('#', '').replace('++', 'pp').replace('.', '').replace('(', '').replace(')', '')

keywords_for_topic = lambda topic: topic.replace(' ', ', ').replace('Adobe,', 'Adobe')


def nav_html(base_path):
    return ''.join([f'      <a href="{href}">{label}</a>\n' for label, href in nav_links])


def create_category_index(category, data):
    subtopic_cards = []
    for sub in data['subtopics']:
        slug = subtopic_url_slug(sub)
        card = ('      <div class="card">\n'
                f'        <h3><a href="{slug}/index.html">{sub}</a></h3>\n'
                f'        <p>{sub} tutorial, tips, and practical guide content.</p>\n'
                '      </div>')
        subtopic_cards.append(card)
    body = ('    <section>\n'
            '      <h2>Category Overview</h2>\n'
            f'      <p>{data["description"]}</p>\n'
            '      <ul>\n'
            + ''.join([f'        <li>{sub} guide for practical usage and workflows.</li>\n' for sub in data['subtopics']])
            + '      </ul>\n'
            '    </section>\n'
            '    <section>\n'
            '      <h2>Subtopic Tutorials</h2>\n'
            '      <div class="grid">\n'
            + '\n'.join(subtopic_cards)
            + '\n      </div>\n'
            '    </section>\n')
    content = html_template.format(
        title=data['title'],
        description=data['description'],
        keywords=', '.join([topic for topic in data['subtopics']]),
        canonical=f'{category}/index.html',
        style=page_style,
        nav=nav_html(category),
        body=body,
    )
    target = root / category / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding='utf-8')
    print('Wrote category index:', target)


def create_subtopic_page(category, subtopic):
    slug = subtopic_url_slug(subtopic)
    title = f'{subtopic} Tutorial | {category.replace("-", " ")} Guide'
    description = f'Learn {subtopic} with step-by-step instructions, best practices, and practical workflow tips.'
    body = ''.join([
        subpage_template.format(section_title='What is ' + subtopic + '?',
                                 section_body=f'{subtopic} is a tool used for {category.lower().replace("-", " ")} tasks and workflows. This guide explains key features, setup, and practical tips.'),
        subpage_template.format(section_title='Getting Started',
                                 section_body=f'Start using {subtopic} by opening the app or website and setting up your account. Learn useful settings and initial configuration for better results.'),
        subpage_template.format(section_title='Key Features and Use Cases',
                                 section_body=f'Explore the most important {subtopic} features, such as collaboration, content creation, automation, or editing tools. Use these features to improve your efficiency.'),
        subpage_template.format(section_title='Best Practices',
                                 section_body=f'Use clear workflows and consistent naming when working with {subtopic}. Save templates, shortcuts, or prompt examples to speed up future tasks.'),
        subpage_template.format(section_title='Tips and Troubleshooting',
                                 section_body=f'If you encounter issues with {subtopic}, check settings, update the app, and review help articles. This section covers common fixes and productivity tips.'),
    ])
    page = html_template.format(
        title=title,
        description=description,
        keywords=keywords_for_topic(subtopic),
        canonical=f'{category}/{slug}/index.html',
        style=page_style,
        nav=nav_html(category),
        body=body + f'    <section>\n      <a class="button" href="../index.html">Back to {categories[category]["title"]}</a>\n    </section>',
    )
    target = root / category / slug / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(page, encoding='utf-8')
    print('Wrote subtopic page:', target)


if __name__ == '__main__':
    for category, data in categories.items():
        create_category_index(category, data)
        for subtopic in data['subtopics']:
            create_subtopic_page(category, subtopic)
