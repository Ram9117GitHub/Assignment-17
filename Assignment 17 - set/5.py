"""Write a python program to add items from another set to the current set. 
thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
"""
thisset ={"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
secondset.update(thisset)
print(secondset)
"""""""""""""""""""""""""""""""""""""""""""""""""""""Output"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
{'NoSQL', 'Java', 'Python', 'SQL', 'C', 'Cpp'}
"""


