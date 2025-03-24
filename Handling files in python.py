#!/usr/bin/env python
# coding: utf-8

# # What is File?
# * Files are named locations on disk to store information
# * They are used to store data permanently
# * Data is stored in non-volatile memory
# * We can retrieve data whenever required
# 
# # Types of files-
# 
# * Text files:
#     Stores data in the form of charavters. it is used to store
#     data and strings.
#     example: .text,.jsone,
#     
# * Binary files: Stores data in the form of bytes(group of 8 bits).
#     example: Audio files, video files    
# # What is file handlings?
# File handling means:
#     * **Opening** a file.
#     * **Performing** some operations on it.
#     * **Closing** a file
# # Data store Two ways:
# 
# 1. **File handling**
# 2. **Database**
# 

# In[1]:


age = input('Enter your age:')
f= open('data.text', 'w')
f.write(age)
f.close()


# In[3]:


f=open('data.text', 'r')
print(f.read())


# In[4]:


f.close()


# # Opening file
# 
#     python provides an in-built function open() to open a file.
#     
#     Syntax:
#         f= open(filename, mode='r', encoding= None,
#                 errors=None, newline=None, closefd=True)
# 
#         f=open(filename,mode='r')
#           1. filename: file to be accessed
#           2. mode: access mode (purpose of opening file.)
#           3. f : file handler, file pointer
# 
# ## Different modes:
# 1. "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# 
# 2. "a" - Append - Opens a file for appending, creates the file if it does not exist
# 
# 3. "w" - Write - Opens a file for writing, creates the file if it does not exist
# 
# 4. "x" - Create - Creates the specified file, returns an error if the file exists
#   
#   
#   In addition you can specify if the file should be handled as binary or text mode.
#   
# 5. "t" - Text - Default value. Text mode
# 
# 6. "b" - Binary - Binary mode (e.g. images)
# 

# In[58]:


files1 ='''Hello! Welcome to demofile.txt
        This file is for testing purposes.
        Good Luck. '''
d = open('demofile.txt','w')
d.write(files1)
d.close()


# # Read only parts of the File
# By default the read() method returns the whole text, 
# but you can also specify how many characters you want to return:

# In[59]:


f = open('demofile.txt','r')
print(f.read(5))


# In[60]:


f.close()


# # Read Lines
# You can return one line by using the readline() method

# In[61]:


f = open('demofile.txt', 'r')
print(f.readline())


# In[62]:


f.close()


# By calling readline() two times, you can read the two first lines.

# In[63]:


k = open('demofile.txt', 'r')
print(k.readline())
print(k.readline())
k.close()


# By looping through the lines of the file, you can read the whole file,
# line by line.

# In[64]:


f = open('demofile.txt', 'r')
for x in f:
    print(x)


# In[65]:


f.close()


# **Note**: You should always close your files. In some cases, due to buffering, changes made to a file may not show untile you close the file.

# # Python File Write
# 
# ## Write to an Existing File
# 
# "a" - Append - will append to the end of the file
# 
# "w" - Write - will overwrite any existing content

# In[66]:


files2 ='''Hello! Welcome to demofile.txt
        This file is for testing purposes.
        Good Luck. '''
d = open('demofile2.txt','w')
d.write(files2)
d.close()


# In[67]:


f = open('demofile2.txt','a')
f.write("Now the file has more content!")
f.close()


# In[68]:


f = open('demofile2.txt','r')
print(f.read())


# In[69]:


f.close()


# Overwrite the content

# In[77]:


files3 ='''Hello! Welcome to demofile.txt
        This file is for testing purposes.
        Good Luck. '''
d = open('demofile3.txt','w')
d.write(files3)
d.close()


# In[78]:


f = open('demofile3.txt', 'w')
f.write('Woops! I have deleted the content!')
f.close()


# In[79]:


f= open('demofile3.txt', 'r')
print(f.read())


# ## Create a New File
# 
# To create a new file in Python, use the open() method, with one of the following parameters:
# 
# "x" - Create - will create a file, returns an error if the file exists
# 
# "a" - Append - will create a file if the specified file does not exists
# 
# "w" - Write - will create a file if the specified file does not exists

# In[116]:


f = open ('my file.txt', 'x')


# # Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function.
# 
# 

# In[80]:


import os


# More about os module (https://www.w3schools.com/python/module_os.asp?ref=escape.tech)

# In[82]:


f= open('demofile.txt', 'r')
f.close()
os.remove('demofile3.txt')


# In[89]:


f = open('my file.txt','r')
f.close()
os.remove('my file.txt')


# ## Check if file exist
# To avoid getting an error, you might want to check if the file exist before you try to delete it.

# In[90]:


if os.path.exists('demofile.txt'):
    os.remove('demofile.txt')
else:
    print('The file does not exist')


# ## Create a Folder by .os
# To Create a Single folder, use the os.mkdir() method

# In[109]:


os.mkdir('myfolder')


# To Creates Nested Folders, use the os.makedirs() method

# In[93]:


os.makedirs('parentfolder/childfolder')


# In[98]:


os.makedirs('myfolder/folder') # in here I create a folder under my exsiting folder'myfolder'.


# ## Delete Folder
# To delete an entire folder, use the **os.rmdir()** method

# In[110]:


os.rmdir('myfolder') # if it's empty othen then it's raises an OSError


# To delete nested folder we need to import shutill

# In[113]:


import shutil


# more about shutil module (https://docs.python.org/3/library/shutil.html)

# To delete nested folder, use the shutil.rmtree() method

# In[114]:


shutil.rmtree('parentfolder')


# In[ ]:




