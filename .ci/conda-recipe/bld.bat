xcopy /e "%RECIPE_DIR%\.." "%SRC_DIR%"
rem "%PYTHON%" setup.py install --single-version-externally-managed --record record.txt
"%PYTHON%" setup.py install --record record.txt
if errorlevel 1 exit 1