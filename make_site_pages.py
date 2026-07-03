import os

root = r"c:\Users\com\Desktop\테스트프로\SoftGuides.github.io"

categories = [
    ("AI Software", "AI-Software", "AI Software tutorials for ChatGPT, Claude, Gemini, Microsoft Copilot, Midjourney, and NotebookLM."),
    ("Microsoft Office", "Microsoft-Office", "Microsoft Office tutorials for Excel, Word, PowerPoint, Outlook, and OneNote."),
    ("Google Workspace", "Google-Workspace", "Google Workspace tutorials for Google Docs, Sheets, Slides, Gmail, Drive, and Forms."),
    ("Design Tools", "Design-Tools", "Design tutorials for Canva, Adobe Photoshop, Adobe Illustrator, and Figma."),
    ("Video Editing", "Video-Editing", "Video editing tutorials for CapCut, DaVinci Resolve, and Adobe Premiere Pro."),
    ("PDF Tools", "PDF-Tools", "PDF tool tutorials for Adobe Acrobat, PDFgear, Smallpdf, and PDF editing workflows."),
    ("Web & Blogging", "Web-Blogging", "Web and blogging tutorials for WordPress, Elementor, Rank Math, Cloudflare, and cPanel."),
    ("Productivity", "Productivity", "Productivity tutorials for Notion, Obsidian, Trello, Asana, and ClickUp."),
    ("Communication", "Communication", "Communication software tutorials for Zoom, Microsoft Teams, Slack, and Discord."),
    ("Browser", "Browser", "Browser tutorials for Google Chrome, Microsoft Edge, Firefox, and Safari."),
    ("Operating Systems", "Operating-Systems", "Operating system tutorials for Windows 11, macOS, and Ubuntu."),
    ("Developer Tools", "Developer-Tools", "Developer tools tutorials for Git, GitHub, VS Code, and Docker."),
]

articles = [
    ("Microsoft Office", "Microsoft-Office", "Excel Guide", "excel-guide.html", "Excel Tutorial | Formulas, PivotTables, and Data Analysis", "Learn how to use Excel formulas, PivotTables, and charts for business reporting and data analysis."),
    ("Google Workspace", "Google-Workspace", "Google Sheets Guide", "google-sheets-guide.html", "Google Sheets Tutorial | Spreadsheets, Functions, and Automation", "Learn how to use Google Sheets formulas, formatting, and automation to boost productivity."),
    ("Design Tools", "Design-Tools", "Canva Guide", "canva-guide.html", "Canva Tutorial | Create Social Media Designs and Graphics", "Learn how to create professional designs in Canva for social media, presentations, and branding."),
    ("Video Editing", "Video-Editing", "CapCut Guide", "capcut-guide.html", "CapCut Tutorial | Video Editing for Beginners", "Learn CapCut editing basics, transitions, effects, and export settings for mobile videos."),
    ("PDF Tools", "PDF-Tools", "Adobe Acrobat Guide", "adobe-acrobat-guide.html", "Adobe Acrobat Tutorial | Edit and Convert PDF Files", "Learn Adobe Acrobat features for editing, annotating, and converting PDF files."),
    ("Web & Blogging", "Web-Blogging", "WordPress Guide", "wordpress-guide.html", "WordPress Tutorial | Build a Blog with SEO and Hosting", "Learn how to set up WordPress, optimize SEO, and manage blog content."),
    ("Productivity", "Productivity", "Notion Guide", "notion-guide.html", "Notion Tutorial | Organize Notes, Projects, and Teams", "Learn how to use Notion for knowledge management, project planning, and workflows."),
    ("Communication", "Communication", "Zoom Guide", "zoom-guide.html", "Zoom Tutorial | Meetings, Webinars, and Collaboration", "Learn how to run Zoom meetings, webinars, screen sharing, and settings."),
    ("Browser", "Browser", "Chrome Guide", "chrome-guide.html", "Google Chrome Tutorial | Browser Tips and Extensions", "Learn Chrome shortcuts, extensions, and privacy settings for faster browsing."),
    ("Operating Systems", "Operating-Systems", "Windows 11 Guide", "windows11-guide.html", "Windows 11 Tutorial | Setup, Shortcuts, and Productivity", "Learn Windows 11 features, settings, and productivity tips."),
    ("Developer Tools", "Developer-Tools", "VS Code Guide", "vscode-guide.html", "VS Code Tutorial | Editor Setup and Productivity Tips", "Learn Visual Studio Code setup, extensions, and developer workflows."),
]

