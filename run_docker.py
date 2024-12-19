import os
import subprocess

if __name__ == "__main__":
    """
    Builds and then runs docker with all of the required commands
    """
    try:
        subprocess.run([
            "docker",
            "build",
            "-t",
            "buttahbot",
            "."
        ])
    except Exception as e:
        print(f"[ERROR] {e}")

    try:
        token = os.environ["BUTTAHBOT_TOKEN"]
        subprocess.run([
            "docker",
            "run",
            "--rm",
            "-e",
            f"BUTTAHBOT_TOKEN={token}",
            "-e",
            "PYTHONUNBUFFERED=1",
            "buttahbot"
        ])
    except Exception as e:
        print(f"[ERROR] {e}")