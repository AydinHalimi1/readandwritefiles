import csv

def main():

    infile = open("EmployeePay.csv", 'r')

    emp_file = csv.reader(infile, delimiter = ',')

    next(emp_file)

    outfile = open("Employee_Bonus.csv", 'w')

    for record in emp_file:
        id_num = record[0]
        firstname = record[1]
        lastname =record[2]
        salary = record[3]
        bonus = record [4]
        totalpay = record[3] + (record)