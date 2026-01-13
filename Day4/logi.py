import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(levelname)s %(message)s",
                    filename="ap.log",
                    filemode="a"
                    )
logging.debug("Debug message")

logging.info("This is info")

logging.warning("This is a warning")
logging.error("This is the error")
logging.critical("CRITICAL DANGER !!!! ")