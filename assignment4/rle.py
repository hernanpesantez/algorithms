def encode(input_string):
    count = 1
    prev = ''
    lst = []
    operations = 0
    for character in input_string:
        operations+=1
        if character != prev:
            if prev:
                operations += 1
                
            
                entry = (prev,count)
                lst.append(entry)
                #print lst
            count = 1
            prev = character
        else:
            operations+=1
            count += 1
    else:
        try:
            operations+=1
            
            entry = (character,count)
            lst.append(entry)
            return lst, 0 , operations
            

        except Exception as e:
            print("Exception encountered {e}".format(e=e)) 
            return e, 1, 0
 
def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q
