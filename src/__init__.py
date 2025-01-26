"""
This file makes the 'app' directory a package and sets up logging.
"""

import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Create a logger for the module
logger = logging.getLogger(__name__)