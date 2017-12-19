import csv
import re
# Reading the file and storing it in respective list
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
# Question 1
#List of Single degrees & extracting the multiple degree in one list
degree_single=[]
degree_mult=[]
all_degree=[]
remove_list=[]
for d in x_degree[1:]:
    d=(d.strip())
    all_degree.append(d)    
    d=d.upper()
    d=d.replace(".","")
    if (len(d) >3):
        d=d.replace(" ",",")
        degree_mult.append(d)
        
    elif(len(d)==1): # removing the item with no degree '0'
        remove_list.append(d)
    else:
        degree_single.append(d)

#flattening of list
x_m=[]
for f in degree_mult:
    f1=f.split(",")
    for f2 in f1:
        x_m.append(f2)
    
degree_list=x_m+degree_single

# Unique Names and count of degrees 
print(set(degree_list))
print("The length of unique name in degrees {}".format(len(set(degree_list))))

#Count of each degree individually
count_phd,count_mph,count_scd,count_bsed,count_md,count_ms,count_jd,count_ma=[0,0,0,0,0,0,0,0]

for t in degree_list:
    if re.findall(r"PHD",t):
        count_phd+=1
    elif re.findall(r"MPH",t):
        count_mph+=1
    elif re.findall(r"SCD",t):
        count_scd+=1
    elif re.findall(r"MA",t):
        count_ma+=1
    elif re.findall(r"BSED",t):
        count_bsed+=1
    elif re.findall(r"MD",t):
        count_md+=1
    elif re.findall(r"MS",t):
        count_ms+=1
    else:
        count_jd+=1

print("The PH.D appears {} times in a list of {}  ".format(count_phd,len(x_degree[1:])))
print("The Sc.D appears {} times in a list of {}  ".format(count_scd,len(x_degree[1:])))
print("The M.D. appears {} times in a list of {}   ".format(count_md,len(x_degree[1:])))
print("The MPH appears {} times in a list of {}  ".format(count_mph,len(x_degree[1:])))
print("The B.s.Ed appears {} times in a list of {}  ".format(count_bsed,len(x_degree[1:])))
print("The M.S. appears {} times in a list of {}  ".format(count_ms,len(x_degree[1:])))
print("The J.D appears {} times in a list of {}  ".format(count_jd,len(x_degree[1:])))
#print(count_phd,count_mph,count_scd,count_bsed,count_md,count_ms,count_jd,count_ma)

#Question 2
# Unique Title headings

title_heading=[]
for titl in x_title[1:]:
    titl=titl.replace(" of Biostatistics","")
    titl=titl.strip(" is Biostatistics")
    title_heading.append(titl)
print("Names of title heading {}".format(set(title_heading)))
#title_heading
print("Number of Unique title heading {}".format(len(set(title_heading))))


#Question 3, 4
#Unique email names and count    
email=[]
for idx, word in enumerate(x_email[1:]):
    e=(word).strip()
    #email.append(e)
    el=(re.search("([\w.]+)@([\w.]+)",e))
    email.append(el.group())
print(email)

domain=[]
for idx, word in enumerate(x_email[1:]):
    dm=word.strip()
    #email.append(e)
    dmn=(re.search("@([\w.]+)",dm))
    domain.append(dmn.group(1))
Unique_domain=set(domain)
print(Unique_domain)
print(" Number of Unique Email domains {}".format(len(Unique_domain)))

