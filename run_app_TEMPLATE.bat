@echo off
REM === Screenshot Saver Launcher ===
REM Make sure Python and pip are in your PATH

echo Starting Streamlit app...
cd /d "%~dp0"

REM Install dependencies if needed
pip install --quiet streamlit pillow

REM Launch the app
streamlit run app.py

pause
