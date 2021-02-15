# Transposition Cipher Encryption

# Python Cryptography Module 
import pyperclip 

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8 
    
    ciphertext = encryptMessage(myKey, myMessage)
    
    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message:
    print(ciphertext+ '|')
    
    # Copy the encrypted string in ciphertext to the clipboard:
    pyperclip.copy(ciphertext)
    
def encryptMessage(myKey, myMessage):
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] *myKey
    
    # Loop through each column in ciphertext:
    for column in range(myKey):
        currentIndex = column 
        
        # Keep looping until currentIndex goes past the message length:
        while currentIndex<len(myMessage): 
        # Place the character at currentIndex in message at the
        # end of the current column in the ciphertext list:
             ciphertext[column] += myMessage[currentIndex]
             
              # Move currentIndex over:
             currentIndex += myKey
             
         # Convert the ciphertext list into a single string value and return it:
        return ''.join(ciphertext)
        
# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()
