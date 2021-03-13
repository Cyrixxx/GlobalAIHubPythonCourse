#Hakan İleri

#CV infos: Job, Salary, City, Age

cvs = {} #create empty dictionary 
#create 5 cvs to store in dictionary
cv1 = {'Job': 'Rapper', 'Salary': '€40M', 'City': 'Stevenage-UK', 'Age': '36'}
cv2 = {'Job': 'Gardener', 'Salary': '€11M', 'City': 'Perth-Australia', 'Age': '31'}
cv3 = {'Job': 'Sergeant', 'Salary': '€6M', 'City': 'Nastola-Finland', 'Age': '31'}
cv4 = {'Job': 'Engineer', 'Salary': '€20M', 'City': 'Oviedo-Spain', 'Age': '39'}
cv5 = {'Job': 'Lawyer', 'Salary': '€8M', 'City': 'Heppenheim-Germany', 'Age': '33'}
#assign each cv to their names
cvs = {'Lewis':cv1, 'Daniel': cv2, 'Valtteri':cv3, 'Fernando':cv4, 'Sebastian':cv5}
for i in cvs: #print cvs to screen seperately 
    print ('\n' + i)
    for j in cvs[i]:
        print (j,':',cvs[i][j])