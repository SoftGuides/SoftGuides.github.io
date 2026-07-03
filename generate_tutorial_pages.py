import os
from pathlib import Path

root = Path('.')

pages = {
    'AI-Software/copilot-guide.html': {
        'title': 'Microsoft Copilot Tutorial | Use Copilot for Productivity and Automation',
        'description': 'Learn how to use Microsoft Copilot for productivity, Office workflows, and Windows automation with practical examples.',
        'keywords': 'Microsoft Copilot tutorial, Copilot guide, AI assistant, productivity, Office automation',
        'sections': [
            ('What is Microsoft Copilot?', 'Microsoft Copilot is an AI assistant integrated across Windows and Office apps. It helps you generate content, automate repetitive tasks, summarize information, and speed up software workflows.'),
            ('Getting Started with Copilot', 'Open Copilot in Windows or Office and allow it to access your current app context. Start with simple prompts like "Draft an email reply" or "Create a presentation outline."'),
            ('Copilot in Office Apps', 'In Word, Copilot can rewrite text, generate summaries, and create documents from prompts. In Excel, it can analyze data, build formulas, and compare values. In PowerPoint, Copilot can design slides, suggest layouts, and write speaker notes.'),
            ('Best Copilot Prompts', 'Use clear and specific prompts. Example: "Create a project status email for a marketing campaign with three bullet points and a professional tone." Another example: "Analyze this table and summarize the top three trends."'),
            ('Tips for Better Results', 'Provide context, mention the output format, and review answers carefully. Use follow-up prompts to refine the output and split complex tasks into smaller steps.'),
        ],
    },
    'AI-Software/midjourney-guide.html': {
        'title': 'Midjourney Tutorial | Create Better AI Images with Prompts',
        'description': 'Learn how to use Midjourney for AI image generation, create strong prompts, and craft visual results step-by-step.',
        'keywords': 'Midjourney tutorial, AI image generation, Midjourney prompts, AI art guide',
        'sections': [
            ('How Midjourney Works', 'Midjourney generates images from text prompts using AI. The key is to write clear descriptions, choose a style, and iterate until the image matches your vision.'),
            ('Writing Effective Prompts', 'Start with the main subject, add visual details, choose a style, and include mood or color information. Example: "A futuristic city skyline at dusk, neon lights, cinematic atmosphere, detailed architecture."'),
            ('Using Parameters', 'Add Midjourney parameters like --v for version, --ar for aspect ratio, and --q for quality. Example: "A fantasy landscape with castles --ar 16:9 --v 5 --q 2."'),
            ('Refinement Workflow', 'Use the U buttons to upscale and V buttons to create variations. If the image is close but not perfect, select a variation and refine the prompt.'),
            ('Practical Use Cases', 'Midjourney is great for concept art, branding, social media visuals, and storyboard ideas. Organize prompts by project and save the best outputs for later use.'),
        ],
    },
    'AI-Software/notebooklm-guide.html': {
        'title': 'NotebookLM Tutorial | Use Google NotebookLM for Research and Notes',
        'description': 'Learn how to use NotebookLM for research, summaries, note organization, and knowledge review with step-by-step tips.',
        'keywords': 'NotebookLM tutorial, Google NotebookLM, research assistant, note summaries',
        'sections': [
            ('What is NotebookLM?', 'NotebookLM is an AI-powered research assistant that helps you summarize notes, answer questions, and work with documents in a conversational way.'),
            ('Uploading Your Notes', 'Add PDFs, documents, or notes into NotebookLM. Use folders and tags to keep the content organized for future reference.'),
            ('Asking Better Questions', 'Ask precise questions like "Summarize the main points from the sales report" or "Compare the three product launch strategies."'),
            ('Using NotebookLM for Study', 'Create study guides, flashcards, and quick summaries. Review the generated answers and add your own notes to improve retention.'),
            ('Tips for Productivity', 'Keep your notebooks focused by subject, update documents regularly, and use NotebookLM to generate outlines before writing reports or presentations.'),
        ],
    },
    'Microsoft-Office/excel-guide.html': {
        'title': 'Excel Tutorial | Formulas, PivotTables, and Data Analysis',
        'description': 'Learn Excel formulas, PivotTables, charts, and data analysis techniques to build useful spreadsheets and reports.',
        'keywords': 'Excel tutorial, Excel formulas, PivotTables, data analysis, Excel charts',
        'sections': [
            ('Excel Basics', 'Excel is a spreadsheet app for organizing data, calculating values, and building charts. Start by entering labels and numbers in rows and columns.'),
            ('Essential Formulas', 'Use SUM to add values, AVERAGE to find the mean, and IF to build conditional logic. Example: "=IF(B2>100, \"Above target\", \"Below target\")".'),
            ('Working with Tables', 'Convert ranges into tables to simplify filtering, sorting, and formatting. Use the Table Design tab to add headers and totals.'),
            ('PivotTables for Analysis', 'Create a PivotTable to summarize large datasets. Drag fields into Rows, Columns, Values, and Filters to explore different views.'),
            ('Charts and Visualization', 'Insert column, line, or pie charts to show trends. Format chart elements, add axis titles, and use data labels for clarity.'),
        ],
    },
    'Google-Workspace/google-sheets-guide.html': {
        'title': 'Google Sheets Tutorial | Spreadsheets, Functions, and Automation',
        'description': 'Learn Google Sheets for spreadsheet organization, formulas, conditional formatting, and automation with Sheets tools.',
        'keywords': 'Google Sheets tutorial, Sheets functions, spreadsheet automation, conditional formatting',
        'sections': [
            ('Getting Started in Google Sheets', 'Open Google Sheets and create a new spreadsheet. Add headers, format data, and use templates for budgets or project plans.'),
            ('Useful Functions', 'Use SUM, COUNTIF, VLOOKUP, and ARRAYFORMULA for smarter data calculations. Example: "=VLOOKUP(A2, Sheet2!A:B, 2, FALSE)".'),
            ('Formatting and Layout', 'Apply alternating row colors, freeze headers, and use number formatting. This makes the sheet easier to read and more professional.'),
            ('Collaborating with Others', 'Share the sheet with colleagues, set permissions, and use comments to discuss changes. Version history helps you restore previous versions.'),
            ('Automation with Macros and Apps Script', 'Record macros for repetitive tasks or use Apps Script to automate custom workflows. Start with simple scripts like formatting or data entry.'),
        ],
    },
    'Design-Tools/canva-guide.html': {
        'title': 'Canva Tutorial | Create Social Media Designs and Graphics',
        'description': 'Learn Canva design basics, templates, and best practices to create social media posts, presentations, and marketing graphics.',
        'keywords': 'Canva tutorial, Canva design, social media graphics, Canva templates',
        'sections': [
            ('Why Use Canva?', 'Canva is a design tool that makes graphic creation easy. Use templates, drag-and-drop elements, and simple text editing for fast results.'),
            ('Starting a New Design', 'Choose a design type, such as Instagram post, presentation, or flyer. Pick a template or start from scratch with a blank canvas.'),
            ('Working with Elements', 'Add text, photos, icons, and shapes. Adjust colors, fonts, and spacing to match your brand or style.'),
            ('Design Tips', 'Keep layouts balanced, use readable fonts, and apply consistent color palettes. Use grids and alignment tools for cleaner designs.'),
            ('Exporting and Sharing', 'Download designs in PNG, JPG, or PDF format. Share directly with team members or publish designs to social media.'),
        ],
    },
    'Video-Editing/capcut-guide.html': {
        'title': 'CapCut Tutorial | Video Editing for Beginners',
        'description': 'Learn CapCut editing basics, timeline workflows, effects, and export settings for mobile video creation.',
        'keywords': 'CapCut tutorial, video editing, CapCut tips, mobile video editing',
        'sections': [
            ('Getting Started with CapCut', 'Open CapCut and create a new project. Import your clips, photos, and audio tracks into the timeline.'),
            ('Basic Editing Tools', 'Trim clips, split footage, and adjust speed. Use the timeline to arrange media and preview the sequence in real time.'),
            ('Add Text and Effects', 'Insert text overlays, transitions, and visual effects. Customize fonts, animation, and timing for better storytelling.'),
            ('Sound and Music', 'Add background music and sound effects. Adjust volume, fade in/fade out, and sync audio to your clips.'),
            ('Export Settings', 'Choose the right resolution and frame rate. Use standard export options like 1080p at 30fps for social media sharing.'),
        ],
    },
    'PDF-Tools/adobe-acrobat-guide.html': {
        'title': 'Adobe Acrobat Tutorial | Edit and Convert PDF Files',
        'description': 'Learn Adobe Acrobat tools for PDF editing, commenting, converting, and protecting files with easy step-by-step instructions.',
        'keywords': 'Adobe Acrobat tutorial, PDF editing, PDF conversion, protect PDF, Adobe Acrobat guide',
        'sections': [
            ('Open and Review PDF Files', 'Open your PDF in Adobe Acrobat. Use the navigation pane, thumbnails, and bookmarks to move through pages quickly.'),
            ('Edit Text and Images', 'Select the Edit PDF tool to change text, move images, or replace graphics. Use formatting options to keep the layout consistent.'),
            ('Add Comments and Annotations', 'Use sticky notes, highlights, and drawing tools to annotate the PDF. This is useful for feedback and revisions.'),
            ('Convert PDFs', 'Export the PDF to Word, Excel, or image formats. You can also create PDFs from documents and web pages.'),
            ('Protect and Share', 'Set passwords, permissions, and redaction. Use the Protect tool to restrict editing, printing, or copying.'),
        ],
    },
    'Web-Blogging/wordpress-guide.html': {
        'title': 'WordPress Tutorial | Build a Blog with SEO and Hosting',
        'description': 'Learn WordPress basics, hosting setup, themes, and SEO tips to build a professional blog and publish content online.',
        'keywords': 'WordPress tutorial, blog setup, hosting, WordPress SEO, Elementor, Rank Math',
        'sections': [
            ('Choose Hosting and Install WordPress', 'Select a hosting provider and use one-click install options. Log in to the WordPress dashboard and complete the setup wizard.'),
            ('Pick a Theme and Customize', 'Choose a theme that fits your blog style. Customize appearance, colors, typography, and layout in the theme customizer.'),
            ('Create Pages and Posts', 'Add essential pages like Home, About, and Contact. Write blog posts with headings, images, and categories for easy navigation.'),
            ('Optimize for SEO', 'Install an SEO plugin such as Rank Math. Set meta titles, descriptions, and use keywords in headings and content.'),
            ('Maintain Your Site', 'Keep plugins and themes updated, back up regularly, and monitor performance with analytics tools.'),
        ],
    },
    'Productivity/notion-guide.html': {
        'title': 'Notion Tutorial | Organize Notes, Projects, and Teams',
        'description': 'Learn Notion for note-taking, databases, task management, and team collaboration with practical templates and workflows.',
        'keywords': 'Notion tutorial, Notion guide, productivity tools, knowledge management, project planning',
        'sections': [
            ('Create a Workspace', 'Sign in to Notion and build your workspace. Create pages for notes, tasks, and projects, then invite team members if needed.'),
            ('Use Templates', 'Start with built-in templates like Meeting Notes, Project Tracker, or Personal Planner. Templates save time and show the best structure.'),
            ('Build Databases', 'Use tables, boards, and calendars for task and project tracking. Add properties like status, due date, and priority.'),
            ('Connect Pages and Content', 'Link pages together using backlinks and @ mentions. Create a dashboard page that points to your most important resources.'),
            ('Best Productivity Tips', 'Keep headings clear, use toggles for details, and review your workspace weekly. Integrate Notion with calendars and tools for more automation.'),
        ],
    },
    'Communication/zoom-guide.html': {
        'title': 'Zoom Tutorial | Meetings, Webinars, and Collaboration',
        'description': 'Learn Zoom meeting setup, scheduling, host controls, screen sharing, and collaboration tips for remote work.',
        'keywords': 'Zoom tutorial, Zoom meetings, Zoom webinar, remote collaboration, video conferencing',
        'sections': [
            ('Set Up Your Zoom Account', 'Create or log in to Zoom. Install the desktop and mobile apps, then confirm your audio and video settings in the Test Meeting.'),
            ('Schedule Meetings', 'Set meeting time, duration, and timezone. Use the calendar integration to add the meeting to Google Calendar or Outlook.'),
            ('Host Controls', 'Manage participants, mute audio, and lock meetings. Use waiting rooms, passcodes, and host controls to keep sessions secure.'),
            ('Screen Sharing and Collaboration', 'Share your screen, a window, or a whiteboard. Use annotation tools to highlight information during the meeting.'),
            ('Webinars and Recordings', 'Use Zoom Webinar mode for large audiences. Record meetings to the cloud or local device and share the recording link afterward.'),
        ],
    },
    'Browser/chrome-guide.html': {
        'title': 'Google Chrome Tutorial | Browser Tips and Extensions',
        'description': 'Learn Google Chrome shortcuts, extension management, privacy settings, and performance tips for faster browsing.',
        'keywords': 'Google Chrome tutorial, browser tips, Chrome extensions, privacy settings, browser performance',
        'sections': [
            ('Chrome Setup and Sync', 'Sign in with your Google account to sync bookmarks, history, and passwords. Customize the New Tab page with shortcuts and backgrounds.'),
            ('Keyboard Shortcuts', 'Use shortcuts like Ctrl+T to open a new tab, Ctrl+Shift+T to reopen closed tabs, and Ctrl+L to jump to the address bar.'),
            ('Extensions and Tools', 'Install useful extensions for productivity, password management, and ad blocking. Manage extensions from chrome://extensions.'),
            ('Privacy and Security', 'Use Incognito mode for private browsing. Clear browsing data and review site permissions for camera, microphone, and location.'),
            ('Speed and Performance', 'Close unused tabs, disable unnecessary extensions, and use Chrome Task Manager to find resource-heavy pages.'),
        ],
    },
    'Operating-Systems/windows11-guide.html': {
        'title': 'Windows 11 Tutorial | Setup, Shortcuts, and Productivity',
        'description': 'Learn Windows 11 features, setup tips, keyboard shortcuts, and productivity workflows for modern PC users.',
        'keywords': 'Windows 11 tutorial, Windows 11 tips, setup guide, productivity shortcuts, system settings',
        'sections': [
            ('Windows 11 Setup', 'Complete the initial setup, sign in with your Microsoft account, and choose privacy settings. Customize the desktop and taskbar to match your workflow.'),
            ('New Start Menu and Taskbar', 'Use the centered Start menu, pinned apps, and search bar. Organize apps and use the taskbar overflow menu for quick access.'),
            ('Keyboard Shortcuts', 'Use Win+D to show the desktop, Win+Tab for Task View, and Win+Left/Right arrows for snapping windows.'),
            ('Virtual Desktops and Multitasking', 'Create Virtual Desktops for work and personal spaces. Use Snap Layouts to arrange windows side by side.'),
            ('Settings and Updates', 'Open Settings for personalization, system updates, and security. Keep Windows updated for performance and feature improvements.'),
        ],
    },
    'Developer-Tools/vscode-guide.html': {
        'title': 'VS Code Tutorial | Editor Setup and Productivity Tips',
        'description': 'Learn VS Code setup, extensions, debugging, and productivity tips for software development and coding workflows.',
        'keywords': 'VS Code tutorial, Visual Studio Code guide, coding editor, extensions, debugging',
        'sections': [
            ('Install and Configure VS Code', 'Download VS Code and install it on your system. Choose a theme, set font preferences, and configure basic editor settings.'),
            ('Essential Extensions', 'Install extensions like Python, Prettier, ESLint, GitLens, and Live Server. These tools improve coding comfort and debugging support.'),
            ('Working with the Terminal', 'Open the integrated terminal with Ctrl+` and run commands from your workspace. Use multiple terminal tabs for parallel tasks.'),
            ('Debugging and Version Control', 'Set breakpoints, inspect variables, and run code directly in VS Code. Use the Source Control panel for Git commits and branch management.'),
            ('Productivity Tips', 'Use multi-cursor editing, search across files, and configure snippets. Customize keyboard shortcuts for faster development.'),
        ],
    },
}

