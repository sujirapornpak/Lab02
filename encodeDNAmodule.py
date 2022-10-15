

def encod_WordstoDNA(yy):
    yy = input('Your input words: ')
    yy = list(yy)
    
    ## Note: This dictionary contains only 96 characters, while 8-bits can encode 2^8 = 256 possibility of characters.
    ASCII = {' ':'00100000','!':'00100001','"':'00100010','#':'00100011',
        '$':'00100100','%':'00100101','&':'00100110',"'":'00100111',
        '(':'00101000',')':'00101001','*':'00101010','+':'00101011',
        ',':'00101100','-':'00101101','.':'00101110','/':'00101111',
        '0':'00110000','1':'00110001','2':'00110010','3':'00110011',
        '4':'00110100','5':'00110101','6':'00110110','7':'00110111',
        '8':'00111000','9':'00111001',':':'00111010',';':'00111011',
        '<':'00111100','=':'00111101','>':'00111110','?':'00111111',
        '@':'01000000','A':'01000001','B':'01000010','C':'01000011',
        'D':'01000100','E':'01000101','F':'01000110','G':'01000111',
        'H':'01001000','I':'01001001','J':'01001010','K':'01001011',
        'L':'01001100','M':'01001101','N':'01001110','O':'01001111',
        'P':'01010000','Q':'01010001','R':'01010010','S':'01010011',
        'T':'01010100','U':'01010101','V':'01010110','W':'01010111',
        'X':'01011000','Y':'01011001','Z':'01011010','[':'01011011',
        ']':'01011101','^':'01011110','_':'01011111',"'\'":'01011100',
        '`':'01100000','a':'01100001','b':'01100010','c':'01100011',
        'd':'01100100','e':'01100101','f':'01100110','g':'01100111',
        'h':'01101000','i':'01101001','j':'01101010','k':'01101011',
        'l':'01101100','m':'01101101','n':'01101110','o':'01101111',
        'p':'01110000','q':'01110001','r':'01110010','s':'01110011',
        't':'01110100','u':'01110101','v':'01110110','w':'01110111',
        'x':'01111000','y':'01111001','z':'01111010','{':'01111011',
        '|':'01111100','}':'01111101','~':'01111110','DEL':'01111111'}
    
    ## Step1: To convert words into long binary string.
    bina = ''
    for i in list(range(len(yy))):
        char = yy[i]
        if char in ASCII:
            bina += ASCII[char]        
    
    ## Step2: To encode 2 bits to DNA base.
    simbasedict = {'00':'A', '01':'T','10':'C','11':'G'}
    myencode = ''
    for i in list(range(0,len(bina),2)):
        bits = bina[i:i+2]
        if bits in simbasedict:
            myencode += simbasedict[bits]
    GCcnt = (myencode.count('G')+myencode.count('C'))/len(myencode)*100
    ATcnt = (myencode.count('A')+myencode.count('T'))/len(myencode)*100
    
    ## Step3: To split long binary string into disered length (window size).        
    binar = ''
    for ii in list(range(0,len(bina),20)):
        line = bina[ii:ii+20]
        binar += line+('\n')    
    
    
    ## Step4: To split long DNA into disered length (window size).
    window = ''
    for ii in list(range(0,len(myencode),20)):
        line2 = myencode[ii:ii+20]
        window += line2+('\n')
    
    ## Step5: To write output into new text file. 
    stri = ''
    f = open('encode_Words_to_DNA.txt','w')
    f.write('Your input words:'+'\n'+stri.join(yy)+'\n'+'\n')
    f.write('Words encoded to binary, '+str(len(bina))+' bits in total, based on the ASCII format are shown below:\n')
    f.write(binar+'\n')
    f.write('Binary sequence encoded to DNA sequence is shown below:\n')
    f.write(window+'\n')
    f.write('The length of this DNA sequence is '+str(len(myencode))+' bp. GC and AT content are '+str(GCcnt)+'% and '+str(ATcnt)+'%, respectively.')
    f.close()
    
    ## Step6: To print both outputs to user presented in jupyter nb..    
    print ('Your words can be converted into binary code,',len(bina),'bits in total, based on the ASCII format as:\n'+binar)
    print ('Binary sequence encoded into DNA sequence is shown below:\n'+window)
    print ('The length of this DNA sequence is',len(myencode),'bp. GC and AT content are',GCcnt,'% and',ATcnt,'%, respectively.')
    print ('Your output file is saved in the text file as "encode_Words_to_DNA.txt".')



