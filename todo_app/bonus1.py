filenames = ['1.Rawdata.txt', '2.Presentation.txt', '3.Report.txt']


for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)
    
print(filenames)