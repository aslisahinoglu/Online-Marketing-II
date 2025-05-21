@echo off
cd /d "%~dp0"
call env\Scripts\activate.bat
where streamlit
streamlit run main.py
pause