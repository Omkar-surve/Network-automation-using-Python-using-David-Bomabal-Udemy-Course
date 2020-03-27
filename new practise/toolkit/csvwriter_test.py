from csv import DictWriter, DictReader

with open('test_csv','w') as f:
    csv_writer = DictWriter(f,fieldnames=['name','contact'])
    csv_writer.writerows([{'name':'omkar','contact':'123'},{'name':'surve','contact':'456'}])

with open('test_csv','r') as t:
    csv_reader = DictReader(t,fieldnames=['name','contact'])
    for k in csv_reader:
        print(k['contact'])
