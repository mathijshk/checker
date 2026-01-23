# Visual Studio Code Setup Guide
# AI Governance Assessment Project

## 🎯 Quick Start in VS Code

### 1. Open het Project

```bash
cd /home/user/checker
code .
```

### 2. Installeer Aanbevolen Extensions

Wanneer je het project opent, krijg je een popup:
- **"Do you want to install the recommended extensions?"**
- Klik op **"Install All"**

Of installeer handmatig via Extensions panel (Ctrl+Shift+X):
- Python
- Pylance
- Python Debugger
- Jinja
- HTML CSS Support
- Prettier

### 3. Setup Python Virtual Environment

**Optie A: Via VS Code Command Palette**
1. Press `Ctrl+Shift+P`
2. Type: "Python: Create Environment"
3. Select "Venv"
4. Select Python interpreter (3.7+)
5. Check "requirements.txt" om dependencies te installeren

**Optie B: Via Terminal**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# of
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

### 4. Configure Environment Variables

```bash
cp .env.example .env
```

Open `.env` in VS Code en vul je email settings in:
```env
SECRET_KEY=genereer-random-key-hier
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=jouw@gmail.com
MAIL_PASSWORD=jouw-app-password
MAIL_DEFAULT_SENDER=noreply@jouwsite.nl
```

## 🚀 Development Workflow

### Running the App

**Method 1: Debug Mode (Recommended)**
1. Open `app.py`
2. Press `F5` or go to Run & Debug panel (Ctrl+Shift+D)
3. Select "Flask: Run Web App"
4. App starts at http://localhost:5000
5. Set breakpoints by clicking left of line numbers
6. Debug variables, step through code, etc.

**Method 2: Terminal**
```bash
# Activate venv first
source venv/bin/activate

# Run app
python app.py
```

**Method 3: VS Code Task**
1. Press `Ctrl+Shift+P`
2. Type "Tasks: Run Task"
3. Select "Run Flask Web App"

### Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `F5` | Start debugging |
| `Shift+F5` | Stop debugging |
| `Ctrl+Shift+B` | Run build task (starts Flask) |
| `Ctrl+C` | Stop server in terminal |
| `Ctrl+Shift+P` | Command Palette |
| `Ctrl+` ` | Toggle terminal |
| `Ctrl+K Ctrl+O` | Open folder |
| `Ctrl+P` | Quick file open |
| `Ctrl+Shift+F` | Search in files |
| `Ctrl+Shift+H` | Replace in files |
| `Alt+Up/Down` | Move line up/down |
| `Shift+Alt+Up/Down` | Copy line up/down |
| `Ctrl+/` | Toggle comment |

## 📁 Project Structure in VS Code

```
checker/
├── .vscode/                    # VS Code configuration
│   ├── extensions.json        # Recommended extensions
│   ├── launch.json           # Debug configurations
│   ├── settings.json         # Workspace settings
│   ├── tasks.json            # Build/run tasks
│   ├── snippets.code-snippets # Code snippets
│   └── README_VSCODE.md      # This file
│
├── app.py                     # ⭐ Main Flask app
├── requirements.txt           # Dependencies
├── .env                       # Environment vars (don't commit!)
├── .env.example              # Template for .env
│
├── templates/                # HTML templates
│   ├── index.html           # Landing page
│   ├── assessment.html      # Questions
│   ├── results.html         # Results display
│   └── email_results.html   # Email template
│
├── static/                   # Static files
│   └── style.css            # Styling
│
├── src/                     # Original CLI modules
└── tests/                   # Tests
```

## 🔍 Using IntelliSense

### Python IntelliSense
- **Auto-complete**: Type and press `Ctrl+Space`
- **Go to Definition**: `F12` or `Ctrl+Click`
- **Peek Definition**: `Alt+F12`
- **Find References**: `Shift+F12`
- **Rename Symbol**: `F2`
- **Quick Fix**: `Ctrl+.`

### Jinja2 IntelliSense
- HTML auto-complete werkt in `.html` files
- Jinja syntax highlighting automatisch
- Snippets: Type `jfor` voor for-loop, `jif` voor if-statement

### Custom Snippets
Type prefix en druk `Tab`:
- `froute` → Flask route template
- `fapi` → Flask API route template
- `aquestion` → Assessment question template
- `jfor` → Jinja for loop
- `jif` → Jinja if statement

## 🐛 Debugging

### Breakpoints
1. Click left of line number (red dot appears)
2. Start debugging (`F5`)
3. Code pauses at breakpoint
4. Inspect variables in Debug sidebar
5. Step through code:
   - `F10` - Step over
   - `F11` - Step into
   - `Shift+F11` - Step out
   - `F5` - Continue

### Debug Console
- Evaluate expressions during debugging
- Type variable names to inspect
- Run Python code in current context

### Watch Expressions
- Add variables to watch list
- Automatically updated during debugging
- Right-click variable → Add to Watch

## 📝 Editing Tips

### Multi-Cursor Editing
- `Ctrl+Alt+Up/Down` - Add cursor above/below
- `Ctrl+D` - Select next occurrence
- `Alt+Click` - Add cursor at click position
- `Ctrl+Shift+L` - Select all occurrences

### HTML/Jinja Editing
- Emmet abbreviations work
- Type `div.container>div.row>div.col` and press `Tab`
- Auto-close tags
- Color picker for CSS colors
- Live preview available with Live Server extension

### CSS Editing
- IntelliSense for CSS properties
- Color preview
- Auto-complete for class names
- CSS variables support
- Prettier auto-formatting (save to format)

## 🧪 Testing

### Run Tests
**Method 1: Debug Configuration**
1. Open Run & Debug panel
2. Select "Python: Test Web App"
3. Press F5

**Method 2: Terminal**
```bash
python test_webapp.py
```

**Method 3: Task**
1. `Ctrl+Shift+P` → "Tasks: Run Task"
2. Select "Run Tests"

## 🔧 Common Tasks

### Install New Dependency
```bash
# In terminal
source venv/bin/activate
pip install package-name
pip freeze > requirements.txt
```

### Add New Route
1. Open `app.py`
2. Type `froute` and press `Tab`
3. Fill in route details
4. Create corresponding template in `templates/`

### Add New Question
1. Open `app.py`
2. Find `ASSESSMENT_QUESTIONS`
3. Type `aquestion` and press `Tab`
4. Fill in question details

### Modify Styling
1. Open `static/style.css`
2. Edit CSS (auto-complete available)
3. Save (Prettier formats automatically)
4. Refresh browser (no server restart needed)

### Create New Template
1. Create file in `templates/` folder
2. Start with:
```html
<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <!-- Content here -->
</body>
</html>
```

## 🌐 Browser Integration

### Live Reload
Install Live Server extension:
1. Right-click HTML file
2. Select "Open with Live Server"
3. Auto-refreshes on save

**Note**: For Flask templates, you need to run Flask app instead.

### Opening in Browser
```bash
# From terminal while Flask is running
xdg-open http://localhost:5000  # Linux
open http://localhost:5000      # Mac
start http://localhost:5000     # Windows
```

Or just click the URL in terminal while holding `Ctrl`.

## 📊 Git Integration

### Source Control Panel (Ctrl+Shift+G)
- View changes
- Stage files (+ icon)
- Commit (checkmark icon)
- Push/Pull (... menu)
- View history
- Create branches

### Git Commands in Terminal
```bash
git status
git add .
git commit -m "Your message"
git push
```

### GitLens Extension (Optional)
Install for advanced Git features:
- Line blame annotations
- File history
- Compare branches
- Rich commit search

## ⚙️ Workspace Settings

Settings are in `.vscode/settings.json`:

- Python interpreter: Points to venv
- Linting: Flake8 enabled
- IntelliSense: Pylance with type checking
- File associations: `.html` files → Jinja
- Auto-formatting: Enabled for CSS/JS
- Terminal: Auto-activates venv

To modify:
1. `Ctrl+,` to open Settings
2. Search for setting
3. Modify in UI or edit `settings.json`

## 🎨 Customization

### Color Theme
1. `Ctrl+K Ctrl+T`
2. Select theme

Popular themes:
- Dark+ (default)
- One Dark Pro
- Dracula
- Material Theme

### Icons
Install "Material Icon Theme" or "VSCode Icons" extension

### Font
In Settings:
- Search "Font Family"
- Add: "Fira Code", "JetBrains Mono", or "Cascadia Code"
- Enable "Font Ligatures" for fancy symbols

## 🚨 Troubleshooting

### Python Interpreter Not Found
1. `Ctrl+Shift+P`
2. "Python: Select Interpreter"
3. Choose `./venv/bin/python`

### Import Errors
```bash
# Rebuild venv
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Jinja Syntax Not Highlighting
1. Check file associations in settings.json
2. Install "Jinja" extension
3. Reload window (`Ctrl+Shift+P` → "Reload Window")

