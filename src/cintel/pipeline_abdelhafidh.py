"""
pipeline_abdelhafidh.py - Project script (modified version).

Author: Abdelhafidh Mahouel
Date: 2026-03-09

Purpose:
  Confirm the project environment is set up correctly.
  Run this script to see log messages in the terminal.
  This version adds extra logging to improve observability.

Run as a Module:
  uv run python -m cintel.pipeline_abdelhafidh
"""

# === DECLARE IMPORTS ===

import logging
from pathlib import Path

from datafun_toolkit.logger import get_logger, log_header, log_path

# === CONFIGURE LOGGER ===

LOG: logging.Logger = get_logger("P1", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS FOR FOLDER PATHS (directories) ===

ROOT_DIR: Path = Path.cwd()
DOCS_DIR: Path = ROOT_DIR / "docs"
ARTIFACTS_DIR: Path = ROOT_DIR / "artifacts"

# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the pipeline with extra logging."""
    log_header(LOG, "CINTEL")

    LOG.info("========================")
    LOG.info("START main()")
    LOG.info("========================")

    log_path(LOG, "ROOT_DIR", ROOT_DIR)
    log_path(LOG, "DOCS_DIR", DOCS_DIR)
    log_path(LOG, "ARTIFACTS_DIR", ARTIFACTS_DIR)

    LOG.info(f"DOCS_DIR exists: {DOCS_DIR.exists()}")
    LOG.info(f"ARTIFACTS_DIR exists: {ARTIFACTS_DIR.exists()}")

    LOG.info("========================")
    LOG.info("Modified pipeline executed successfully!")
    LOG.info("========================")
    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
