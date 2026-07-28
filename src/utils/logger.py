import logging
from pathlib import Path


class PipelineLogger:


    @staticmethod
    def get_logger():

        log_dir = Path("logs")

        log_dir.mkdir(

            parents=True,

            exist_ok=True

        )

        logger = logging.getLogger(

            "market_analysis"

        )

        logger.setLevel(

            logging.INFO

        )

        if not logger.handlers:

            formatter = logging.Formatter(

                "%(asctime)s | %(levelname)s | %(message)s"

            )

            file_handler = logging.FileHandler(

                log_dir / "pipeline.log"

            )

            file_handler.setFormatter(

                formatter

            )

            logger.addHandler(

                file_handler

            )

        return logger