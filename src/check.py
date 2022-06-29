import argparse
import pandas as pd

import colorama
import logging.handlers
from colorama import Fore, Style


class Logger:
    Logger = None
    colorama.init()

    def __init__(self, level, name="truc"):
        self.Logger = logging.getLogger(name)
        self.Logger.setLevel(level)
        formatter = logging.Formatter("%(levelname)s - %(message)s")

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.Logger.addHandler(ch)

    def info(self, message):
        self.Logger.info(message)

    def warning(self, message):
        self.Logger.warning(f"{Fore.YELLOW}{message}{Style.RESET_ALL}")

    def error(self, message):
        self.Logger.error(f"{Fore.RED}{message}{Style.RESET_ALL}")
        exit()

    def debug(self, message):
        self.Logger.debug(message)


def open_datafile(datafile):
    try:
        data = pd.read_csv(datafile)
    except pd.errors.EmptyDataError:
        exit("Empty data file.")
    except pd.errors.ParserError:
        raise argparse.ArgumentTypeError(
            "Error parsing file, needs to be a \
            well formated csv."
        )
    except Exception as error:
        exit(f"{error}: File {datafile} corrupted or does not exist.")
    return data


def test_accuracy(dataset1, dataset2, logger):
    score = 0
    for i in range(len(dataset1)):
        if dataset1[i] == dataset2[i]:
            score += 1
        else:
            logger.debug(
                f"Diff line {i + 2}, index = {i}\n'{dataset1[i]}' vs '{dataset2[i]}'")
    logger.info(f"\nAccuracy: {score / len(dataset1):.2f}")


def cli():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("dataset1", type=open_datafile,
                        help="First dataset to compare.")
    parser.add_argument("dataset", type=open_datafile,
                        help="Second dataset to compare.")
    parser.add_argument(
        "-l",
        "--level",
        metavar="log-level",
        choices=["ERROR", "WARNING", "INFO", "DEBUG", "NOTSET"],
        default="INFO",
        help="Choices: ERROR, WARNING, INFO, DEBUG. The parameter set by default is INFO.",
    )
    args = parser.parse_args()
    logger = Logger(level=args.level)

    try:
        dataset1 = args.dataset1.loc[:, "Hogwarts House"]
        dataset2 = args.dataset.loc[:, "Hogwarts House"]
        test_accuracy(dataset1, dataset2, logger)
    except Exception as error:
        print("Something went wrong:", error)


if __name__ == "main":
    cli()
