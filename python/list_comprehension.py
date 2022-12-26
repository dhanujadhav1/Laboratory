import random

# print( [  i for i in range(0,10)])

# print( [random.randint(10,100) for n in range(20)])

# print( [(x,x**2,x**3 ) for x in range(10)])


lst = [ num if num > 2 else "True" for num in range(0,10) ]

# print(lst)
# 8766576849

# print( [ int(x) for x in ['10','20','30','40']])

a=  [ n for n in range(10,30) if n% 2==0]

# print( [ num for num in a if num <20 or num>50 ])

# print( ['!' if alphabet in 'aeiou' else alphabet for alphabet in 'Techical Guruji'])

arr=[[1,2,3],[4,5,6],[7,8,9]]

# print([n for ele in arr for n in ele])

aTemp= [1,2,3]
bTemp= [3,4,5]
# print([ a1+b1 for a1 in aTemp for b1 in bTemp ])

# print( [ [a+b for a in [1,2,3]] for b in [3,4,5]] )

print( [ (i,j,k) for i in [1,2,3] for j in [1,2,3] for k in [1,2,3] if i != j and j!= k and k!=i ])
