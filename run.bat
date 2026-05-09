@echo off
REM Professional Flask Portfolio - Run Application

echo.
echo ============================================
echo   Running Professional Flask Portfolio
echo ============================================
echo.

REM Check if virtual environment exists
if not exist venv (
    echo ERROR: Virtual environment not found!
    echo Please run install.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo Virtual environment activated!
echo.

REM Check if Flask is installed
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo ERROR: Flask is not installed
    echo Run: pip install -r requirements.txt
    pause
    exit /b 1
)

echo Starting Flask application...
echo.
echo ==========================================
echo   Server is running!
echo.
echo   Open your browser and go to:
echo   http://localhost:5000
echo.
echo   Press Ctrl+C to stop the server
echo ==========================================
echo.

python app.py
