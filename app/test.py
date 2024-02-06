a='''data = ["6 OVA","7 Special","8 TV"]
rs=["TV","OVA","Movie","TV Special","Special"]
for j in data:
    for i in rs:
        if i in j:
            data[(data.index(j))]=j[0:(len(j)-len(i)-1)]
            print(j[0:(len(j)-len(i))])
            #data[data.index(j)]='j[0:(len(j)-len(i))]'
            #print(j[0:(len(j)-len(i))])
print(data)'''
import re

# Sample list of strings
data = ["6 OVA", "7 TV", "10 Movie", "5 TV", "4 OVA", "Other String"]

# Regular expression pattern to match substrings to be removed
pattern = re.compile(r'\b(?:OVA|TV|Movie)\b')

# Remove substrings from the list of strings
filtered_data = [pattern.sub('', item) for item in data]

print(filtered_data)