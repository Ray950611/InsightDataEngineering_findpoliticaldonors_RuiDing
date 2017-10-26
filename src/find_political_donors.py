import sys
def median(lst):
    n = len(lst)
    if n % 2 == 1:
            return sorted(lst)[int(n/2)]
    else:
            return (sorted(lst)[n/2-1]+sorted(lst)[n/2])/2.0
input_name = sys.argv[1]
output_date = sys.argv[3]
output_zip = sys.argv[2]

infile = open(input_name,'r')
out_date = open(output_date,'w')
out_zip = open(output_zip,'w')
date_dic = {}
zip_dic = {}
line = infile.readline()
while line!='':
    #print line
    line_list = line.split('|')
    #print line_list
    ID = line_list[0]
    date = line_list[13]
    amount = line_list[14]
    other = line_list[15]
    zipcode = line_list[10]
    #ignore
    if len(other)==0:
    
    #update date_dic
        if len(date)==8:
            cur1 = (ID,date)
            if cur1 not in date_dic.keys():
                date_dic.update({cur1:[int(amount)]})
            else:
                amount_list = date_dic[cur1]
                amount_list.append(int(amount))
        if len(zipcode)>=5:
            zipcode = zipcode[0:5]
            cur2 = (ID,zipcode)
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
    
    line = infile.readline()
infile.close()
out_zip.close()
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
