#Operations on Lists - September 13

#In addition to the string operations, there are additional operations that
#can be used to manipulate lists.

x = [1, 2, 3]
print(x)
x.append(4)                      #add item to end of list x
print(x)               
x.extend([6, 7])                 #add new list to end of list x
print(x)
print(x.pop(5))                  #pops 5th item of list x
#print(list.pop(x))              #why does this do the same thing? [not quite the same...]
print(x)
x.insert(6,5)                    #inserts 5 at new spot 6
print(x)
print(x.sort())                  #sorts list x
print(x)
#also available:
s = "Sphinx of black quartz, judge my vow"
#print(s.sort())                 <can't do it.
l = ["s","p","h","i","n","x",
     "o","f",
     "b","l","a","c","k",
     "q","u","a","r","t","z",
     "j","u","d","g","e",
     "m","y",
     "v","o","w"]
print(l)
l.sort()                         #can do it
print(l)

##    also available:
##    x.index(y)  returns the position of the first occurence of item y in list x
##    x.count(y)  returns number of times y appears in x
##    x.remove(y) removes the ~*first instance of item y in list*~
