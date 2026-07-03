from pathlib import Path

root = Path('.')

categories = {
    'AI-Software': {
        'title': 'AI Software Tutorials',
        'description': 'AI software tutorials for ChatGPT, Claude, Gemini, Copilot, Perplexity, Cursor, Midjourney, and NotebookLM with practical prompts, workflows, and tool guides.',
        'keywords': 'AI software, ChatGPT tutorial, Claude tutorial, Gemini AI, Copilot guide, Midjourney prompts, NotebookLM guide',
        'subtopics': ['ChatGPT', 'Claude', 'Gemini', 'Microsoft Copilot', 'Perplexity', 'Cursor', 'Midjourney', 'NotebookLM'],
    },
    'Microsoft-Office': {
        'title': 'Microsoft Office Tutorials',
        'description': 'Microsoft Office tutorials for Excel, Word, PowerPoint, Outlook, and OneNote. Learn productivity workflows, document formatting, and data analysis.',
        'keywords': 'Microsoft Office tutorial, Excel guide, Word tips, PowerPoint tutorial, Outlook help, OneNote tutorial',
        'subtopics': ['Excel', 'Word', 'PowerPoint', 'Outlook', 'OneNote'],
    },
    'Google-Workspace': {
        'title': 'Google Workspace Tutorials',
        'description': 'Google Workspace tutorials for Docs, Sheets, Slides, Gmail, Drive, and Forms. Improve collaboration, document workflows, and automation.',
        'keywords': 'Google Workspace tutorial, Google Docs guide, Google Sheets tutorial, Gmail tips, Google Drive help, Google Forms',
        'subtopics': ['Google Docs', 'Google Sheets', 'Google Slides', 'Gmail', 'Google Drive', 'Google Forms'],
    },
    'Design-Tools': {
        'title': 'Design Tools Tutorials',
        'description': 'Design tool tutorials for Canva, Photoshop, Illustrator, and Figma. Create graphics, branding, layouts, and UX mockups efficiently.',
        'keywords': 'Design tutorial, Canva guide, Photoshop tutorial, Illustrator tips, Figma tutorial',
        'subtopics': ['Canva', 'Adobe Photoshop', 'Adobe Illustrator', 'Figma'],
    },
    'Video-Editing': {
        'title': 'Video Editing Tutorials',
        'description': 'Video editing tutorials for CapCut, DaVinci Resolve, and Adobe Premiere Pro. Learn editing workflows, transitions, and export best practices.',
        'keywords': 'Video editing tutorial, CapCut guide, DaVinci Resolve tutorial, Premiere Pro guide',
        'subtopics': ['CapCut', 'DaVinci Resolve', 'Adobe Premiere Pro'],
    },
    'PDF-Tools': {
        'title': 'PDF Tools Tutorials',
        'description': 'PDF tool tutorials for Adobe Acrobat, PDFgear, Smallpdf, and PDF editing workflows. Learn to create, edit, convert, and secure PDF files.',
        'keywords': 'PDF tutorial, Adobe Acrobat guide, PDFgear tutorial, Smallpdf tutorial, PDF editing',
        'subtopics': ['Adobe Acrobat', 'PDFgear', 'Smallpdf', 'PDF Editing'],
    },
    'Web-Blogging': {
        'title': 'Web & Blogging Tutorials',
        'description': 'Web and blogging tutorials for WordPress, Elementor, Rank Math, Cloudflare, and cPanel. Build fast blogs, optimize SEO, and manage hosting.',
        'keywords': 'WordPress tutorial, Elementor guide, Rank Math tutorial, Cloudflare setup, cPanel tutorial',
        'subtopics': ['WordPress', 'Elementor', 'Rank Math', 'Cloudflare', 'cPanel'],
    },
    'Productivity': {
        'title': 'Productivity Tutorials',
        'description': 'Productivity tutorials for Notion, Obsidian, Trello, Asana, and ClickUp. Organize projects, notes, and team workflows effectively.',
        'keywords': 'Productivity tutorial, Notion guide, Obsidian tutorial, Trello workflow, Asana guide, ClickUp tutorial',
        'subtopics': ['Notion', 'Obsidian', 'Trello', 'Asana', 'ClickUp'],
    },
    'Communication': {
        'title': 'Communication Tutorials',
        'description': 'Communication tutorials for Zoom, Microsoft Teams, Slack, and Discord. Learn meetings, chat workflows, and team collaboration best practices.',
        'keywords': 'Zoom tutorial, Microsoft Teams guide, Slack tutorial, Discord guide, communication tools',
        'subtopics': ['Zoom', 'Microsoft Teams', 'Slack', 'Discord'],
    },
    'Browser': {
        'title': 'Browser Tutorials',
        'description': 'Browser tutorials for Google Chrome, Microsoft Edge, Firefox, and Safari. Improve speed, privacy, and extension workflows.',
        'keywords': 'Google Chrome tutorial, Microsoft Edge guide, Firefox tutorial, Safari tips, browser guide',
        'subtopics': ['Google Chrome', 'Microsoft Edge', 'Firefox', 'Safari'],
    },
    'Operating-Systems': {
        'title': 'Operating System Tutorials',
        'description': 'Operating system tutorials for Windows 11, macOS, and Ubuntu. Learn setup, productivity, and system maintenance best practices.',
        'keywords': 'Windows 11 tutorial, macOS guide, Ubuntu tutorial, operating system tips',
        'subtopics': ['Windows 11', 'macOS', 'Ubuntu'],
    },
    'Developer-Tools': {
        'title': 'Developer Tools Tutorials',
        'description': 'Developer tools tutorials for Git, GitHub, VS Code, and Docker. Learn coding workflows, version control, and container development.',
        'keywords': 'Git tutorial, GitHub guide, VS Code tutorial, Docker tutorial',
        'subtopics': ['Git', 'GitHub', 'VS Code', 'Docker'],
    },
}

