# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:15:39 2019

@author: DavidGaribaldi
"""

import csv

def cleanup_1034(CP_file, output_file): #1034 cleanup, parent conferences and home visits
    split_list = []
    with open(CP_file) as old_file, open(output_file, 'w', newline = '') as output:
        for line in old_file:
            split_list = line.split(',')
            split_list[7] = split_list[8].replace('"', '').strip() + ' ' + split_list[7].replace('"', '').strip()
            w = csv.writer(output, quoting = csv.QUOTE_NONE, quotechar = '')
            while len(split_list) > 8:
                split_list.pop()
            del split_list[2:4]
            del split_list[3]
            #print(split_list)
            if 'Ã±' in split_list[-1]:
                split_list[-1] = split_list[-1].replace('Ã±', 'ñ')
            split_list.insert(1, split_list[-1])
            split_list.pop()
            split_list.append(split_list[0] + split_list[3])
            w.writerow(split_list)
            
def cleanup_1026(CP_file, output_file): #1026 cleanup, only adds advocate groups
    advocate_list = ['Angie', 'Berenis', 'Diana', 'Jane', 'Janette', 'Jenny', 'Judith', 'Lauren', 'Leah', 'Maria', 'Sara', 'Group Name', '']
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                row.insert(0, row[3])
                row.insert(2, row[5])
                del row[5:7]
                print(row)
                if row[5] in advocate_list:
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
                
def cleanup_1073b(CP_file, output_file): #Family goals
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                del row[0]
                row.insert(0, row[5])
                del row[4:]
                print(row)
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
                    csv_out.writerow(row)
                except:
                    if row[1] == 'Family ID':
                        row[2] = 'Entry Complete'
                        row[3] = 'Exit Complete'
                        csv_out.writerow(row)
                        
def cleanup_1077(CP_file, output_file): #CRMs cleanup
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                row.pop()
                row.insert(0, row[2])
                del row[3]
                print(row)
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
                csv_out.writerow(row)
                
def cleanup_1214(CP_file, output_file): #Roster Report
    with open(CP_file) as fin:
        with open(output_file, 'w', newline = '') as fout:
            csv_in = csv.reader(fin)
            csv_out = csv.writer(fout)
            for row in csv_in:
                del row[2:]
                print(row)
                csv_out.writerow(row)
            
            
cleanup_1034(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1034 Parent Conferences.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1034 PC Output.csv")
cleanup_1034(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1034 Home Visits.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1034 HV Output.csv")
cleanup_1026(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1026 Group List.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1026 GL Output.csv")
cleanup_1166(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1166 Needs Assessments.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1166 NA Output.csv")
cleanup_1073b(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1073 Family Goals.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1073b FG Output.csv")
cleanup_4220(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\4220 FASNs.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\4220 FASNs Output.csv")
cleanup_1077(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1077 CRMs.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1077 CRM Output.csv")
cleanup_1073(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1073 Need Identified.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1073 NI Output.csv")
cleanup_1214(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 Homeless App.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 App Output.csv")
cleanup_1214(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 Homeless FS.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 FS Output.csv")
cleanup_1214(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 Class Roster.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 CR Output.csv")
cleanup_1214(r"C:\Users\DavidGaribaldi\Desktop\Python Inputs\1214 PIR.csv", r"C:\Users\DavidGaribaldi\Desktop\Python Outputs\1214 PIR Output.csv")

















