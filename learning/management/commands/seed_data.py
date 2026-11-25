"""
Management command to seed the database with initial lessons and exercises.
Run with: python manage.py seed_data
"""
from django.core.management.base import BaseCommand
from learning.models import Lesson, Topic
from practice.models import Exercise


LESSONS = [
    # ─── HTML Fundamentals ───────────────────────────────────────────────────
    {
        'title': 'What is HTML?',
        'category': 'html_fundamentals',
        'difficulty': 'beginner',
        'order': 1,
        'description': 'An introduction to HTML — the language that powers the web.',
        'content': '''<h2>What is HTML?</h2>
<p><strong>HTML</strong> (HyperText Markup Language) is the standard language for creating web pages. 
It describes the structure of a webpage using a series of <em>elements</em> represented by <em>tags</em>.</p>
<p>Every website you visit is built with HTML at its core. HTML tells the browser what content to display 
and how to organize it, while CSS controls the appearance and JavaScript adds interactivity.</p>
<div class="info-box">
  <h4>Key Facts</h4>
  <ul>
    <li>HTML stands for <strong>HyperText Markup Language</strong></li>
    <li>It was created by <strong>Tim Berners-Lee</strong> in 1991</li>
    <li>The latest version is <strong>HTML5</strong></li>
    <li>HTML files use the <code>.html</code> or <code>.htm</code> extension</li>
    <li>HTML is <em>not</em> a programming language — it is a markup language</li>
  </ul>
</div>''',
        'code_example': '<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="UTF-8">\n    <title>My First Page</title>\n  </head>\n  <body>\n    <h1>Hello, World!</h1>\n    <p>This is my first HTML page.</p>\n  </body>\n</html>',
        'topics': [
            {'title': 'Definition of HTML', 'description': 'HTML is the standard markup language for creating web pages.'},
            {'title': 'History of HTML', 'description': 'Created by Tim Berners-Lee in 1991, now on version HTML5.'},
        ]
    },
    {
        'title': 'HTML Document Structure',
        'category': 'html_fundamentals',
        'difficulty': 'beginner',
        'order': 2,
        'description': 'Learn the basic skeleton that every HTML document must have.',
        'content': '''<h2>HTML Document Structure</h2>
<p>Every HTML document follows a standard structure. Understanding this structure is essential 
before writing any HTML code.</p>
<h3>The DOCTYPE Declaration</h3>
<p>The <code>&lt;!DOCTYPE html&gt;</code> declaration must be the very first line in an HTML file. 
It tells the browser that this is an HTML5 document.</p>
<h3>The html Element</h3>
<p>The <code>&lt;html&gt;</code> element is the root element that wraps all other content. 
The <code>lang</code> attribute specifies the language of the document.</p>
<h3>The head Section</h3>
<p>The <code>&lt;head&gt;</code> element contains meta-information about the document that is not displayed 
directly on the page, such as the title, character encoding, and links to stylesheets.</p>
<h3>The body Section</h3>
<p>The <code>&lt;body&gt;</code> element contains all the content that is visible to the user — 
text, images, links, and so on.</p>''',
        'code_example': '<!DOCTYPE html>\n<html lang="en">\n<head>\n  <meta charset="UTF-8">\n  <meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <title>Document Title</title>\n</head>\n<body>\n  <!-- Your visible content goes here -->\n  <h1>Page Heading</h1>\n  <p>Page content...</p>\n</body>\n</html>',
        'topics': [
            {'title': 'DOCTYPE', 'description': 'The DOCTYPE declaration tells the browser the document type.'},
            {'title': 'Head vs Body', 'description': 'Head contains metadata; body contains visible content.'},
        ]
    },
    {
        'title': 'HTML Tags and Elements',
        'category': 'html_fundamentals',
        'difficulty': 'beginner',
        'order': 3,
        'description': 'Understand the difference between tags and elements in HTML.',
        'content': '''<h2>HTML Tags and Elements</h2>
<p>HTML uses <strong>tags</strong> to mark up content. Most tags come in pairs: an opening tag and a closing tag.</p>
<h3>Anatomy of an HTML Element</h3>
<p>An HTML element consists of:</p>
<ul>
  <li><strong>Opening tag</strong>: <code>&lt;tagname&gt;</code></li>
  <li><strong>Content</strong>: The text or nested elements inside</li>
  <li><strong>Closing tag</strong>: <code>&lt;/tagname&gt;</code></li>
</ul>
<h3>Self-Closing Tags</h3>
<p>Some elements do not have closing tags because they cannot contain content. These are called <em>void elements</em>:</p>
<ul>
  <li><code>&lt;br&gt;</code> — Line break</li>
  <li><code>&lt;img&gt;</code> — Image</li>
  <li><code>&lt;hr&gt;</code> — Horizontal rule</li>
  <li><code>&lt;input&gt;</code> — Form input</li>
  <li><code>&lt;meta&gt;</code> — Metadata</li>
  <li><code>&lt;link&gt;</code> — External resource link</li>
</ul>
<h3>Nesting Elements</h3>
<p>HTML elements can be nested inside each other. When nesting, always close the innermost element first.</p>''',
        'code_example': '<!-- A complete element -->\n<p>This is a paragraph element.</p>\n\n<!-- Self-closing element -->\n<br>\n<img src="photo.jpg" alt="A photo">\n\n<!-- Nested elements -->\n<ul>\n  <li>First item</li>\n  <li>Second item</li>\n</ul>',
        'topics': [
            {'title': 'Opening and Closing Tags', 'description': 'Most HTML elements have both opening and closing tags.'},
            {'title': 'Void Elements', 'description': 'Some elements like <br>, <img>, and <input> are self-closing.'},
            {'title': 'Nesting', 'description': 'Elements can be nested inside each other.'},
        ]
    },
    {
        'title': 'HTML Attributes',
        'category': 'html_fundamentals',
        'difficulty': 'beginner',
        'order': 4,
        'description': 'Learn how attributes add extra information and behaviour to HTML elements.',
        'content': '''<h2>HTML Attributes</h2>
<p>Attributes provide additional information about HTML elements. They are always placed inside the opening tag 
and usually come in <strong>name="value"</strong> pairs.</p>
<h3>Common Attributes</h3>
<ul>
  <li><code>id</code> — A unique identifier for an element</li>
  <li><code>class</code> — One or more CSS class names</li>
  <li><code>style</code> — Inline CSS styles</li>
  <li><code>href</code> — URL for anchor tags</li>
  <li><code>src</code> — Source URL for images and scripts</li>
  <li><code>alt</code> — Alternative text for images</li>
  <li><code>type</code> — Type attribute for inputs and buttons</li>
  <li><code>placeholder</code> — Hint text for form inputs</li>
</ul>
<h3>Boolean Attributes</h3>
<p>Some attributes are boolean — their presence alone means <em>true</em>. 
For example, <code>disabled</code>, <code>checked</code>, <code>required</code>.</p>''',
        'code_example': '<!-- id and class attributes -->\n<div id="main-content" class="container highlight">\n\n<!-- href attribute -->\n<a href="https://example.com" target="_blank">Visit Example</a>\n\n<!-- src and alt attributes -->\n<img src="image.jpg" alt="Description of image" width="300">\n\n<!-- Boolean attributes -->\n<input type="text" placeholder="Enter name" required>\n<button disabled>Submit</button>',
        'topics': [
            {'title': 'name="value" pairs', 'description': 'Attributes are written as name="value" inside opening tags.'},
            {'title': 'Boolean Attributes', 'description': 'Attributes like disabled and required just need to be present.'},
        ]
    },
    {
        'title': 'Headings and Paragraphs',
        'category': 'html_fundamentals',
        'difficulty': 'beginner',
        'order': 5,
        'description': 'Use heading levels and paragraph elements to structure your text content.',
        'content': '''<h2>Headings and Paragraphs</h2>
<p>Headings and paragraphs are the building blocks of text content on the web.</p>
<h3>Heading Elements</h3>
<p>HTML provides six heading levels: <code>&lt;h1&gt;</code> through <code>&lt;h6&gt;</code>. 
<code>&lt;h1&gt;</code> is the most important and should be used only once per page as the main heading. 
Heading levels define the outline of your document.</p>
<h3>Paragraph Element</h3>
<p>The <code>&lt;p&gt;</code> element defines a paragraph. Browsers automatically add spacing above and below paragraphs.</p>
<h3>Text Formatting</h3>
<ul>
  <li><code>&lt;strong&gt;</code> — Bold, important text</li>
  <li><code>&lt;em&gt;</code> — Italic, emphasised text</li>
  <li><code>&lt;br&gt;</code> — Line break within a paragraph</li>
  <li><code>&lt;hr&gt;</code> — Thematic break (horizontal line)</li>
</ul>''',
        'code_example': '<h1>Main Page Title</h1>\n<h2>Section Heading</h2>\n<h3>Sub-section Heading</h3>\n<h4>Sub-sub-section</h4>\n<h5>Even smaller heading</h5>\n<h6>Smallest heading</h6>\n\n<p>This is a regular paragraph with <strong>bold text</strong> and <em>italic text</em>.</p>\n<p>Another paragraph. Notice the automatic spacing.</p>\n\n<hr>\n\n<p>A paragraph after a horizontal rule.</p>',
        'topics': [
            {'title': 'h1 to h6', 'description': 'Six levels of headings defining document hierarchy.'},
            {'title': 'Paragraphs', 'description': 'The <p> element wraps blocks of text into paragraphs.'},
        ]
    },
    {
        'title': 'Links and Anchors',
        'category': 'html_fundamentals',
        'difficulty': 'beginner',
        'order': 6,
        'description': 'Create hyperlinks that connect pages and resources on the web.',
        'content': '''<h2>Links and Anchors</h2>
<p>Hyperlinks are the foundation of the web. The <code>&lt;a&gt;</code> (anchor) element creates a link 
to another page, file, email address, or location within the same page.</p>
<h3>Key Attributes</h3>
<ul>
  <li><code>href</code> — The URL the link points to</li>
  <li><code>target="_blank"</code> — Opens the link in a new tab</li>
  <li><code>title</code> — Tooltip text shown on hover</li>
  <li><code>download</code> — Downloads the linked file</li>
</ul>
<h3>Link Types</h3>
<ul>
  <li><strong>Absolute URLs</strong>: Full URL including protocol — <code>https://example.com</code></li>
  <li><strong>Relative URLs</strong>: Relative to the current file — <code>../about.html</code></li>
  <li><strong>Anchor links</strong>: Jump to an id on the same page — <code>#section-id</code></li>
  <li><strong>Email links</strong>: Opens email client — <code>mailto:user@example.com</code></li>
</ul>''',
        'code_example': '<!-- External link -->\n<a href="https://www.google.com" target="_blank">Go to Google</a>\n\n<!-- Relative link -->\n<a href="about.html">About Us</a>\n\n<!-- Anchor link (jumps to section) -->\n<a href="#contact">Jump to Contact</a>\n\n<!-- Email link -->\n<a href="mailto:hello@example.com">Send Email</a>\n\n<!-- Target section -->\n<section id="contact">\n  <h2>Contact Us</h2>\n</section>',
        'topics': [
            {'title': 'href Attribute', 'description': 'The href attribute specifies the link destination.'},
            {'title': 'Opening in New Tab', 'description': 'Use target="_blank" to open links in new tabs.'},
        ]
    },
    {
        'title': 'Lists in HTML',
        'category': 'html_fundamentals',
        'difficulty': 'beginner',
        'order': 7,
        'description': 'Create ordered, unordered, and definition lists to organise information.',
        'content': '''<h2>Lists in HTML</h2>
<p>Lists are used to group related items. HTML provides three types of lists.</p>
<h3>Unordered Lists</h3>
<p>The <code>&lt;ul&gt;</code> element creates a bulleted list. Each item is wrapped in <code>&lt;li&gt;</code>.</p>
<h3>Ordered Lists</h3>
<p>The <code>&lt;ol&gt;</code> element creates a numbered list. Use the <code>type</code> attribute to change 
the numbering style (1, A, a, I, i) and <code>start</code> to begin at a different number.</p>
<h3>Definition Lists</h3>
<p>The <code>&lt;dl&gt;</code> element creates a list of terms and descriptions, useful for glossaries.</p>
<h3>Nested Lists</h3>
<p>Lists can be nested inside each other to create hierarchical structures.</p>''',
        'code_example': '<!-- Unordered list -->\n<ul>\n  <li>HTML</li>\n  <li>CSS</li>\n  <li>JavaScript</li>\n</ul>\n\n<!-- Ordered list -->\n<ol>\n  <li>Learn HTML</li>\n  <li>Learn CSS</li>\n  <li>Build projects</li>\n</ol>\n\n<!-- Nested list -->\n<ul>\n  <li>Frontend\n    <ul>\n      <li>HTML</li>\n      <li>CSS</li>\n    </ul>\n  </li>\n  <li>Backend</li>\n</ul>',
        'topics': [
            {'title': 'ul and ol', 'description': 'ul for unordered (bulleted) and ol for ordered (numbered) lists.'},
            {'title': 'li Elements', 'description': 'Each list item is wrapped in an <li> element.'},
        ]
    },
    # ─── CSS Box Model ────────────────────────────────────────────────────────
    {
        'title': 'Understanding the CSS Box Model',
        'category': 'css_box_model',
        'difficulty': 'beginner',
        'order': 1,
        'description': 'Every HTML element is a box. Learn how margin, border, padding and content work together.',
        'content': '''<h2>The CSS Box Model</h2>
<p>In CSS, every element is treated as a rectangular box. The <strong>box model</strong> describes how 
the size of that box is calculated and how the space around it is managed.</p>
<h3>The Four Layers</h3>
<ul>
  <li><strong>Content</strong> — The actual text, image, or other content inside the element</li>
  <li><strong>Padding</strong> — The transparent space between the content and the border</li>
  <li><strong>Border</strong> — A line that surrounds the padding and content</li>
  <li><strong>Margin</strong> — The transparent space outside the border, separating the element from others</li>
</ul>
<h3>Box Sizing</h3>
<p>By default, <code>width</code> and <code>height</code> only apply to the content area. 
Using <code>box-sizing: border-box</code> makes <code>width</code> and <code>height</code> include 
the padding and border, which is usually easier to work with.</p>''',
        'code_example': '.box {\n  /* Content size */\n  width: 200px;\n  height: 100px;\n\n  /* Padding - space inside */\n  padding: 20px;\n\n  /* Border */\n  border: 3px solid #6366f1;\n\n  /* Margin - space outside */\n  margin: 30px;\n\n  /* Include padding/border in size calculation */\n  box-sizing: border-box;\n}',
        'topics': [
            {'title': 'Content Area', 'description': 'The innermost area where your content lives.'},
            {'title': 'Padding', 'description': 'Space between content and border, inherits background colour.'},
            {'title': 'Border', 'description': 'A visible line around the padding and content.'},
            {'title': 'Margin', 'description': 'Transparent space outside the border.'},
        ]
    },
    # ─── Flexbox ──────────────────────────────────────────────────────────────
    {
        'title': 'Introduction to Flexbox',
        'category': 'flexbox',
        'difficulty': 'beginner',
        'order': 1,
        'description': 'Learn CSS Flexbox — the most powerful tool for one-dimensional layout.',
        'content': '''<h2>CSS Flexbox</h2>
<p>Flexbox (Flexible Box Layout) is a CSS layout method designed for arranging items in one dimension — 
either a row or a column. It makes it easy to distribute space and align items.</p>
<h3>Getting Started</h3>
<p>To use Flexbox, apply <code>display: flex</code> to a container element. All direct children 
of that container become <em>flex items</em>.</p>
<h3>Main Axis and Cross Axis</h3>
<p>Flexbox works along two axes:</p>
<ul>
  <li><strong>Main axis</strong>: The primary direction of layout (horizontal by default)</li>
  <li><strong>Cross axis</strong>: Perpendicular to the main axis (vertical by default)</li>
</ul>
<h3>Key Properties</h3>
<ul>
  <li><code>flex-direction</code>: row | column | row-reverse | column-reverse</li>
  <li><code>justify-content</code>: Aligns items along the <em>main axis</em></li>
  <li><code>align-items</code>: Aligns items along the <em>cross axis</em></li>
  <li><code>flex-wrap</code>: Controls whether items wrap to a new line</li>
  <li><code>gap</code>: Spacing between flex items</li>
</ul>''',
        'code_example': '.container {\n  display: flex;\n  flex-direction: row;\n  justify-content: center;\n  align-items: center;\n  gap: 16px;\n  flex-wrap: wrap;\n}\n\n.item {\n  flex: 1;\n  min-width: 100px;\n  padding: 20px;\n  background: #6366f1;\n  color: white;\n  border-radius: 8px;\n}',
        'topics': [
            {'title': 'display: flex', 'description': 'Turns a container into a flex container.'},
            {'title': 'flex-direction', 'description': 'Sets the direction of the main axis.'},
            {'title': 'justify-content', 'description': 'Aligns items on the main axis.'},
            {'title': 'align-items', 'description': 'Aligns items on the cross axis.'},
        ]
    },
    # ─── CSS Grid ─────────────────────────────────────────────────────────────
    {
        'title': 'Introduction to CSS Grid',
        'category': 'css_grid',
        'difficulty': 'intermediate',
        'order': 1,
        'description': 'Master two-dimensional layout with CSS Grid.',
        'content': '''<h2>CSS Grid Layout</h2>
<p>CSS Grid is a two-dimensional layout system that lets you control both rows and columns simultaneously. 
It is perfect for building complex page layouts.</p>
<h3>Setting Up a Grid</h3>
<p>Apply <code>display: grid</code> to a container. Then use <code>grid-template-columns</code> and 
<code>grid-template-rows</code> to define the grid structure.</p>
<h3>Key Properties</h3>
<ul>
  <li><code>grid-template-columns</code>: Defines column tracks</li>
  <li><code>grid-template-rows</code>: Defines row tracks</li>
  <li><code>gap</code> / <code>column-gap</code> / <code>row-gap</code>: Spacing between cells</li>
  <li><code>grid-column</code>: Specifies how many columns an item spans</li>
  <li><code>grid-row</code>: Specifies how many rows an item spans</li>
  <li><code>justify-items</code>: Horizontal alignment of items within cells</li>
  <li><code>align-items</code>: Vertical alignment of items within cells</li>
</ul>
<h3>The fr Unit</h3>
<p>The <code>fr</code> unit represents a fraction of the available space in the grid container. 
<code>grid-template-columns: 1fr 2fr 1fr</code> creates three columns where the middle is twice as wide.</p>''',
        'code_example': '.grid-container {\n  display: grid;\n  grid-template-columns: 1fr 2fr 1fr;\n  grid-template-rows: auto auto;\n  gap: 16px;\n}\n\n/* Span across multiple columns */\n.header {\n  grid-column: 1 / -1; /* spans all columns */\n}\n\n.sidebar {\n  grid-column: 1;\n  grid-row: 2;\n}',
        'topics': [
            {'title': 'display: grid', 'description': 'Creates a grid container.'},
            {'title': 'grid-template-columns', 'description': 'Defines the column structure.'},
            {'title': 'fr unit', 'description': 'A fractional unit of available space.'},
            {'title': 'Spanning', 'description': 'Items can span multiple rows or columns.'},
        ]
    },
    # ─── CSS Positioning ──────────────────────────────────────────────────────
    {
        'title': 'CSS Positioning',
        'category': 'css_positioning',
        'difficulty': 'intermediate',
        'order': 1,
        'description': 'Control exactly where elements appear on the page using CSS positioning.',
        'content': '''<h2>CSS Positioning</h2>
<p>The <code>position</code> property determines how an element is placed in the document and 
how offset properties (<code>top</code>, <code>right</code>, <code>bottom</code>, <code>left</code>) affect it.</p>
<h3>Position Values</h3>
<ul>
  <li><code>static</code> — Default. Element is placed in normal document flow. Offset properties have no effect.</li>
  <li><code>relative</code> — Element stays in normal flow but can be offset <em>relative to its normal position</em>.</li>
  <li><code>absolute</code> — Element is removed from normal flow and positioned <em>relative to its nearest positioned ancestor</em>.</li>
  <li><code>fixed</code> — Element is removed from normal flow and positioned <em>relative to the viewport</em>. It stays in place during scrolling.</li>
  <li><code>sticky</code> — Element acts like <code>relative</code> until it reaches a scroll threshold, then acts like <code>fixed</code>.</li>
</ul>
<h3>The z-index Property</h3>
<p>When elements overlap, <code>z-index</code> controls which element appears on top. 
Higher values appear in front. Only works on positioned elements (not <code>static</code>).</p>''',
        'code_example': '/* Relative positioning */\n.box {\n  position: relative;\n  top: 20px;\n  left: 30px;\n}\n\n/* Absolute positioning */\n.parent {\n  position: relative; /* Creates positioning context */\n}\n.child {\n  position: absolute;\n  top: 0;\n  right: 0;\n}\n\n/* Fixed — stays during scroll */\n.navbar {\n  position: fixed;\n  top: 0;\n  left: 0;\n  width: 100%;\n}',
        'topics': [
            {'title': 'static', 'description': 'Default positioning, element is in normal flow.'},
            {'title': 'relative', 'description': 'Offset from its normal position.'},
            {'title': 'absolute', 'description': 'Positioned relative to nearest positioned ancestor.'},
            {'title': 'fixed', 'description': 'Positioned relative to the viewport.'},
            {'title': 'sticky', 'description': 'Sticks at a scroll offset.'},
        ]
    },
    # ─── CSS Properties ───────────────────────────────────────────────────────
    {
        'title': 'CSS Colors and Backgrounds',
        'category': 'css_properties',
        'difficulty': 'beginner',
        'order': 1,
        'description': 'Explore different ways to apply colors and backgrounds in CSS.',
        'content': '''<h2>CSS Colors and Backgrounds</h2>
<p>CSS provides multiple ways to specify color and control the background of elements.</p>
<h3>Color Formats</h3>
<ul>
  <li><strong>Named colors</strong>: <code>red</code>, <code>blue</code>, <code>coral</code></li>
  <li><strong>Hex</strong>: <code>#6366f1</code>, <code>#fff</code></li>
  <li><strong>RGB</strong>: <code>rgb(99, 102, 241)</code></li>
  <li><strong>RGBA</strong>: <code>rgba(99, 102, 241, 0.5)</code> — with transparency</li>
  <li><strong>HSL</strong>: <code>hsl(239, 84%, 67%)</code></li>
</ul>
<h3>Background Properties</h3>
<ul>
  <li><code>background-color</code>: Sets a solid background color</li>
  <li><code>background-image</code>: Sets a background image or gradient</li>
  <li><code>background-size</code>: cover | contain | auto</li>
  <li><code>background-position</code>: Where the image starts</li>
  <li><code>background-repeat</code>: Whether the image tiles</li>
</ul>''',
        'code_example': '.box {\n  /* Solid color */\n  background-color: #6366f1;\n  color: white;\n\n  /* Linear gradient */\n  background: linear-gradient(135deg, #6366f1, #8b5cf6);\n\n  /* Radial gradient */\n  background: radial-gradient(circle, #6366f1, #1e1b4b);\n\n  /* Background image */\n  background-image: url("pattern.svg");\n  background-size: cover;\n  background-position: center;\n}',
        'topics': [
            {'title': 'Color Formats', 'description': 'Named, hex, RGB, RGBA, and HSL color notations.'},
            {'title': 'Gradients', 'description': 'Linear and radial gradients as backgrounds.'},
        ]
    },
]


