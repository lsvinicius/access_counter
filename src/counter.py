from src import settings, logger


def get_saved_count() -> int:
    count = 0
    try:
        with open(settings.get_count_file(), 'r') as f:
            count = int(f.readline())
    except Exception as ex:
        logger.logger.error('something went wrong {}\nstarting count = 0'.format(ex))
        pass
    finally:
        return count


def save_count(count: int):
    try:
        with open(settings.get_count_file(), 'w') as f:
            return f.write(str(count))
    except Exception as ex:
        logger.logger.error('{}\ncould not save count = {}'.format(ex, count))
        pass
