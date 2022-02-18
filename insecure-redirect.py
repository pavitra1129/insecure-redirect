import os
input = raw_input("input the domain--> ")
a = "getallurls " + input + " | tee -a urls.txt"
os.system(a)
os.system("clear")
os.system("grep =http urls.txt | tee -a =http.txt")
os.system("rm -rf urls.txt")
