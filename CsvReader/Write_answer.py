import csv,os
from pathlib import Path

def write_answer(file_name,value):
    data_folder = "Tests/Data/" + file_name
    relative_file_path = Path(data_folder)
    absolute_file_path = relative_file_path.absolute()

    writeFile = open(absolute_file_path, 'w')
    writer = csv.writer(writeFile)
    writer.writerow([value])
    writeFile.close()

