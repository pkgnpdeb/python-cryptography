# Reverse Cipher Algorithm 

message = "Three can keep a secret, if two of them are dead"

# variable for cipher text 
translated = ''

# index variable for creating cipher 
i = len(message) -1

# Loop 
while i>=0:
    translated = translated+message[i]
    i = i-1

# print cypher text message 
print(translated)



