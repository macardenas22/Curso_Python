# función que elimine los duplicados de una lista [1,1,2,2,4] -> [1,2,4]

#opción general 
def remove_duplicates(some_list): #recibe una lista como parametro
    without_duplicates = [ ] #creación lista vacia 
    for element in some_list:
        #not in sino esta 
        if element not in without_duplicates:
	        without_duplicates.append(element)#agregará el elemento en la lista 
    return without_duplicates

def remove_duplicates1(some_list):
    return list(set(some_list))


def run():
	random_list = [1,1,2,2,4]
    # print(remove_duplicates(random_list))
	print(remove_duplicates1(random_list))
   
if __name__ == "__main__":
    run()

    


