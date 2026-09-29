"""
Manage llama.cpp server.
"""

import subprocess
import time
import requests
from pathlib import Path


class AIServer:

    def __init__(
        self,
        model_path,
        llama_server,
        host="127.0.0.1",
        port=8080
    ):

        self.model = Path(model_path)

        self.binary = Path(llama_server)

        self.host = host

        self.port = port

        self.process = None

    def is_running(self):

        try:

            requests.get(
                f"http://{self.host}:{self.port}/health",
                timeout=2
            )

            return True

        except Exception:

            return False

    def start(self):

        if self.is_running():

            return

        cmd = [
            str(self.binary),
            "-m",
            str(self.model),
            "--host",
            self.host,
            "--port",
            str(self.port)
        ]

        self.process = subprocess.Popen(cmd)

        for _ in range(30):

            if self.is_running():

                return

            time.sleep(1)

        raise RuntimeError(
            "Unable to start llama.cpp server."
        )

    def stop(self):

        if self.process:

            self.process.terminate()

            self.process.wait()
