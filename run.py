import os
import sys
import subprocess

if __name__ == "__main__":
    """
    Runs the docker container or rebuilds the image based on arguments

    Args:
        -b or -B: builds the Docker image
    """
    if len(sys.argv) == 1:
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
    
    elif (len(sys.argv) == 1 and (sys.argv[1] == "-b" or sys.argv[1] == "-B")):
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

    else:
        print(f"[WARN] Unknown argument")