nav_links = [
    ('Home', '../index.html'),
    ('AI Software', '../AI-Software/index.html'),
    ('Microsoft Office', '../Microsoft-Office/index.html'),
    ('Google Workspace', '../Google-Workspace/index.html'),
    ('Design Tools', '../Design-Tools/index.html'),
    ('Video Editing', '../Video-Editing/index.html'),
    ('PDF Tools', '../PDF-Tools/index.html'),
    ('Web & Blogging', '../Web-Blogging/index.html'),
    ('Productivity', '../Productivity/index.html'),
    ('Communication', '../Communication/index.html'),
    ('Browser', '../Browser/index.html'),
    ('Operating Systems', '../Operating-Systems/index.html'),
    ('Developer Tools', '../Developer-Tools/index.html'),
    ('About', '../about.html'),
    ('Contact', '../contact.html'),
    ('Privacy Policy', '../privacy-policy.html'),
]

page_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="https://softguides.github.io/{canonical}" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:type" content="website" />
  <style>
    body {{ font-family: Arial, sans-serif; margin:0; padding:0; background:#f4f6fb; color:#111; }}
    header, main, footer {{ max-width:980px; margin:0 auto; padding:20px; }}
    header {{ background:#12264e; color:#fff; }}
    header h1 {{ margin:0; font-size:2.3rem; }}
    header p {{ margin:12px 0 0; font-size:1rem; color:#d1d9f1; line-height:1.8; }}
    nav {{ margin-top:18px; }}
    nav a {{ color:#b8d7ff; margin-right:16px; text-decoration:none; display:inline-block; margin-bottom:8px; }}
    .hero {{ background:#e8eef9; border-radius:16px; padding:24px; border:1px solid #d8e3f0; box-shadow:0 12px 28px rgba(16,40,86,.08); }}
    .hero h2 {{ margin-top:0; color:#14284f; }}
    .hero p {{ color:#3d4b6f; line-height:1.75; }}
    .hero ul {{ margin:16px 0 0 20px; color:#33415b; }}
    section {{ background:#fff; border-radius:14px; border:1px solid #dde3ee; padding:22px; box-shadow:0 8px 24px rgba(15,40,80,.06); margin-top:20px; }}
    section h2 {{ margin-top:0; color:#12264e; }}
    section p {{ color:#3c4a6e; line-height:1.75; }}
    ul {{ margin:16px 0 20px 20px; color:#33415b; }}
    li {{ margin-bottom:10px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:18px; margin-top:22px; }}
    .card {{ background:#fff; border:1px solid #dfe6f0; border-radius:14px; padding:20px; box-shadow:0 6px 22px rgba(0,0,0,.05); }}
    .card h3 {{ margin-top:0; font-size:1.15rem; color:#142a4f; }}
    .card p {{ color:#4a5568; line-height:1.75; }}
    .ad-block {{ margin:28px 0; }}
    a.button {{ display:inline-block; padding:12px 18px; margin-top:14px; background:#12264e; color:#fff; border-radius:8px; text-decoration:none; }}
  </style>
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
    <section class="hero">
      <h2>{hero_title}</h2>
      <p>{hero_text}</p>
      <ul>
{hero_list}
      </ul>
    </section>
    <section>
      <h2>{section_title}</h2>
      <p>{section_text}</p>
    </section>
    <section>
      <h2>{topics_title}</h2>
      <ul>
{topic_list}
      </ul>
    </section>
    <section>
      <h2>{featured_title}</h2>
      <div class="grid">
{cards}
      </div>
    </section>
    <section>
      <h2>{action_title}</h2>
      <p>{action_text}</p>
      <a class="button" href="{first_link}">{first_text}</a>
    </section>
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
    <p>SoftGuides · Detailed tutorials and guides for software users.</p>
  </footer>
</body>
</html>
'''


def make_slug(name: str) -> str:
    return name.lower().replace(' ', '-').replace('++', 'pp').replace('.', '').replace('(', '').replace(')', '')


def nav_html():
    return ''.join([f'      <a href="{href}">{label}</a>\n' for label, href in nav_links])


def create_category_index(category: str, data: dict):
    hero_title = f'Complete {data["title"]} and Tutorials'
    hero_text = f'{data["description"]} Explore the latest AI and productivity tools with guides, examples, and quick-start tips.'
    hero_list = ''.join([f'        <li>{subtopic} tutorial and practical examples.</li>\n' for subtopic in data['subtopics']])
    section_title = 'Why This Category Matters'
    section_text = f'Users search for {data["keywords"]}. This category page organizes detailed guides, tool comparisons, and actionable workflows for real-world use.'
    topics_title = 'What You Will Learn'
    topic_list = ''.join([f'        <li>How to use {subtopic} for better results, workflows, and productivity.</li>\n' for subtopic in data['subtopics']])
    cards = ''
    for subtopic in data['subtopics']:
        slug = make_slug(subtopic)
        cards += ('        <div class="card">\n'
                  f'          <h3><a href="{slug}/index.html">{subtopic}</a></h3>\n'
                  f'          <p>{subtopic} tutorial, practical tips, and useful workflows.</p>\n'
                  '        </div>\n')
    first_link = f'{make_slug(data["subtopics"][0])}/index.html'
    first_text = f'Start with {data["subtopics"][0]}'

    content = page_template.format(
        title=f'{data["title"]} | {", ".join(data["subtopics"][:3])} and More',
        description=data['description'],
        keywords=data['keywords'],
        canonical=f'{category}/index.html',
        nav=nav_html(),
        hero_title=hero_title,
        hero_text=hero_text,
        hero_list=hero_list,
        section_title=section_title,
        section_text=section_text,
        topics_title=topics_title,
        topic_list=topic_list,
        featured_title='Featured Tutorials',
        cards=cards,
        action_title='Choose the Best Tutorial for Your Needs',
        action_text='Use the card links above to start the tutorial that matches your goal. Each page is designed to help you learn quickly and rank better in search results.',
        first_link=first_link,
        first_text=first_text,
    )

    path = root / category / 'index.html'
    path.write_text(content, encoding='utf-8')
    print(f'Updated {path}')


if __name__ == '__main__':
    for category, data in categories.items():
        create_category_index(category, data)
