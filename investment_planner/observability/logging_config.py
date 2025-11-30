import logging
import os

# Log directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "investment_planner.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# Create logger
logger = logging.getLogger("investment_planner")
logger.setLevel(logging.DEBUG)

logger.debug("Logger initialized successfully.")
