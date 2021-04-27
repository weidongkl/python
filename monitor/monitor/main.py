import psutil
import time
import logging

from monitor import mem_utils
from monitor import kill

DEFAULT_SLEEP_TIME = 3
WARN_MEM_PERCENT = 90


def get_process_pid(process_name):
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return proc.pid
    else:
        return None


def kill_dde_file_manage():
    try:
        dde_file_manage_name="dde-file-manager"
        dde_file_manage_pid = get_process_pid(dde_file_manage_name)
        if not dde_file_manage_pid is None:
            kill.kill_process(dde_file_manage_pid)
    except Exception as e:
        logging.error(e)


def main():
    while True:
        if mem_utils.get_mem_percent() > WARN_MEM_PERCENT:
            kill_dde_file_manage()
        time.sleep(DEFAULT_SLEEP_TIME)
