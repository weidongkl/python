import os
import signal


def kill_process(pid):
    os.kill(int(pid), signal.SIGKILL)
