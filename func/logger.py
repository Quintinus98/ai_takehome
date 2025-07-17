#!/usr/bin/python
import logging

def initialize_logger():
    """Initialize the logger for the enrichment pipeline."""
    logger = logging.getLogger("Logger")

    if logger.handlers:
        logger.setLevel(logging.INFO)
        return logger

    # create console handler and set level to info
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s : [%(levelname)s] %(message)s')
    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)

    return logger