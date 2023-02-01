# Lab02
## The Python code for encryption and decryption of DNA data

DNA is a powerful way of capturing knowledge containing a set of orders to create a living machine. Besides this kind of knowledge, humans develop what is called an **“explanatory knowledge”** from their creativity to understanding physical world, creating technological innovations or even spreading cultural memes (adapted from David Deutsch's TED talk). As Dawkins stated before, ***“No matter how much knowledge and wisdom you acquire during your life, not one jot will be passed on to your children by genetic means”*** (The Selfish Gene, 1976), *how could we cope with a long-lived way of preserving this precious information as do DNA capability?* Thanks to the human’s power of creativity (again), the encryption has finally come to light in the ways that information can be encoded into DNA string, so called the **“DNA storage”**, creating a promising long-term storage technology for the future. With a huge capacity of storing (1 gram of DNA can hold a number of petabytes of data), together with sequencing technology becoming more advanced, owning your DNA-made flash drive might not be far from reach. 

Luckily enough, I got inspired by these sci-fi stories that had brought me closer to DNA data storage concept entangled with the programing language. Thus, I’m very pleased to introduce my very first Python codes written for the purpose of encoding (writing) and decoding (reading) text data into a sequence of DNA letters. In doing so, the codes can be divided into two steps as follows:

**Step 1: Encoding, by converting texts/characters into binary values, followed by encoding into DNA letters.**
- 1.1 Construct a dictionary of 96 characters and 8-bits binary string (e.g., 00010111) as “keys” and “key-values”, respectively.
- 1.2 Get input (words/sentence) from user. Both the binary string and DNA sequence are returned to user (an output .txt file).

**Step 2: Decoding, by converting DNA sequence into binary values, followed by decoding into words/characters.**
- 2.1 Construct a dictionary of reciprocal pairs of those in step 1 as “keys” and “key-values”.
- 2.2 Get input (DNA sequence) from user. Both the binary string and words/characters are returned to user (an output .txt file).