def decod_DNAtoWords(xx):
    xx = input('Your input DNA sequence: ')
    xx = xx.replace(' ','')
    GCcnt = (xx.count('G')+xx.count('C'))/len(xx)*100
    ATcnt = (xx.count('A')+xx.count('T'))/len(xx)*100
    
    ## Step1: To convert DNA into long binary string.
    simbasedict2 = {'A':'00', 'T':'01','C':'10','G':'11'}
    mydecode = ''
    for i in list(range(0,len(xx))):
        base = xx[i:i+1]
        if base in simbasedict2:
            mydecode += simbasedict2[base]
    
    ## Step2: To decode 8-bits to characters.
    ## Noted that 8-bits results in 2^8 = 256 possibility of characters. 
    ## However, this dictionary contains only 96 characters, which might cause 'KeyError' if any 8-bits don't exist.
    ASCIIex = {'00100000':' ','00100001':'!','00100010':'"','00100011':'#',
        '00100100':'$','00100101':'%','00100110':'&','00100111':"'",
        '00101000':'(','00101001':')','00101010':'*','00101011':'+',
        '00101100':',','00101101':'-','00101110':'.','00101111':'/',
        '00110000':'0','00110001':'1','00110010':'2','00110011':'3',
        '00110100':'4','00110101':'5','00110110':'6','00110111':'7',
        '00111000':'8','00111001':'9','00111010':':','00111011':';',
        '00111100':'<','00111101':'=','00111110':'>','00111111':'?',
        '01000000':'@','01000001':'A','01000010':'B','01000011':'C',
        '01000100':'D','01000101':'E','01000110':'F','01000111':'G',
        '01001000':'H','01001001':'I','01001010':'J','01001011':'K',
        '01001100':'L','01001101':'M','01001110':'N','01001111':'O',
        '01010000':'P','01010001':'Q','01010010':'R','01010011':'S',
        '01010100':'T','01010101':'U','01010110':'V','01010111':'W',
        '01011000':'X','01011001':'Y','01011010':'Z','01011011':'[',
        '01011101':']','01011110':'^','01011111':'_','01011100':"'\'",
        '01100000':'`','01100001':'a','01100010':'b','01100011':'c',
        '01100100':'d','01100101':'e','01100110':'f','01100111':'g',
        '01101000':'h','01101001':'i','01101010':'j','01101011':'k',
        '01101100':'l','01101101':'m','01101110':'n','01101111':'o',
        '01110000':'p','01110001':'q','01110010':'r','01110011':'s',
        '01110100':'t','01110101':'u','01110110':'v','01110111':'w',
        '01111000':'x','01111001':'y','01111010':'z','01111011':'{',
        '01111100':'|','01111101':'}','01111110':'~','01111111':'DEL'}        
    charac = ''
    for i in list(range(0,len(mydecode),8)):
        byte = mydecode[i:i+8]
        try:
            ASCIIex[byte]
        except KeyError:
            charac += '#'
        else:
            charac += ASCIIex[byte]
    
    ## Step3: To split long binary string into disered length (window size). 
    bytee = ''
    for ii in list(range(0,len(mydecode),20)):
        line = mydecode[ii:ii+20]
        bytee += line+('\n') 
    
    ## Step4: To write output into new text file.
    f = open('decode_DNA_to_Words.txt','w')
    f.write('Your input DNA sequence:'+'\n'+xx+'\n')
    f.write('The length of this DNA sequence is '+str(len(xx))+' bp. GC and AT content are '+str(GCcnt)+'% and '+str(ATcnt)+'%, respectively.\n\n')
    f.write('DNA sequence decoded to binary, '+str(len(mydecode))+' bits in total, is shown below:\n')
    f.write(bytee+'\n')
    f.write('Binary sequence decoded to characters based on the ASCII format is shown below:\n')
    f.write(charac+'\n')
    f.close()
    
    ## Step5: To print both outputs to user presented in jupyter nb.
    print ('The length of this DNA sequence is',len(xx),'bp. GC and AT content are',GCcnt,'% and',ATcnt,'%, respectively.\n')
    print ('DNA sequence decoded to binary,',(len(mydecode)),'bits in total, is shown below:\n'+bytee)
    print ('Binary sequence decoded to characters based on the ASCII format is shown below:\n'+charac+'\n')
    print ('Your output file is saved in the text file as "decode_DNA_to_Words.txt".')  


