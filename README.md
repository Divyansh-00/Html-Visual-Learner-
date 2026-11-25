# HTML Visual Learning Studio 🎨💻

An interactive, visual educational web application built with **Django** to help students master HTML and CSS through hands-on visual demonstrations, real-time code sandboxes, and guided practice challenges.

---

## 🌟 Key Features

### 1. Interactive Visualizers
- **CSS Box Model:** Real-time visual manipulation of Margin, Border, Padding, and Content dimensions with live CSS code sync.
- **Flexbox Playground:** Interactive controls for `flex-direction`, `justify-content`, `align-items`, `flex-wrap`, and `gap`.
- **CSS Grid Visualizer:** Dynamic grid layout generator with customizable columns, rows, and gaps.
- **CSS Positioning:** Demonstrations of `static`, `relative`, `absolute`, `fixed`, and `sticky` positioning behaviors.
- **CSS Properties Studio:** Live controls for colors, typography, borders, shadows, and spacing.
- **HTML Elements Reference:** Interactive showcase of standard HTML5 elements with syntax, descriptions, and examples.

### 2. Code Playground
- Split-screen live HTML & CSS editor powered by **CodeMirror 6**.
- Sandboxed `<iframe>` rendering with instant live preview.
- Multi-device preview toggle (Desktop, Tablet, Mobile).
- Light and Dark editor themes.
- Save and reload custom playground projects.

### 3. Guided Practice & Challenges
- Interactive coding challenges with automated CSS answer evaluation.
- Instant feedback detailing which required CSS properties match or are missing.
- Safe client-side fallback evaluation.

### 4. Student Dashboard & Authentication
- Full user registration, login, and logout powered by Django's built-in authentication system.
- Per-student learning progress tracking and completion stats.
- Django Admin panel configured to manage lessons, topics, and exercises dynamically.

---

## 🛠️ Technology Stack

- **Backend:** Python, Django 6.x
- **Database:** SQLite (default for development)
- **Frontend:** Vanilla JavaScript, HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Code Editor:** CodeMirror 6 (loaded via CDN)
- **Architecture:** Modular Django app structure (`accounts`, `learning`, `visualizer`, `practice`)

---

## 🚀 Quick Start Guide

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/html-visual-learning-studio.git
cd html-visual-learning-studio
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply database migrations
```bash
python manage.py migrate
```

### 5. Seed initial lessons and practice exercises
```bash
python manage.py seed_data
```

### 6. (Optional) Create an Admin superuser
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Open your browser and navigate to **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.

---

## 📁 Project Structure

```
html_visual_studio/
├── config/              # Root Django configuration & routing
├── accounts/            # User authentication (Login, Register, Logout)
├── learning/            # Lessons, topics, and student progress tracking
├── visualizer/          # Interactive CSS & HTML visualizer tools
├── practice/            # Code playground, exercises, and answer validation
├── templates/           # Reusable HTML templates & page layouts
├── static/              # Custom CSS styles and design system
├── requirements.txt     # Python project dependencies
├── manage.py            # Django management script
└── README.md            # Project documentation
```

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
