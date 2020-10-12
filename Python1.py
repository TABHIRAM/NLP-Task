import re 

with open(r'c:\Users\Ramu\Desktop\NLP\LabelledData.txt') as file_in:
    lines = []
    for line in file_in:
         lines.append(line)
         #print(line)

          #print(type(line))
         raw_to_string = re.split(',,,', line)[:1] # Removing Answers.
         print(raw_to_string) 
     
         file = open(r'c:\Users\Ramu\Desktop\NLP\NewData.txt',"a") # Saving in a new file.
         file.write(str(raw_to_string))
         file.write("\n")
         file.close()
 
        
      
        