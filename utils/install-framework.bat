py -m pip install Django django-debug-toolbar 
if not %errorLevel%==0 (
    python -m pip install Django django-debug-toolbar
)
if not %errorLevel%==0 (
    pip install Django django-debug-toolbar
)
if %errorLevel%==0 (
    echo "Django and django-debug-toolbar installed"
) else (
    echo "Django and django-debug-toolbar not installed"
)
pause