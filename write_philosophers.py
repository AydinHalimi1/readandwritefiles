def main():
    #Open File
    outfile = open('philosophers.txt','w')

    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')
    #Close File
    outfile.close()

def add_my_name():
    outfile = open('philosophers.txt','a')
    
    outfile.write('Aydin Halimi\n')
    
    outfile.close()

main()
add_my_name()