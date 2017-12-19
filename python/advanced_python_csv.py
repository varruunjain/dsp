import re
import csv
with open("/Users/varru/Documents/Python Scripts/faculty.csv") as filename:
    reader= csv.reader(filename, delimiter=',')
    x_name=[]
    x_degree=[]
    x_title=[]
    x_email=[]
    for row in reader:
        x_name.append(row[0])
        x_degree.append(row[1])
        x_title.append(row[2])
        x_email.append(row[3])


email=[]
for idx, word in enumerate(x_email[1:]):
    e=(word).strip()
    email.append(e)
    el=(re.search("([\w.]+)@([\w.]+)",e))
    email.append(el.group())
domain=[]
for idx, word in enumerate(x_email[1:]):
    dm=word.strip()
    #email.append(e)
    dmn=(re.search("@([\w.]+)",dm))
    domain.append(dmn.group(1))
Unique_domain=set(domain)
print(Unique_domain)
print(" Number of Unique Email domains {}".format(len(Unique_domain)))

with open("emails.csv",'w') as file:
    em=csv.writer(file,delimiter='\n',dialect='excel')
    em.writerow(email)

