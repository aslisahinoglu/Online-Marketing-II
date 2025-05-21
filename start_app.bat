@echo off
cd "%~dp0"
call env\Scripts\activate
streamlit run main.py
pause