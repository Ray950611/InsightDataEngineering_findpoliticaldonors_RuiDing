import sys
#my median function
def median(lst):
    n = len(lst)
    if n % 2 == 1:
            return sorted(lst)[int(n/2)]
    else:
            return (sorted(lst)[n/2-1]+sorted(lst)[n/2])/2.0
#command line arguments for input and output file names
input_name = sys.argv[1]
output_date = sys.argv[3]
output_zip = sys.argv[2]
#read file
infile = open(input_name,'r')
out_date = open(output_date,'w')
out_zip = open(output_zip,'w')
#two dictionaries used to store by date and by zip data
date_dic = {}
zip_dic = {}
#skip the first line
line = infile.readline()
while line!='':
    line_list = line.split('|')
    #identify the five important variables
    ID = line_list[0]
    date = line_list[13]
    amount = line_list[14]
    other = line_list[15]
    zipcode = line_list[10]
    #check other is empty while ID and amount are not
    if len(other)==0 and len(ID)!=0 and len(amount)!=0:
    #update date_dic if date valid
        if len(date)==8:
            cur1 = (ID,date)
            #check if key cur1 exists in the record or is a new key
            if cur1 not in date_dic.keys():
                date_dic.update({cur1:[int(amount)]})
            else:
                amount_list = date_dic[cur1]
                amount_list.append(int(amount))
    #update zip_dic and print a line to by zip output file if zipcode valid
        if len(zipcode)>=5:
            zipcode = zipcode[0:5]
            cur2 = (ID,zipcode)
            #check if key cur2 exists in the record or is a new key
            if cur2 not in zip_dic.keys():
                zip_dic.update({cur2:[int(amount)]})
                out_zip.write(ID+'|'+zipcode+'|'+str(amount)+'|'+str(1)+'|'+str(amount)+'\n')
            else:
                amount_list = zip_dic[cur2]
                amount_list.append(int(amount))
                sum_amount = sum(amount_list)
                count = len(amount_list)
                med = int(round(median(amount_list)))
                out_zip.write(ID+'|'+zipcode+'|'+str(med)+'|'+str(count)+'|'+str(sum_amount)+'\n')
    #read next record
    line = infile.readline()
infile.close()
out_zip.close()
#Now write the by date output file
#sort the ID,date pairs
keys = sorted(date_dic)
for key_pair in keys:
    ID = key_pair[0]
    date = key_pair[1]
    amount_list = date_dic[key_pair]
    sum_amount = sum(amount_list)
    count = len(amount_list)
    med = int(round(median(amount_list)))
    out_date.write(ID+'|'+date+'|'+str(med)+'|'+str(count)+'|'+str(sum_amount)+'\n')
out_date.close()
