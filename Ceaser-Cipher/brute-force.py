"""
<<<<<<< HEAD
Caesar Cipher Hacker
with Brute Force Method
"""

message = 'LRF, RKNZ CNCREF UNF ORRA YRNXRQ.'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.,'

# Loop through every possible key:
for key in range(len(SYMBOLS)):
    """
    It is important to set translated to blank string so that the 
    previous iteration's value for translation is cleared: 
    """
    translated = ''
    
    """
    The rest of the program is similar as Ceaser program: 
    
    Loop through each symbol in message: 
    """
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key
            
            # Handle wraparound:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)
                
                #Append the decrypted symbol:
                translated = translated + SYMBOLS[translatedIndex]
        else:
             # Append the symbol without encrypting/decrypting:
             translated = translated + symbol

     # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))
