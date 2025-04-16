# A program that iterates through the .txt-files in a folder, open the file and exchanges all commas to tabulations.
# Put logs from subjective tests in ./logs folder, then execute this program by running python logconverter.py in the terminal. Logs will now be tabulated and will be easier to enter into spreadsheet.
import os

pathToUnprocessedLogs = "./logs"
pathToConvertedLogs = "./convertedlogs"
fileEnding = ".txt"

os.makedirs(pathToConvertedLogs, exist_ok=True)
alltexts = ""

for filename in os.listdir(pathToUnprocessedLogs):
    if filename.endswith(fileEnding):
        with open(os.path.join(pathToUnprocessedLogs, filename), "r") as f:
            text = f.read()
            text = "\n" + f"User: {filename[0]}, Subjective test: {filename[0:2]}"  + "\n" + text
            text=text.replace(",", "\t")
            alltexts += text

with open(os.path.join(pathToConvertedLogs, "converted_logs.txt"), "w") as f:
    f.write(alltexts)