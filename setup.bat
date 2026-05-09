@echo off
REM Flask Portfolio Setup Script

echo ============================================
echo   Flask Professional Portfolio Setup
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    exit /b 1
)

echo [1/3] Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo [2/3] Installing dependencies...
pip install -r requirements.txt

echo [3/3] Project setup complete!
echo.
echo ============================================
echo   IMPORTANT: Add Your Profile Photo
echo ============================================
echo.
echo Before running the app, please:
echo 1. Find your profile photo (JPG or PNG)
echo 2. Place it in the folder: static\images\
echo 3. Name it: profile.jpg
echo.
echo ============================================
echo   To Run the Application
echo ============================================
echo.
echo 1. Activate the virtual environment:
echo    venv\Scripts\activate.bat
echo.
echo 2. Run the Flask app:
echo    python app.py
echo.
echo 3. Open your browser and go to:
echo    http://localhost:5000
echo.
echo ============================================
