#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Convert html table to CSV file

import csv
from bs4 import BeautifulSoup, NavigableString

print("Name for file")
file_name = input()
file_name = file_name + '.csv'
print(' ')

print("Enter Html of the Table ")
table = input()

html_doc = table
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())

f = open(file_name, 'w')
writer = csv.writer(f)


# In[2]:


#header
header = []
for element in soup.find_all("th"):
    print(element.string)
    header.append(element.string)
print(header)
writer.writerow(header)


# In[3]:


#data
ros_data = []
from bs4 import BeautifulSoup, NavigableString, Tag
for sibling in soup.tr.next_siblings:
    data = []
    
    for child in sibling:
        if(isinstance(child, Tag)):
            data.append(child.get_text())
    ros_data.append(data)
print(ros_data)
writer.writerows(ros_data)
f.close()
