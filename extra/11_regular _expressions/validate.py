import re 

email = input("What is your email? ").strip()

if re.search(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email, re.IGNORECASE):
    print ("Valid")
else:
    print("Invalid") 
    
# [] Cualquier caracter dentro de los corchetes 
# [^] ninguno de los caracteres que estan dentro de los corchetes

# \d decimal digit
# \D not a decimal digit
# \s whitespace characters
# \S not a whitespace caracters
# \w word character... as well as number and the undercore
# \W not a word character 

# A|B either A or B
# (...) a group
# (?:...) non-capturing version