nav_links = [
    ("Home", "../index.html"),
    ("AI Software", "../AI-Software/index.html"),
    ("Microsoft Office", "../Microsoft-Office/index.html"),
    ("Google Workspace", "../Google-Workspace/index.html"),
    ("Design Tools", "../Design-Tools/index.html"),
    ("Video Editing", "../Video-Editing/index.html"),
    ("PDF Tools", "../PDF-Tools/index.html"),
    ("Web & Blogging", "../Web-Blogging/index.html"),
    ("Productivity", "../Productivity/index.html"),
    ("Communication", "../Communication/index.html"),
    ("Browser", "../Browser/index.html"),
    ("Operating Systems", "../Operating-Systems/index.html"),
    ("Developer Tools", "../Developer-Tools/index.html"),
]

nav_html = "\n".join(f'      <a href="{href}">{label}</a>' for label, href in nav_links)

index_cards = "\n".join(
    f'        <div class="category-card">\n          <h2>{name}</h2>\n          <p>{description}</p>\n          <a class="button" href="{folder}/index.html">View {name}</a>\n        </div>'
    for name, folder, description in categories
)

index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>SoftGuides | Software Tutorials for AI, Office, Design, and Productivity</title>
  <meta name="description" content="SoftGuides provides SEO-friendly software tutorials for AI tools, Microsoft Office, Google Workspace, design, productivity, and developer tools. Learn how to use ChatGPT, Excel, Canva, VS Code and more." />
  <meta name="keywords" content="software tutorials, AI software guide, ChatGPT tutorial, Microsoft Office tips, Google Workspace tutorials, Canva guide, VS Code, blog, Adsense" />
  <link rel="canonical" href="https://softguides.github.io/" />
  <style>
    body { font-family: Arial, sans-serif; margin:0; padding:0; line-height:1.6; color:#111; background:#f7f7f7; }
    header, main, footer { max-width:1080px; margin:0 auto; padding:20px; }
    header { background:#0a1f44; color:#fff; }
    header h1 { margin:0 0 10px; font-size:2.4rem; }
    nav { margin-top:14px; }
    nav a { color:#a8d4ff; text-decoration:none; margin-right:14px; display:inline-block; margin-bottom:8px; }
    .hero { padding:32px 0; }
    .hero p { max-width:760px; font-size:1.1rem; }
    .category-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:18px; margin-top:24px; }
    .category-card { background:#fff; border:1px solid #dde3ec; padding:20px; border-radius:12px; box-shadow:0 4px 16px rgba(0,0,0,0.05); }
    .category-card h2 { margin:0 0 12px; font-size:1.2rem; color:#0a1f44; }
    .category-card p { margin:0 0 16px; color:#444; }
    .adsense { margin:28px 0; }
    footer { padding:24px 0 40px; color:#555; font-size:.95rem; }
    a.button { display:inline-block; margin-top:14px; padding:10px 16px; background:#0a1f44; color:#fff; border-radius:8px; text-decoration:none; }
  </style>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9374368296307755" crossorigin="anonymous"></script>
</head>
<body>
  <header>
    <h1>SoftGuides</h1>
    <p>Quality software tutorials for AI tools, productivity apps, office suites, design tools, and developer workflows.</p>
    <nav>
{nav_html}
    </nav>
  </header>
  <main>
    <section class="hero">
      <h2>Beginner-friendly software tutorials built for Google search and AdSense revenue</h2>
      <p>Start with practical guides, structured content, and clear steps for the most popular tools. Each category page is optimized for search visibility and includes relevant internal links for better ranking.</p>
    </section>
    <div class="adsense">
      <ins class="adsbygoogle"
        style="display:block"
        data-ad-client="ca-pub-9374368296307755"
        data-ad-slot="4652042516"
        data-ad-format="auto"
        data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>
    <section>
      <h2>Categories</h2>
      <div class="category-grid">
{index_cards}
      </div>
    </section>
  </main>
  <footer>
    <p>SoftGuides by SoftGuides.github.io · SEO-friendly software tutorials for global readers.</p>
  </footer>
</body>
</html>
"""

for name, folder, description in categories:
    folder_path = os.path.join(root, folder)
    os.makedirs(folder_path, exist_ok=True)
    article_list = []
    if folder == "AI-Software":
        article_list = [
            ("ChatGPT Tutorial", "chatgpt-guide.html"),
            ("Midjourney Guide", "midjourney-guide.html"),
            ("Microsoft Copilot Guide", "copilot-guide.html"),
        ]
    else:
        for art_name, art_folder, title, filename, art_title, art_desc in articles:
            if art_folder == folder:
                article_list.append((title, filename))
    article_links = "\n".join(f'            <li><a href="{filename}">{title}</a></li>' for title, filename in article_list)
    sample_text = f"Explore the most important tutorials in {name}. Browse the guides below to learn each tool step by step."
    page_html = f"""<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>{name} Tutorials | SoftGuides</title>
  <meta name=\"description\" content=\"{description} Learn actionable tutorials, tips, and how-to guides for {name}.\" />
  <meta name=\"keywords\" content=\"{name} tutorials, {name} guide, software tutorial, how-to, tips, SEO friendly\" />
  <link rel=\"canonical\" href=\"https://softguides.github.io/{folder}/index.html\" />
  <style>
    body {{ font-family: Arial, sans-serif; margin:0; padding:0; background:#f4f7fb; color:#111; }}
    header, main, footer {{ max-width:980px; margin:0 auto; padding:20px; }}
    header {{ background:#12264e; color:#fff; }}
    header h1 {{ margin:0; font-size:2rem; }}
    header p {{ margin:12px 0 0; font-size:1rem; color:#c7d6ef; }}
    nav {{ margin-top:16px; }}
    nav a {{ color:#c7d6ef; margin-right:14px; text-decoration:none; display:inline-block; margin-bottom:8px; }}
    .section-card {{ background:#fff; border:1px solid #dfe6f0; border-radius:12px; padding:22px; box-shadow:0 6px 24px rgba(10,23,55,.05); margin-top:20px; }}
    .section-card h2 {{ margin-top:0; color:#14243a; }}
    .section-card p {{ color:#404a5b; }}
    .ad-block {{ margin:28px 0; }}
    ul {{ margin:16px 0 24px 20px; }}
    a.button {{ display:inline-block; padding:10px 16px; margin-top:10px; background:#12264e; color:#fff; border-radius:8px; text-decoration:none; }}
  </style>
  <script async src=\"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9374368296307755\" crossorigin=\"anonymous\"></script>
</head>
<body>
  <header>
    <h1>{name} Tutorials</h1>
    <p>Actionable tutorials, tips, and walkthroughs for {name} tools and workflows.</p>
    <nav>
{nav_html}
    </nav>
  </header>
  <main>
    <section class=\"section-card\">
      <h2>Overview</h2>
      <p>{sample_text}</p>
      <p>Browse popular tutorials, get practical advice, and learn how to use {name} tools for real work and creative projects.</p>
    </section>
    <section class=\"section-card\">
      <h2>Featured Guides</h2>
      <ul>
{article_links}
      </ul>
      <a class=\"button\" href=\"../index.html\">Back to Home</a>
    </section>
    <div class=\"ad-block\">
      <ins class=\"adsbygoogle\"
        style=\"display:block\"
        data-ad-client=\"ca-pub-9374368296307755\"
        data-ad-slot=\"4652042516\"
        data-ad-format=\"auto\"
        data-full-width-responsive=\"true\"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>
  </main>
  <footer>
    <p>SoftGuides · {name} tutorials optimized for search engines and AdSense performance.</p>
  </footer>
</body>
</html>
"""
    with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as f:
        f.write(page_html)

article_template = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>{page_title}</title>
  <meta name=\"description\" content=\"{page_description}\" />
  <meta name=\"keywords\" content=\"{keywords}\" />
  <link rel=\"canonical\" href=\"https://softguides.github.io/{folder}/{filename}\" />
  <style>
    body {{ font-family: Arial, sans-serif; margin:0; padding:0; background:#f7f9ff; color:#111; }}
    header, main, footer {{ max-width:880px; margin:0 auto; padding:20px; }}
    header {{ background:#1d3253; color:#fff; }}
    header h1 {{ margin:0; font-size:2rem; }}
    header p {{ margin:12px 0 0; font-size:1rem; color:#c7d6ef; }}
    nav {{ margin-top:16px; }}
    nav a {{ color:#c7d6ef; margin-right:14px; text-decoration:none; display:inline-block; margin-bottom:8px; }}
    .section-card {{ background:#fff; border-radius:14px; border:1px solid #dde3ec; padding:22px; box-shadow:0 6px 24px rgba(10,23,55,.05); margin-top:20px; }}
    .section-card h2 {{ margin-top:0; color:#14243a; }}
    .section-card p {{ color:#404a5b; }}
    .ad-block {{ margin:28px 0; }}
    ul {{ margin:16px 0 24px 20px; }}
    a.button {{ display:inline-block; padding:10px 16px; margin-top:10px; background:#1d3253; color:#fff; border-radius:8px; text-decoration:none; }}
  </style>
  <script async src=\"https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9374368296307755\" crossorigin=\"anonymous\"></script>
</head>
<body>
  <header>
    <h1>{page_title}</h1>
    <p>{page_description}</p>
    <nav>
{nav_html}
    </nav>
  </header>
  <main>
    <section class=\"section-card\">
      <h2>Quick Start</h2>
      <p>{intro_text}</p>
      <ul>
{steps}
      </ul>
    </section>
    <section class=\"section-card\">
      <h2>Best Practices</h2>
      <ul>
{best_practices}
      </ul>
    </section>
    <div class=\"ad-block\">
      <ins class=\"adsbygoogle\"
        style=\"display:block\"
        data-ad-client=\"ca-pub-9374368296307755\"
        data-ad-slot=\"4652042516\"
        data-ad-format=\"auto\"
        data-full-width-responsive=\"true\"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>
    <section class=\"section-card\">
      <h2>Next Steps</h2>
      <p>{conclusion}</p>
      <a class=\"button\" href=\"index.html\">Back to {category_name}</a>
    </section>
  </main>
  <footer>
    <p>SoftGuides · SEO-friendly {category_name} tutorial page.</p>
  </footer>
</body>
</html>
"""

for category_name, folder, page_slug, filename, page_title, page_description in articles:
    folder_path = os.path.join(root, folder)
    keywords = f"{page_title}, {category_name}, tutorial, guide, SEO friendly"
    intro_text = f"This {page_title.lower()} provides practical first steps, example workflows, and clear instructions for beginners."
    steps = "\n".join(
        f'        <li>{step}</li>' for step in [
            "Open the tool and set up your first project or document.",
            "Use templates and built-in features for faster results.",
            "Follow examples for real use cases and common tasks.",
        ]
    )
    best_practices = "\n".join(
        f'        <li>{practice}</li>' for practice in [
            "Save your work frequently and use version history.",
            "Use keyboard shortcuts to speed up common actions.",
            "Keep content focused on clear goals and user needs.",
        ]
    )
    conclusion = f"After completing this guide, you can use {category_name} with more confidence and apply the most useful features to your daily work."
    html = article_template.format(
        page_title=page_title,
        page_description=page_description,
        keywords=keywords,
        folder=folder,
        filename=filename,
        nav_html=nav_html,
        intro_text=intro_text,
        steps=steps,
        best_practices=best_practices,
        conclusion=conclusion,
        category_name=category_name,
    )
    with open(os.path.join(folder_path, filename), "w", encoding="utf-8") as f:
        f.write(html)

with open(os.path.join(root, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("Pages created")
