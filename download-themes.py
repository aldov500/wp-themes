from ast import parse
import glob
import re

# Receives a filepath and search for currencies 
def getCBLA(bloomberg_file):
    cbla_currencies = ['UYU']
     
    foutput = open("py_out.txt", "a")
    finput  = open(bloomberg_file, "r")
    
    foutput.write('################################################################\n')
    foutput.write(parseDate(bloomberg_file) + '\n')
    #foutput.write('################################################################\n')
    
    for brecord in finput:
        for currency in cbla_currencies:
            if brecord.find(currency)==0:
                #print(currency)
                foutput.write(parseRecord(brecord))
                #foutput.write(brecord)
            
    foutput.close()
    finput.close()

def parseDate(s):
    start = '_'
    end = '_'
    return s[s.find(start)+len(start):s.rfind(end)]

def parseRecord(brecord):
    pipe        = '|'
    currency    = brecord[0:3]
    index_bid   = 0
    px_bid      = 0
    index_bid   = brecord[0:].find(pipe) + 1
    px_bid      = brecord[index_bid:]
    #print("CUR : " + currency)
    #print("DAT : " + recursiveParse(brecord,0,px_bid,pipe,5))
    #print("BID : " + recursiveParse(brecord,0,px_bid,pipe,3))
    #print("ASK : " + recursiveParse(brecord,0,px_bid,pipe,4))
    #print("LAS : " + recursiveParse(brecord,0,px_bid,pipe,6))
    return currency + "\t" + recursiveParse(brecord,0,px_bid,pipe,3) + "\t" + recursiveParse(brecord,0,px_bid,pipe,4) + "\t" + recursiveParse(brecord,0,px_bid,pipe,6) + '\n'
    
def recursiveParse(bstring, index, px, bchar, times):
    if(times == -1):
        return px[0:len(px)-1]
    times   = times - 1
    bstring = bstring[index:]
    index   = bstring[0:].find(bchar) + 1
    px      = bstring[:index]
    return recursiveParse(bstring, index, px, bchar, times)

# Main
path_themes = "C:/Users/101324781/Desktop/themes-wp/table-links.txt"
content = open(path_themes, "r").read()

#list_files = content.read().split('<td class="download-product" data-title="Product">')

startwp     = '<td class="download-file" data-title="Download">'
endwp       = '" class="woocommerce-MyAccount-downloads-file button alt'
list_files  = content[content.find(startwp)+len(startwp):content.rfind(endwp)]

print(list_files)

for linkwp in list_files.split('<a href='):
    print('---------------------------------------------------------------------')
    print(linkwp)
    startws     = '<a href="'
    endws       = '" class="woocommerce-MyAccount-downloads'
    newfile     = linkwp[linkwp.find(startws)+len(startws):linkwp.rfind(endws)]
    print(newfile)
    #td_content = linkwp.split('<a href="')
    #for linktd in td_content:
    #    start = '<a href="'
    #    end = '</a>'
    #    s = linktd
    #    print (s[s.find(start)+len(start):s.rfind(end)])

    

