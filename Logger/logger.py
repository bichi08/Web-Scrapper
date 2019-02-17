def set_logger():
    import logging

    from datetime import datetime

    curr_time = datetime.now()
    timestamp = "-".join(
        [str(x) for x in [curr_time.year, curr_time.month, curr_time.day, curr_time.hour, curr_time.minute,
                          curr_time.second]])

    log_path = "/home/bichi/Documents/scrapper_log/"
    logging.basicConfig(filename='{}{}.log'.format(log_path, timestamp),
                        format='%(asctime)s %(message)s',
                        filemode='w')

    # Creating an object
    logger = logging.getLogger()

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    return logger
