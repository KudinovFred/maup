import os
os.getcwd()


"""
>>> import os
>>> os.getcwd()
'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32'
>>> os.mkdir
<built-in function mkdir>
>>> os.mkdir("c:\\my")
>>> os.chdir("c:\\my")
>>> os.getcwd()
'c:\\my'
>>> import sys
>>> sys.path
['', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\win32', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\win32\\lib', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\Pythonwin']
>>> sys.path.append("c:\\my")
>>> sys.path
['', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\win32', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\win32\\lib', 'C:\\Users\\vshu\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\Pythonwin', 'c:\\my']
>>> sys.path.pop()
'c:\\my'
"""