page_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <meta name="keywords" content="{keywords}" />
  <link rel="canonical" href="https://softguides.github.io/{path}" />
  <style>
    body {{ font-family: Arial, sans-serif; margin:0; padding:0; background:#f7f9ff; color:#111; }}
    header, main, footer {{ max-width:980px; margin:0 auto; padding:20px; }}
    header {{ background:#1d3253; color:#fff; }}
    header h1 {{ margin:0; font-size:2rem; }}
    header p {{ margin:12px 0 0; font-size:1rem; color:#c7d6ef; }}
    nav {{ margin-top:18px; }}
    nav a {{ color:#c7d6ef; margin-right:16px; text-decoration:none; display:inline-block; margin-bottom:8px; }}
    section {{ background:#fff; border-radius:14px; border:1px solid #dde3ec; padding:22px; box-shadow:0 6px 24px rgba(10,23,55,.05); margin-top:20px; }}
    section h2 {{ margin-top:0; color:#14243a; }}
    section p {{ color:#404a5b; line-height:1.7; }}
    ul {{ margin:16px 0 20px 20px; }}
    .ad-block {{ margin:28px 0; }}
    a.button {{ display:inline-block; padding:10px 16px; margin-top:10px; background:#1d3253; color:#fff; border-radius:8px; text-decoration:none; }}
  </style>
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9374368296307755" crossorigin="anonymous"></script>
</head>
<body>
  <header>
    <h1>{title}</h1>
    <p>{description}</p>
    <nav>
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
      <a href="../about.html">About</a>
      <a href="../contact.html">Contact</a>
      <a href="../privacy-policy.html">Privacy Policy</a>
    </nav>
  </header>
  <main>
{sections}
    <div class="ad-block">
      <ins class="adsbygoogle"
        style="display:block"
        data-ad-client="ca-pub-9374368296307755"
        data-ad-slot="4652042516"
        data-ad-format="auto"
        data-full-width-responsive="true"></ins>
      <script>(adsbygoogle = window.adsbygoogle || []).push({{}});</script>
    </div>
    <section>
      <h2>Next Steps</h2>
      <p>Use this guide again when you need a quick refresher. Explore related tutorials in the same category to build your skills faster.</p>
      <a class="button" href="../index.html">Back to Category</a>
    </section>
  </main>
  <footer>
    <p>SoftGuides · Detailed tutorial for software users and learners.</p>
  </footer>
</body>
</html>
'''

for path, data in pages.items():
    sections_text = ''
    for title, paragraph in data['sections']:
        sections_text += f'    <section>\n      <h2>{title}</h2>\n      <p>{paragraph}</p>\n    </section>\n'
    content = page_template.format(
        title=data['title'],
        description=data['description'],
        keywords=data['keywords'],
        path=path,
        sections=sections_text,
    )
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding='utf-8')
    print('Created', target)

# Update AI-Software index links
ai_index = root / 'AI-Software' / 'index.html'
if ai_index.exists():
    text = ai_index.read_text(encoding='utf-8')
    new_grid = '''      <div class="grid">
        <div class="card">
          <h2><a href="chatgpt-guide.html">ChatGPT Tutorial</a></h2>
          <p>Learn how to use ChatGPT for prompts, productivity, content creation, and automation.</p>
        </div>
        <div class="card">
          <h2><a href="copilot-guide.html">Microsoft Copilot</a></h2>
          <p>Discover Copilot features for Office apps, Windows, and workflow automation.</p>
        </div>
        <div class="card">
          <h2><a href="midjourney-guide.html">Midjourney Guide</a></h2>
          <p>Create stunning AI images with Midjourney prompts, parameters, and tips.</p>
        </div>
        <div class="card">
          <h2><a href="notebooklm-guide.html">NotebookLM</a></h2>
          <p>Use NotebookLM for research, note summaries, and knowledge management.</p>
        </div>
      </div>'''
    import re
    new_text = re.sub(r'<div class="grid">[\s\S]*?</div>\s*<a class="button"', new_grid + '\n      <a class="button"', text, count=1)
    ai_index.write_text(new_text, encoding='utf-8')
    print('Updated AI-Software index links')
else:
    print('AI-Software index not found')
