#lab 10-3    
def double_stuff (stuff):
    for index, var in enumerate(stuff):
            stuff[index] = var*2
    return(stuff)

print()

print(double_stuff([1,5,10]))

print(double_stuff([5,"dog",200]))

print(double_stuff(["cat",6,1.75]))