import psutil


def get_mem_percent():
    return psutil.virtual_memory()[2]
