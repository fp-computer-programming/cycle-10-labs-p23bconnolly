#lab 10-3    
def double_stuff (stuff):
    for index, var in enumerate(stuff):
            stuff[index] = var*2
    return(stuff)
#a function that takes list as its only parameter
print()

print(double_stuff([1,5,10]))

print(double_stuff([5,"dog",200]))

print(double_stuff(["cat",6,1.75]))
#each of these test cases double the values in each list