### Flask Not Starting
1. Check terminal for errors
2. Verify `.env` file exists
3. Check port 5000 not in use:
```bash
lsof -ti:5000 | xargs kill -9  # Kill process on port 5000
```

### IntelliSense Not Working
1. Verify Pylance extension installed
2. Check Python interpreter selected
3. Reload window
4. Check `.vscode/settings.json` exists

## 📚 Useful Extensions

**Essential:**
- Python (Microsoft)
- Pylance (Microsoft)
- Python Debugger (Microsoft)

**Web Development:**
- Jinja (wholroyd)
- HTML CSS Support (ecmel)
- Auto Rename Tag (Jun Han)
- Live Server (Ritwick Dey)
- Prettier (esbenp)

**Git:**
- GitLens (Eric Amodio)

**Productivity:**
- Path Intellisense (Christian Kohler)
- Bracket Pair Colorizer 2
- TODO Highlight (Wayou Liu)
- Better Comments (Aaron Bond)

**Python Specific:**
- Python Docstring Generator (Nils Werner)
- autoDocstring (Nils Werner)

## 💡 Pro Tips

1. **Use Command Palette** (`Ctrl+Shift+P`) for everything
2. **Quick Open Files** (`Ctrl+P`) - type filename
3. **Symbol Search** (`Ctrl+Shift+O`) - navigate functions in file
4. **Workspace Search** (`Ctrl+Shift+F`) - find across all files
5. **Zen Mode** (`Ctrl+K Z`) - distraction-free coding
6. **Split Editor** (`Ctrl+\`) - view multiple files
7. **Terminal Split** (Click + icon in terminal) - multiple terminals
8. **Sticky Scroll** - enable in settings to keep function names visible
9. **Minimap** - shows code overview on right side
10. **Breadcrumbs** - shows file path at top

## 🎯 Next Steps

1. ✅ VS Code setup compleet
2. ▶️ Start Flask app met `F5`
3. 🌐 Open http://localhost:5000
4. 🔧 Begin met customization
5. 🚀 Deploy when ready

---

**Happy Coding! 🎉**

Voor vragen over het project zelf, zie `WEB_README.md` en `QUICK_START.md`.
