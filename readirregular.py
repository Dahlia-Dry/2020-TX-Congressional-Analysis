import pandas as pd
def readirregular(filename,outfile):
    csvlines = []
    for line in open(filename,"r"):
        values = line.split()
        for i in range(len(values)):
            values[i] = values[i].replace(',','')
        csvlines.append(','.join(values))
        print(values)
    with open(outfile,'w') as file:
        for line in csvlines:
            file.write(line)
            file.write('\n')
readirregular('sos/allcounties-2020senatefinal.txt',
            'sos/allcounties-2020senatefinal.csv')
