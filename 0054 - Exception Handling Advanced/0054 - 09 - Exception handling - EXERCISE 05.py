import sys
class DatabaseCrashError(Exception):
    pass
class DatabaseSession:
    def __enter__(self):
        print("[Session Started]")
        return self
    def write_data(self, message):
        if message == "CRITICAL_CORE_FAILURE":
            raise ValueError("Core temperature critical!")
        else:
            print(f"Writing: {message}")
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            print("[Session Closed Cleanly]")
        else:
            print("[Session Closed due to Error]")
            raise DatabaseCrashError("Database operation failed unexpectedly.") from exc_value
            



# --- TEST SUITE ---
# Test Case 1: System operates normally within bounds
with DatabaseSession() as db:
    db.write_data("Log info")
# Expected output:
# [Session Started]
# Writing: Log info
# [Session Closed Cleanly]

# Test Case 2: System encounters a standard error and wraps it (The Guru Test)
try:
    with DatabaseSession() as db:
        db.write_data("CRITICAL_CORE_FAILURE")
except DatabaseCrashError as e:
    print(f"Caught Outer Error: {e}")
    print(f"Original Root Cause: {e.__cause__}")
# Expected output:
# [Session Started]
# [Session Closed due to Error]
# Caught Outer Error: Database operation failed unexpectedly.
# Original Root Cause: Core temperature critical!
# ------------------