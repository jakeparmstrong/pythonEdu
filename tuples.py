#The tuple works like an array, but it uses round brackets
tuple = (1,2,5,3,4)
print(tuple) #output is (1, 2, 5, 3, 4)

#tuple[2]=3 //Error: you can't re-assign individual 
#tuple[3]=4 //values in a tuple
#tuple[4]=5 //

tuple = (1,2,3,4,5) #However: You may overwrite the whole structure
print(tuple) #output is (1, 2, 3, 4, 5)
#tuple[5] = 6 //This produces an error, but...
tuple = (0,0,0,0,0,0) #you can resize a tuple like this
print(tuple)
