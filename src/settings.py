import os


def get_port() -> int:
    port = os.environ.get('ACCESS_COUNTER_PORT')
    return port if port else 8080


def get_debug() -> bool:
    debug = os.environ.get('ACCESS_COUNTER_DEBUG')
    return debug if debug else True


def get_log_file_path() -> str:
    log = os.environ.get('ACCESS_COUNTER_LOG_FILE')
    return log if log else '/var/log/access_counter/access_counter_log'


def get_count_file() -> str:
    count = os.environ.get('ACCESS_COUNTER_COUNT_FILE')
    return count if count else '/etc/access_counter/count.txt'
