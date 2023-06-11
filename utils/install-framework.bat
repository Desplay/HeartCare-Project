py -m pip install Django django-debug-toolbar channels daphne
if not %errorLevel%==0 (
    python -m pip install Django django-debug-toolbar
)
if not %errorLevel%==0 (
    pip install Django django-debug-toolbar
)
if %errorLevel%==0 (
    echo "Django and another framework installed"
) else (
    echo "Django and another framework not installed, Try manual install, please read README.md"
)
pause