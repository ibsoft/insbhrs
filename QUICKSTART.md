# Quick Start Guide - Professional Flask Portfolio

## 🚀 Getting Started in 3 Steps

### Step 1: Prepare Your Profile Photo

**Important:** Before running the application, save your profile photo in the correct location.

**Location:** `static/images/profile.jpg`

**How to do it:**
1. You have a profile photo in your attachments
2. Save it to the folder: `c:\Users\ioannisb\Documents\Python-Development\insbhrs\static\images\`
3. Name it exactly: `profile.jpg`
4. If it's PNG format, you can use `profile.png` - just keep the name lowercase

**Tips for your photo:**
- Use a professional headshot
- Recommended size: 500x500 pixels or larger
- The photo will be displayed as a 150x150px circle
- Make sure the image is clear and well-lit

### Step 2: Install and Run the Application

**Option A: Using the Setup Script (Recommended for Windows)**

1. Open Command Prompt in the project folder
2. Double-click `setup.bat`
3. Follow the prompts
4. Run: `python app.py`

**Option B: Manual Setup**

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
venv\Scripts\activate.bat

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
```

### Step 3: View Your Portfolio

- Open your web browser
- Go to: `http://localhost:5000`
- Press `Ctrl+C` in the terminal to stop the server

---

## 📝 Customizing Your Content

### Edit Your Information

Open `app.py` and find the `profile_data` dictionary. Modify these sections:

**Your Name:**
```python
'name': 'Your Name Here',
```

**Your Title:**
```python
'title': 'Your Title Here - Your Company',
```

**Your About Section:**
Replace the current "About" text with your own content. Keep the formatting with `\n` for paragraphs.

**Your Experience:**
Add or modify job entries in the `experience` list:
```python
{
    'title': 'Your Job Title',
    'company': 'Company Name',
    'duration': 'Start - End',
    'location': 'Location',
    'icon': 'fas fa-briefcase',  # Font Awesome icon
    'description': 'Job description...'
}
```

**Your Skills:**
Add skills to the `skills` list:
```python
'skills': [
    'Your Skill 1',
    'Your Skill 2',
    'Your Skill 3',
    # ... more skills
]
```

---

## 🎨 Customizing the Appearance

### Change the Color Theme

Edit `static/css/style.css` and modify these variables (around line 1):

```css
:root {
    --dark-green: #0d2e1f;        /* Darkest background */
    --medium-green: #1a4d2e;      /* Medium background */
    --light-green: #2d6a4f;       /* Lighter sections */
    --accent-green: #40916c;      /* Accent color */
    --bright-green: #52b788;      /* Bright highlights */
    --neon-green: #74c69d;        /* Neon bright color */
    --terminal-text: #a8dadc;     /* Text color */
}
```

Example to change to a blue theme:
```css
--dark-green: #0d1b2e;
--bright-green: #1e90ff;
--neon-green: #00bfff;
```

### Update Footer Contact Links

In `templates/index.html`, scroll to the footer section and update:

```html
<a href="mailto:your-email@example.com">
    <i class="fas fa-envelope"></i> Email
</a>
<a href="https://linkedin.com/in/yourprofile" target="_blank">
    <i class="fab fa-linkedin"></i> LinkedIn
</a>
<a href="https://github.com/yourprofile" target="_blank">
    <i class="fab fa-github"></i> GitHub
</a>
```

---

## 🔧 Troubleshooting

**Problem:** "profile.jpg not found" error
- **Solution:** Make sure the image is saved at: `static/images/profile.jpg`

**Problem:** Flask command not recognized
- **Solution:** Make sure you've activated the virtual environment: `venv\Scripts\activate.bat`

**Problem:** "Port 5000 is already in use"
- **Solution:** Change the port in `app.py`:
  ```python
  if __name__ == '__main__':
      app.run(debug=True, port=5001)  # Use 5001 instead
  ```

**Problem:** Page looks plain without styling
- **Solution:** Hard refresh your browser: `Ctrl+Shift+R` or `Ctrl+Shift+Delete` and clear cache

---

## 📱 Testing on Mobile

After running the app, test on your phone:

1. Find your computer's IP address (Windows Command Prompt):
   ```
   ipconfig
   ```
   Look for "IPv4 Address" (something like 192.168.x.x)

2. On your phone, visit: `http://192.168.x.x:5000`

3. The page should be fully responsive on mobile devices

---

## 🚀 Deployment Options

### Deploy to Heroku

1. Create a `Procfile`:
   ```
   web: gunicorn app:app
   ```

2. Add to `requirements.txt`:
   ```
   gunicorn==20.1.0
   ```

3. Push to Heroku using their CLI

### Deploy to PythonAnywhere

1. Create account at pythonywhere.com
2. Upload your files
3. Configure in their web app settings
4. Your site will be live!

### Deploy to AWS/Azure/Google Cloud

Each has their own Flask deployment guides. Generally:
1. Create a virtual machine or container
2. Install Python and dependencies
3. Run the Flask app with a production server

---

## 📚 Font Awesome Icons

The portfolio uses Font Awesome icons. Common ones used:

- `fas fa-user-circle` - User profile
- `fas fa-briefcase` - Work/experience
- `fas fa-star` - Skills
- `fas fa-shield-alt` - Security
- `fas fa-server` - Server
- `fas fa-network-wired` - Network
- `fas fa-cogs` - Settings/operations
- `fas fa-calendar` - Calendar
- `fas fa-map-marker-alt` - Location
- `fas fa-envelope` - Email
- `fab fa-linkedin` - LinkedIn
- `fab fa-github` - GitHub

View all at: https://fontawesome.com/icons

---

## ❓ Need More Help?

1. Check the README.md for more details
2. Review the code comments in app.py and templates/index.html
3. The styling is in static/css/style.css with detailed comments

---

**Your professional portfolio is ready to showcase your expertise!** 🎯
