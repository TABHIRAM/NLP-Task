import re

with open(r'c:\Users\Ramu\Desktop\NLP\NewData.txt') as f:
    lines = f.readlines()
    for line in lines:
        if re.search(r'who', line):
            a = line+str('Type: Who ')
            print(a) 
            continue
        elif re.search(r'what', line):
            b = line+str('Type: What')
            print(b)
            continue    
        elif re.search(r'when', line):
            c = line+str('Type: When ')
            print(c)
            continue 
        elif re.search(r'how', line):
            d = line+str('Type: Unknown ')
            print(d)
            continue     
        else:
            e = line+str('Type: Affirmation')
            print(e)
            
#     file = open(r'c:\Users\Ramu\Desktop\NLP\Output.txt',"a") # Saving in a new file.
#     file.write(str(a))
#     file.write("\n")
#     file.write(str(b))
#     file.write("\n")
#     file.write(str(c))
#     file.write("\n")
#     file.write(str(d))
#     file.write("\n")
#     file.write(str(e))
#     file.write("\n")
        
#     file.close()            
             