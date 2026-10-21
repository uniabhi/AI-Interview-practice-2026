import logging

logging.debug("Database connection शुरू हो रहा है")
logging.info("Server सफलतापूर्वक start हुआ")
logging.warning("API rate limit लगभग पूरी हो गई है")
logging.error("Database connection fail हो गया")
logging.critical("Payment service उपलब्ध नहीं है")

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def divide(a, b):
    logging.info("Division शुरू हो रहा है")

    if b == 0:
        logging.error("0 से divide नहीं कर सकते")
        return None

    result = a / b
    logging.info("Division successful, result=%s", result)
    return result

divide(10, 2)
divide(10, 0)


import logging

logger = logging.getLogger("student_app")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
)

logger.addHandler(file_handler)

logger.info("App started")
logger.warning("Low storage warning")