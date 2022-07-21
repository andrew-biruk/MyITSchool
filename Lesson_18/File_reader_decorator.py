import os
import shutil
import logging
from json import dump
from re import findall

logging.basicConfig(
    level=logging.INFO,
    filename="LogInfo/Log_DecorReader.log",
    format="%(asctime)s - %(levelname)s - line %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    filemode="w")


class FileReaderDecorator:
    """decorator to collect information about files opened via given function"""
    storage = dict()

    def __init__(self, func):
        self.func = func

    def __call__(self, file_name: str):
        try:
            # trying to execute function:
            result = self.func(file_name)
            logging.info(f"Successfully executed: {self.func.__name__}({file_name})")

            # handling duplicate files:
            if file_name in self.storage:
                file_name = shutil.copy(file_name, "_duplicate".join(os.path.splitext(file_name)))
                logging.info(f"Copy of duplicate item created: {file_name}")

            # updating data collection:
            self.storage[file_name] = {
                "path": os.path.abspath(file_name),
                "extension": os.path.splitext(file_name)[1],
                "size": str(os.path.getsize(file_name)) + " bytes"}

        except FileNotFoundError as no_file_err:
            logging.error(no_file_err)
            return f"{file_name} file not found"

        # if all is OK, save files info into json and return result:
        else:
            return f"{file_name}: " + f"{result[0]} {result[1]}" if any(result) else f"No results"

    @classmethod
    def write_to_json(cls):
        """saves files_info.json to directory 'FilesInfo'"""
        with open("files_info.json", "w") as json_fw:
            dump(cls.storage, json_fw, indent=4)
        logging.info("Data saved to files_info.json")


@FileReaderDecorator
def extractor(file_name: str) -> tuple[list, list]:
    """:returns: tuple of: number catches, email catches"""

    nums, emails = [], []
    number_match = r"\b\d{3}\b"

    # following regex is illustrative (has no validity verification):
    email_match = r"[\w]+[\.-]?[\w]+@[\w]+[\.-]?[\w]+\.\w{2,}\b"

    with open(file_name) as file:
        for line in file:
            line = line.rstrip()
            nums.extend(findall(number_match, line))
            emails.extend(findall(email_match, line))
    return nums, emails


os.chdir(os.getcwd() + "/FilesInfo")
for f in ["test1.txt",
          "test2.txt",
          "test3.txt",
          "test1.txt"]:
    print(extractor(f), end="\n")

FileReaderDecorator.write_to_json()
