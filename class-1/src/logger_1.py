import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    filename="my_logging.log"
)

logger = logging.getLogger(__name__)

logger.info("this is my info logging")
logger.warning("this is my warning logging")
logger.error("this is my error logging")
logger.debug("this is the debug logging")
