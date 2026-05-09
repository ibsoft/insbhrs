#!/usr/bin/env python3
"""
Flask Portfolio - Setup Helper
This script helps you set up your professional portfolio
"""

import os
import sys
import shutil
from pathlib import Path


def print_header(text):
    """Print a formatted header"""
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60 + "\n")


def check_image():
    """Check if profile image exists"""
    images_dir = Path(__file__).parent / "static" / "images"
    profile_jpg = images_dir / "profile.jpg"
    profile_png = images_dir / "profile.png"

    if profile_jpg.exists():
        print("✅ Profile image found: profile.jpg")
        return True
    elif profile_png.exists():
        print("✅ Profile image found: profile.png")
        return True
    else:
        print("❌ Profile image NOT found")
        print(f"\n   Expected location: {images_dir}")
        print("\n   Solution:")
        print("   1. Save your profile photo to that folder")
        print("   2. Name it 'profile.jpg' or 'profile.png'")
        print("   3. The photo will be displayed as a 150x150px circle")
        return False


def check_python_version():
    """Check Python version"""
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major >= 3 and version.minor >= 7:
        print("✅ Python version is compatible")
        return True
    else:
        print("❌ Python 3.7+ is required")
        return False


def check_flask():
    """Check if Flask is installed"""
    try:
        import flask
        print(f"✅ Flask is installed (version {flask.__version__})")
        return True
    except ImportError:
        print("❌ Flask is not installed")
        print("\n   Run: pip install -r requirements.txt")
        return False


def print_next_steps():
    """Print next steps"""
    print_header("NEXT STEPS")
    print("""
1. ADD YOUR PROFILE PHOTO:
   - Save your photo to: static/images/profile.jpg
   - Recommended: 500x500 pixels or larger
   
2. CUSTOMIZE YOUR CONTENT:
   - Edit app.py to update your information
   - Modify your skills, experience, and about section
   
3. RUN THE APPLICATION:
   - Activate virtual environment: venv\\Scripts\\activate.bat
   - Run: python app.py
   - Visit: http://localhost:5000
   
4. CUSTOMIZE THE APPEARANCE:
   - Edit static/css/style.css for styling
   - Edit templates/index.html for HTML structure
   - Modify the color variables at the top of style.css

5. DEPLOYMENT:
   - Read QUICKSTART.md for deployment options
   - Options: Heroku, PythonAnywhere, AWS, Azure, etc.
    """)


def main():
    """Main setup function"""
    print("\n")
    print_header("PROFESSIONAL FLASK PORTFOLIO - SETUP CHECK")

    print("Checking your setup...\n")

    # Check Python
    print("1. Checking Python version...")
    python_ok = check_python_version()

    # Check Flask
    print("\n2. Checking Flask installation...")
    flask_ok = check_flask()

    # Check image
    print("\n3. Checking profile image...")
    image_ok = check_image()

    # Summary
    print_header("SETUP SUMMARY")

    checks = {
        "Python Version": python_ok,
        "Flask Installed": flask_ok,
        "Profile Image": image_ok,
    }

    for check, status in checks.items():
        symbol = "✅" if status else "❌"
        print(f"{symbol} {check}")

    # Print next steps
    print_next_steps()

    if not all(checks.values()):
        print("\n⚠️  Please address the issues above before running the app\n")
        if not flask_ok:
            print("Run: pip install -r requirements.txt\n")
        sys.exit(1)
    else:
        print("\n✅ Setup looks good! You can now run: python app.py\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
