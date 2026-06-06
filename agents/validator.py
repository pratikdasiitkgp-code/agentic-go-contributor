import subprocess

def run_tests():

    try:
        result = subprocess.run(
            ["go", "test", "./..."],
            capture_output=True,
            text=True
        )

        return result.stdout

    except FileNotFoundError:

        return """
Go compiler not found.

Validation skipped.

Please install Go from:
https://go.dev/dl/
"""