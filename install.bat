@echo off
REM Professional Flask Portfolio - Complete Setup

echo.
echo ============================================
echo   Professional Flask Portfolio Setup
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python from https://www.python.org
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [OK] Python is installed
python --version
echo.

REM Create virtual environment
echo [1/4] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists, skipping...
) else (
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)
echo [OK] Virtual environment ready
echo.

REM Activate virtual environment
echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo [OK] Virtual environment activated
echo.

REM Install dependencies
echo [3/4] Installing Python dependencies...
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] All dependencies installed
echo.

REM Run setup check
echo [4/4] Running setup verification...
python setup_check.py
if errorlevel 1 (
    echo.
    echo Setup verification found issues. Please fix them above.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   Setup Complete! Ready to Run
echo ============================================
echo.
echo To start your portfolio:
echo   1. The virtual environment is already active
echo   2. Run: python app.py
echo   3. Visit: http://localhost:5000
echo.
echo To stop the server: Press Ctrl+C
echo.
echo IMPORTANT: Add your profile photo to:
echo   static\images\profile.jpg
echo.
pause
