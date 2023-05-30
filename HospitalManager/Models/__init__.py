try:
    from doctors import dataRender, addPatientToQueue
except ImportError:
    from .doctors import dataRender, addPatientToQueue