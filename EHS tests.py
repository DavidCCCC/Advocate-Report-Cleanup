import csv
from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m/%d/%Y")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2-d1).days)


def cleanup_1214(CP_file, output_file): #Roster Report
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                del row[2]
                if 'EHS' in row[5]:
                    del row[5]
                elif 'Home' in row[6]:
                    del row[6]
                del row[3:5]
                del row[4]
                csv_out.writerow(row)

def cleanup_1214fam(CP_file, output_file): #Roster Report
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                del row[:3]
                del row[1]
                del row[2:]
                csv_out.writerow(row)
            for poop in csv_in:
                print("Hello")
                if poop != "":
                    print("poop")

def familydicter(csv_in, csv_out):
    n = 1
    today = str(datetime.today().date())
    family = {}
    for row in csv_in:
        if n != 1 and row[3] not in family:
            if days_between(row[4], today) > 90:
                family[row[3]] = days_between(row[4], today)
        csv_out.writerow(row)
        n = 2
    return family

def cleanup_1214entry(CP_file, output_file): #family enrolled within 90 days
    with open(CP_file) as fin:
        with open(r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\temp.csv", 'w', newline = '') as fouttemp:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fouttemp)
            familydict = familydicter(csv_in, csv_out)
    with open(r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\temp.csv") as ftemp:
        with open(output_file, 'w', newline='') as fout:
            csv_in = csv.reader(ftemp)
            csv_out = csv.writer(fout)
            for row in csv_in:
                del row[0:3]
                del row[1]
                del row[2:]
                if row[0] not in familydict:
                    csv_out.writerow(row)

def cleanup_1034(CP_file, output_file):
    with open(CP_file) as fin:
        with open(output_file, 'w', newline='') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                del row[2:7]
                del row[3:]
                csv_out.writerow(row)



cleanup_1214(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 EHS Class Roster.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 EHS CR Output.csv")
cleanup_1214fam(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 EHS Class Roster.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 EHS Family Output.csv")
cleanup_1214entry(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 EHS Class Roster.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 EHS 90 Output.csv")
cleanup_1034(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1034 EHS Home Visits.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1034 EHS HV.csv")