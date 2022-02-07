import csv

def main():
    infile = open('customers.csv','r')

    customer = csv.reader(infile, delimiter=',')

    outfile = open('customer_country.csv','w')

    for record in customer:
        firstname = record[1]
        lastname = record[2]
        country = record[4]
        print(firstname)
        outfile.write(firstname + ',' + lastname + ',' + country + '\n')
    #print("Total Number of Counters" + str(counter-1))

    outfile.close()
    infile.close()
main()