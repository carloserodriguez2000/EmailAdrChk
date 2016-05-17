################################################################################
# hi. This program plays a game inspired by the TV show "BigBang Theory".
def cleanS ( string ):
    cleanS = string.strip()              # get read off Leading and training spaces.
    cleanS = cleanS.lower()
    return cleanS

################################################################################
# this cole be used also "str.partition(sep)"
################################################################################
def GetDomain(sLine):
    words = sLine.split()
    pieces = sLine.split('@')
    return (pieces[1])

################################################################################
#
def GetLocalS(sLine):
    words = sLine.split()
    pieces = sLine.split('@')
    return (pieces[0])

################################################################################
#
def checkValidDomain(domainS):
    if(len( domainS) >254):
        print('Domain part is longer than 254 chars')
        return False

    if (' ' in domainS):
        return False
    
    if ('-' in domainS):
        alphaNumDomS = domainS.split('-')
        domainS = alphaNumDomS[0]+alphaNumDomS[1]
    else :
        alphaNumDomS = domainS

    if ('.' in domainS):
        alphaNumDomS = domainS.split('.')
        domainS = alphaNumDomS[0]+alphaNumDomS[1]
    else :
        alphaNumDomS = domainS
       
    if( domainS.isalnum() == True):
        return True
    else:
        return False
    
################################################################################
#
def checkValidLocal(localS):
    if(len( localS) >64):
        print('Local part is longer than 64 chars')
        return False
    if ( not localS[0].isalpha()):
         print('First Digit is not alpha', localS)
         return False
    segments = localS.split('.')
    print ('Segments =', segments)
    return True

    
################################################################################
#
def main ():
    continueLoop = True
    while (continueLoop == True):
        sLine = input( 'Enter an Email address to check syntax: ')
        sLine = cleanS( sLine)
        if( len(sLine)>255):
            print("Address has %i chars. It is too long. max 256 total" %(len(sLIne)))
        
        domainS = GetDomain(sLine)
        localS = GetLocalS(sLine)

        print('Domain=\"%s\". Local= \"%s\".' %(domainS, localS))

        if (checkValidDomain(domainS) == True):
            print ('Domain \"%s\" is VALID' %(domainS))

        if( checkValidLocal(localS)== True):
            print( 'Local \"%s\" is VALID' % (localS))
            
        continueLoop = (input("Press 1 to run again: ") == '1')
    else :
        print("Thank you for Playing.  Bye.")
         
################################################################################
#
################################################################################
main()