EXERCISES = [
    {
        'title': 'Add Padding to a Box',
        'category': 'css',
        'difficulty': 'beginner',
        'order': 1,
        'description': 'Practice adding padding to create space inside an element.',
        'instructions': 'Give the .box element a padding of 20px on all sides. Use the CSS padding property.',
        'starter_html': '<div class="box">Hello, World!</div>',
        'starter_css': '.box {\n  background-color: #6366f1;\n  color: white;\n  /* Add padding here */\n}',
        'expected_properties': {'padding': '20px'},
    },
    {
        'title': 'Center Elements with Flexbox',
        'category': 'flexbox',
        'difficulty': 'beginner',
        'order': 1,
        'description': 'Use Flexbox to center three boxes both horizontally and vertically inside a container.',
        'instructions': 'Make the .container a flex container and center the three boxes both horizontally and vertically.',
        'starter_html': '<div class="container">\n  <div class="box">1</div>\n  <div class="box">2</div>\n  <div class="box">3</div>\n</div>',
        'starter_css': '.container {\n  width: 400px;\n  height: 200px;\n  background: #f1f5f9;\n  /* Add flexbox properties here */\n}\n\n.box {\n  width: 60px;\n  height: 60px;\n  background: #6366f1;\n  color: white;\n  border-radius: 8px;\n}',
        'expected_properties': {'display': 'flex', 'justify-content': 'center', 'align-items': 'center'},
    },
    {
        'title': 'Create a 3-Column Grid',
        'category': 'grid',
        'difficulty': 'intermediate',
        'order': 1,
        'description': 'Build a three-column equal-width grid layout using CSS Grid.',
        'instructions': 'Make the .grid-container display as a CSS grid with 3 equal columns using the fr unit.',
        'starter_html': '<div class="grid-container">\n  <div class="item">Column 1</div>\n  <div class="item">Column 2</div>\n  <div class="item">Column 3</div>\n</div>',
        'starter_css': '.grid-container {\n  /* Add grid properties here */\n  gap: 16px;\n}\n\n.item {\n  background: #6366f1;\n  color: white;\n  padding: 20px;\n  border-radius: 8px;\n  text-align: center;\n}',
        'expected_properties': {'display': 'grid', 'grid-template-columns': '1fr 1fr 1fr'},
    },
    {
        'title': 'Build a Rounded Button',
        'category': 'css',
        'difficulty': 'beginner',
        'order': 2,
        'description': 'Style a button with rounded corners and a violet background.',
        'instructions': 'Style the .btn element with a background-color of #6366f1, border-radius of 8px, and color of white.',
        'starter_html': '<button class="btn">Click Me</button>',
        'starter_css': '.btn {\n  padding: 12px 24px;\n  border: none;\n  font-size: 16px;\n  cursor: pointer;\n  /* Add color, border-radius here */\n}',
        'expected_properties': {'background-color': '#6366f1', 'border-radius': '8px', 'color': 'white'},
    },
    {
        'title': 'Relative vs Absolute Positioning',
        'category': 'css',
        'difficulty': 'intermediate',
        'order': 1,
        'description': 'Position a badge in the top-right corner of a card using absolute positioning.',
        'instructions': 'Make the .card position: relative and the .badge position: absolute with top: 0 and right: 0.',
        'starter_html': '<div class="card">\n  <span class="badge">New</span>\n  <p>Card content here</p>\n</div>',
        'starter_css': '.card {\n  width: 200px;\n  height: 150px;\n  background: white;\n  border: 1px solid #e2e8f0;\n  border-radius: 8px;\n  padding: 16px;\n  /* Add position here */\n}\n\n.badge {\n  background: #6366f1;\n  color: white;\n  padding: 4px 8px;\n  border-radius: 4px;\n  /* Add position, top, right here */\n}',
        'expected_properties': {'position': 'absolute', 'top': '0', 'right': '0'},
    },
    {
        'title': 'Add a Box Shadow',
        'category': 'css',
        'difficulty': 'beginner',
        'order': 3,
        'description': 'Make an element pop with a subtle box shadow.',
        'instructions': 'Add a box-shadow property to the .card element: 0 4px 6px rgba(0,0,0,0.1)',
        'starter_html': '<div class="card">I have a shadow!</div>',
        'starter_css': '.card {\n  background: white;\n  border-radius: 12px;\n  padding: 24px;\n  width: 200px;\n  /* Add box-shadow here */\n}',
        'expected_properties': {'box-shadow': '0 4px 6px rgba(0,0,0,0.1)'},
    },
]


class Command(BaseCommand):
    help = 'Seed the database with initial lessons and exercises'

    def add_arguments(self, parser):
        parser.add_argument('--clear', action='store_true', help='Clear existing data before seeding')

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Lesson.objects.all().delete()
            Exercise.objects.all().delete()

        created_lessons = 0
        for lesson_data in LESSONS:
            topics_data = lesson_data.pop('topics', [])
            lesson, created = Lesson.objects.get_or_create(
                title=lesson_data['title'],
                defaults=lesson_data
            )
            if created:
                created_lessons += 1
                for topic_data in topics_data:
                    Topic.objects.create(lesson=lesson, **topic_data)
            else:
                # Restore topics key for next iteration safety
                lesson_data['topics'] = topics_data

        created_exercises = 0
        for ex_data in EXERCISES:
            _, created = Exercise.objects.get_or_create(
                title=ex_data['title'],
                defaults=ex_data
            )
            if created:
                created_exercises += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Seeded {created_lessons} lessons and {created_exercises} exercises.'
            )
        )
