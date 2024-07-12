import hashlib
import csv

def hash_password_hack(input_file_name, output_file_name):
    with open(f'{input_file_name}.csv','r') as f :
        reader=csv.reader(f)
        with open(f'{output_file_name}.csv','w',newline='') as final :
            writer=csv.writer(final)
            a=dict()
            for i in range(1000,10000) :     #It is guaranteed that the passwords are 4 digits long.
                hash=hashlib.sha256(str(i).encode('utf-8')).hexdigest()
                a[hash]=str(i)
            for row in f :
                b=list()
                c=list()
                list_row=row.strip().split(',')
                b.append(list_row[0])  
                for key,value in a.items() :
                    if list_row[1]==key :
                        c.append(a[key])  
                writer.writerow(b+c)
                        
                

    


