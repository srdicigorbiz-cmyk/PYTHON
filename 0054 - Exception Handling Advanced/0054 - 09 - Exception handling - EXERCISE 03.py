import sys
def custom_crash_logger(exc_type, exc_value, exc_traceback):
    print(f"CRASH LOG: {exc_type.__name__} -> {exc_value}")

sys.excepthook = custom_crash_logger




# --- TEST SUITE ---
# Triggering a simulation crash manually to test the hook:
raise ZeroDivisionError("Cannot divide by zero.")

# Expected output in the terminal (ONLY this single line, no traceback!):
# CRASH LOG: ZeroDivisionError -> Cannot divide by zero.
# ------------------