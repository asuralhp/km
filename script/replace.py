from config import *
from func.csv_report import read_csv_to_listOfDict

listOfMatch = read_csv_to_listOfDict(path_csv_out)
print(listOfMatch)