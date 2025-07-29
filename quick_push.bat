@echo off
REM Go to project folder
cd /d "Y:\documents\Batch Classify"

REM Add all changes
git add .

REM Commit with timestamp
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set datetime=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2% %datetime:~8,2%:%datetime:~10,2%
git commit -m "Auto commit on %datetime%"

REM Push to GitHub
git push origin main

echo.
echo ✅ Push completed. Press any key to close...
pause >nul
