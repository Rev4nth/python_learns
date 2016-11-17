# Ex-5
# Extract filenames that has txt as extension
import re
filenames = ['file1.txt', 'file2.txt', 'file3.pdf', 'file4.pdf']
filenew = []
for filename in filenames:
    match = re.search(r'.txt',filename)
    if match:
        filenew.append(filename)
print filenew
