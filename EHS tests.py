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

def cleanup_1166(CP_file, output_file): #Needs Assessments
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                #print(row)
                row.insert(0, row[4])
                row.insert(1, row[6])
                row.insert(2, row[5])
                del row[4:]
                #print(row)
                csv_out.writerow(row)

def cleanup_1235(CP_file, output_file): #Family goals
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                row.insert(2, row[5])
                del row[6:]
                del row[4]
                #print(row)
                csv_out.writerow(row)

def cleanup_1073(CP_file, output_file): #Needs Identified
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                row.insert(0, row[4])
                row.insert(1, row[7])
                row.insert(2, row[7])
                p_key = row[0] + row[4] + row[5]
                row.insert(2, p_key)
                del row[1:3]
                del row[3:5]
                del row[-5:]
                #print(row)
                csv_out.writerow(row)

def cleanup_4220(CP_file, output_file): #FASN cleanup
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                del row[1:6]
                del row[2:7]
                del row[3:9]
                del row[4:]
                try:
                    int(row[1])
                    if row[2] == '':
                        row[2] = 'Yes'
                    else:
                        row[2] = 'No'
                    if row[3] == '':
                        row[3] = 'Yes'
                    else:
                        row[3] = 'No'
                    print(row)
                    csv_out.writerow(row)
                except:
                    if row[1] == 'Family ID':
                        row[2] = 'Entry Complete'
                        row[3] = 'Exit Complete'
                        print(row)
                        csv_out.writerow(row)



cleanup_1214(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 EHS Class Roster.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 EHS CR Output.csv")
cleanup_1214fam(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 EHS Class Roster.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 EHS Family Output.csv")
cleanup_1214entry(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 EHS Class Roster.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 EHS 90 Output.csv")
cleanup_1034(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1034 EHS Home Visits.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1034 EHS HV.csv")
cleanup_1166(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1166 EHS Needs Assessments.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1166 EHS NA Output.csv")
cleanup_1235(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1235 EHS Family Goals.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1235 EHS FG Output.csv")
cleanup_1073(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1073 EHS Need Identified.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1073 EHS NI Output.csv")
cleanup_4220(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\4220 EHS FASNs.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\4220 EHS FASNs Output.csv")



