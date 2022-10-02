from Student_app.models.models import Student
from Student_app import db
import os
import app
import pandas as pd
import config
from config import sql_var
import os
from pathlib import Path

BASE_DIR =Path(__file__).resolve().parent.parent
print('BASE_DIR:',BASE_DIR)
STATIC_DIR=os.path.join(BASE_DIR,'static')
print('STATIC_DIR', STATIC_DIR)


def parseCSV(filePath):
    col_names= ['Name', 'Mobile', 'Address','Education']
    print('column Names:', col_names)
    csvData =pd.read_csv(filePath, names=col_names,header=None)
    print('CSV Data:',csvData)

    for i, row in csvData.iterrows():
        sql="INSERT INTO students(Name , Mobile, Address, Education) VALUES(%s, %s, %s ,%s)"
        print('SQL:', sql)
        value=(row['Name'], row['Mobile'], row['Address'], row['Education'])
        print('values:', value)
        print(i, row['Name'], row['Mobile'], row['Address'], row['Education'])
        sql_var(sql, value)


class  StudentServices:
    def uploadFiles(self, file):
        print('uploaded file :', file)


        if file.filename !='':
            file_path =os.path.join(STATIC_DIR,file.filename)
            print('file path:', file_path)

            file.save(file_path)
            parseCSV(file_path)

        return "Your CSV File is Uploaded to read data and insert students_info into table"




