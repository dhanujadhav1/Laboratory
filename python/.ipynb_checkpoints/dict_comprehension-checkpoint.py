# General syntax for writing dict comprehension
# dict_var = { Key:value for (key,value) in dictionary.items()}
# 

d={ 1:'a',2:'b',3:'c',4:'d'}

# print( { k: v + "_processed" for (k,v) in d.items() if v !='a'})

print( {k: ('vowels' if v=='a' else "consonants" ) for (k,v) in d.items()})

