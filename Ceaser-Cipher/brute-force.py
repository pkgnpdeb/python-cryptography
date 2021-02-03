# ceaser cipher hacking 
# via Brute Force 

message = 'VORD GRGVIJ CVRBVU RK RYR.TFD'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123567890 !?.'

# Loop through every possible key 
for key in range(len(SYMBOLS)):
    """
    It is important to set translated to blank string so that the previous 
    iteration's value for translated is cleared:
    """
    translated = ''

    
    # The rest of the program is almost as same as Ceaser Cipher
    # Loop through each symbol in message: 
    
    for symbol in message:
        if symbol in SYMBOLS: 
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key 

            # Handle wraparound:
            if translatedIndex <0:
                translatedIndex = translatedIndex + len(SYMBOLS)

                # Append the decrypted symbol:
                translated = translated + symbol

        else:
            # Append the symbol without encrypting/decrytping 
            translated = translated + symbol 

    # Display possible decryption: 
    print('Key #%s: %s' % (key, translated))
