#Büşra Yaşar
'''
This program converts MCC/MNC codes of countries to PLMN coding.
Please use "mccmnc.txt" file as an input and get the converted result in
"out.txt"

'''

def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    # return string   
    return str1  

def convert(mccmnc):
    lenOfcountry = (len(mccmnc)-1)
    print(mccmnc,'length:',lenOfcountry )
    stra = str(mccmnc);
    newstr = [None]*6
    
    if lenOfcountry == 5: #convert 5 digit country code
        newstr[0] = stra[1]
        newstr[1] = stra[0]
        newstr[2] = 'F'
        newstr[3] = stra[2]
        newstr[4] = stra[4]
        newstr[5] = stra[3]
        
        print("PLMN coding :", listToString(newstr))
        text = listToString(newstr)
        return text
           
    elif lenOfcountry == 6: #convert 6 digit country code
        newstr[0] = stra[1]
        newstr[1] = stra[0]
        newstr[2] = stra[5]
        newstr[3] = stra[2]
        newstr[4] = stra[4]
        newstr[5] = stra[3]
    
        
        print("PLMN coding :",listToString(newstr))
        text = listToString(newstr)
        return text
    else:
        print("Wrong length! ")
def append_multiple_lines(file_name, lines_to_append):
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        appendEOL = False
        # Move read cursor to the start of file.
        file_object.seek(0)
        # Check if file is not empty
        data = file_object.read(100)
        if len(data) > 0:
            appendEOL = True
        # Iterate over each string in the list
        for line in lines_to_append:
            # If file is not empty then append '\n' before first line for
            # other lines always append '\n' before appending line
            if appendEOL == True:
                file_object.write("\n")
            else:
                appendEOL = True
            # Append element at the end of file
            file_object.write(line)          
  
def main():  
    try:

        fname = "mccmnc.txt"
        count = 0
        c = len(open("mccmnc.txt").readlines(  ))
        plmnList = ['']*c #number of country can be changed
        with open(fname, 'r') as f:
            for line in f:
                converted = convert(line)
                plmnList[count] = converted
                count += 1
        print("Total number of lines is:", count)
        #print(plmnList[1])
        #for i in count:
        append_multiple_lines("out.txt", plmnList )
       
    except FileNotFoundError:
        print("Dosya bulunamadı.")


if __name__ == '__main__':
    main()
