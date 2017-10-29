# Insight Data Engineering
## Find Political Donors
#### Rui Ding

This repo contains the files and tests for the find political donors coding challenge.

Author: Rui Ding

Solution Description and Implementation Notes:

In this repo I provide a source code find_political_donors.py which solves the coding challenge problem.
The input data is read line by line as if it is streaming in. Lines where other_id is not empty will be skipped.

(1) To calculate the running median of the donation amounts for a specific recipient from a specific zipcode,
I maintain a dictionary zip_dic that stores past records of amount values as a list with the keys represented by the pair (ID,zip)
whenever ID and zip are checked to be valid. Upon a new distinct key from the current record, the dictionary will update a new entry with this key and initiate the value list to contain the amount from this record. If the current key already exists in the dictionary, then its amount list will append the current amount. After reading each valid record to the zip_dic, a running median
calculation for the current key's value list will be done and the output file medianvals_by_zip will write a corresponding line
in the required format.

(2)Similar to the by zip calculation, a dictionary date_dic is used to store amount lists under the key pairs (ID,date) whenever
ID and date are checked to be valid. The updating scheme is the same as before. The output file medianvals_by_date will not be written until all lines have been read. Then it sorts by ID alphabetically and then by date chronologically. Finally it writes one line with the specified format for every key pair (ID,date) which calculates the median for amounts given to a recipient on a particular date.

The structure of this repo follows the specifications of the coding challenge, with input file itcont.txt stored in the input folder and output files will be written to the output folder when you run the test code run.sh.
In the testsuites, there is the original sample test1(which has a very small input) and my own test2 which contains 5000 records from the online data source of political donations by individuals.
When the test code run_tests.sh is executed both tests will run and results will be compared with the prestored output answers.

Overall, the program passes the test case and is robust against different inputs. It runs in reasonable time and the structure is clear to unerstand.
