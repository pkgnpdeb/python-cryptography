# Ceaser Cipher, Ceaser Cipher Brute-Force attack and Transportation Cipher

## Algorithm of Ceaser Cipher 

```
# The algorithm of Caesar cipher holds the following features −
* Caesar Cipher Technique is the simple and easy method of encryption technique.
* It is simple type of substitution cipher.
* Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet.

# Explanation

* The plain text character is traversed one at a time.
* For each character in the given plain text, transform the given character as per the rule.
* Depending on the procedure of encryption and decryption of text.
* After the steps is followed, a new string is generated which is referred as cipher text.

```

## Requirements 

```
----- Install Pyperclip -----
$ pip install pyperclip		[On Python2]
$ pip3 install pyperclip	[On Python3]

----- Install XSEL (For Pyper copy/paste) -----
$ sudo apt install xsel

``` 

## Ceaser Cipher Algorithm Visual
![ceaser](https://user-images.githubusercontent.com/48232101/106557274-9282dd80-6549-11eb-9318-c0400618356f.png)

## Ceaser Cipher Visual
![ceaser](https://user-images.githubusercontent.com/48232101/106877332-bc323500-6700-11eb-864e-a6639918c23b.png)

## Ceaser Cipher Brute-Force Visual
![brute](https://user-images.githubusercontent.com/48232101/106877641-17fcbe00-6701-11eb-92ae-00e9fdf7bd81.gif)

## Algorithm of Transposition Cipher 
```
Transposition Cipher is a cryptographic algorithm where the order of alphabets in the plaintext is rearranged to form a cipher text. 
In this process, the actual plain text alphabets are not included.

Example
A simple example for a transposition cipher is: 
Columnar transposition cipher where each character in the plain text is written horizontally with specified alphabet width. 
The cipher is written vertically, which creates an entirely different cipher text.

For example, suppose we use the keyword ZEBRAS and the message WE ARE DISCOVERED. FLEE AT ONCE. 
In a regular columnar transposition, we write this into the grid as follows:

6 3 2 4 1 5
W E A R E D
I S C O V E 
R E D F L E 
E A T O N C 
E Q K J E U 
providing five nulls (QKJEU), these letters can be randomly selected as they just fill out the incomplete columns
and are not part of the message. The ciphertext is then read off as:

EVLNE ACDTK ESEAQ ROFOJ DEECU WIREE

In the irregular case, the columns are not completed by nulls:

6 3 2 4 1 5
W E A R E D 
I S C O V E 
R E D F L E 
E A T O N C 
E 
This results in the following ciphertext:

EVLNA CDTES EAROF ODEEC WIREE

```

## Transposition Cipher Algorithm Visual
* Will be updated soon 

## Transposition Cipher Visual (Encryption) 
* Will be updated soon 

