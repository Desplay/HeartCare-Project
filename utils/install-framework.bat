py -m pip install Django django-debug-toolbar 
if not %errorLevel%==0 (
    python -m pip install Django django-debug-toolbar
)
if not %errorLevel%==0 (
    pip install Django django-debug-toolbar
)