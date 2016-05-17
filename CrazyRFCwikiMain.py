################################################################################
# hi. This program plays a game inspired by the TV show "BigBang Theory".
def cleanS ( string ):
    cleanS = string.strip()              # get read off Leading and training spaces.
    cleanS = cleanS.lower()
    return cleanS

################################################################################
#
def stripComment ( sLine):
   # code
    print( sLine + 'cheking')    
    
################################################################################
# this cole be used also "str.partition(sep)"
def GetDomain(sLine):
    # code
##    print( sLine + 'cheking')
    words = sLine.split()
    pieces = sLine.split('@')
##    print(pieces[1])
 
    return (pieces[1])

################################################################################
#
def GetLocalS(sLine):
    # code
##    print( sLine + 'cheking')
    words = sLine.split()
    pieces = sLine.split('@')
##    print(pieces[0])
    return (pieces[0])
################################################################################
#
def checkValidDomain(domainS):
    # code
    print( domainS + 'cheking')
    if(len( domainS) >254):
        print('Domain part is longer than 254 chars')
        return False

    if (' ' in domainS):
        ##print('domain has space')
        return False
    
    if ('-' in domainS):
        #alphaNumDomS = domainS.lstrip('-')
        alphaNumDomS = domainS.split('-')
        ##print(alphaNumDomS)
        ##print(len(alphaNumDomS))
        domainS = alphaNumDomS[0]+alphaNumDomS[1]
        ##print('domain has -\"%s\"' %(domainS) )              # a dot is ok but need more
    else :
        alphaNumDomS = domainS

    if ('.' in domainS):
        #alphaNumDomS = domainS.lstrip('.')
        alphaNumDomS = domainS.split('.')
        ##print(alphaNumDomS)
        ##print(len(alphaNumDomS))
        domainS = alphaNumDomS[0]+alphaNumDomS[1]
        ##print('domain has .\"%s\"' %(domainS) )              # a dot is ok but need more
    else :
        alphaNumDomS = domainS

    print(domainS)        
    if( domainS.isalnum() == True):
        ##print('domain is alphanum')
        return True
    else:
        ##print('missing alphanum')
        return False


    # check for IP based domains
##    if ((domainS.startswith('[') and domainS.endswith(']'))):
###################
##        octets = domainS.strip('[]')
##        print ( octets )
##        numbers = octets.split(':')
##        print ( numbers )
##        if( numbers[0].isnumerid() and numbers[1].isnumeric):
##            return True
###################
    
    
        

        
    
################################################################################
#
def checkValidLocal(localS):
    #code
    print( localS + 'cheking')
    if(len( localS) >64):
        print('Local part is longer than 64 chars')
        return False
    if ( localS[0] == '.'):
        return False
    
## Check for dot and the beginning or concecutive dots
    last =''  # initialinze as a empty
    for letter in localS :
        if (letter == last):
            print ('concecutive dots found')
            return False        ## if it finds consecutive ".." then not valid
        if letter == '.':
            last = '.'          ## find the first dot and hold it.
##################################################################################
## Check for "(zero or more characters)" matching and take it out
    r=localS.split('(')
    if r[0] =='' :
        #Found leading comment
        print("Leading(found")
        r=r[1]
        s= r.split(')') # s contains everyting inside the parens.
        print('for: r=',r, 's=',s )
        if s[0] =='' :
            #Found closing parens. let see if the stuff in the parens is valid
            valid = True
            for validL in ['"(),:;<>@[\] ']:
                if not(validL in s[1]):
                    valid = False
                    print('invalid \"%s\" ' %(validL))
            print ('End For ',s[0], ' ', s[1])
            if ( validL == True ):
                print('valid local () ',s[1])
#######################################################################
    ##print('Original \"%s\". r=\"%s\". s=\"%s\"' (localS, r, s))
    print('Original= ', localS,  'r= ', r)
    
##    if (' ' in localS):
##        print('localS has space')
##        return False
##    
##    if ('-' in localS):
##        #alphaNumDomS = domainS.lstrip('-')
##        alphaNumDomS = localS.split('-')
##        print(alphaNumDomS)
##        print(len(alphaNumDomS))
##        localS = alphaNumDomS[0]+alphaNumDomS[1]
##        print('domain has -\"%s\"' %(domainS) )              # a dot is ok but need more
##    else :
##        alphaNumDomS = localS
##
##    if ('.' in localS):
##        #alphaNumDomS = domainS.lstrip('.')
##        alphaNumDomS = localS.split('.')
##        print(alphaNumDomS)
##        print(len(alphaNumDomS))
##        localS = alphaNumDomS[0]+alphaNumDomS[1]
##        print('domain has .\"%s\"' %(localS) )              # a dot is ok but need more
##    else :
##        alphaNumDomS = localS
##
##    print(localS)        
##    if( localS.isalnum() == True):
##        print('domain is alphanum')
##        return True
##    else:
##        print('missing alphanum')
##        return False

    
################################################################################
#
def main ():

    sLine = input( 'Enter an Email address to check syntax: ')
    sLine = cleanS( sLine)
    if( len(sLine)>255):
        print("Address has %i chars. It is too long. max 256 total" %(len(sLIne)))
        
    
    domainS = GetDomain(sLine)
    localS = GetLocalS(sLine)

    print('Domain=\"%s\". Local= \"%s\".' %(domainS, localS))

    if (checkValidDomain(domainS) == True):
        print ('valid domain')

    if( checkValidLocal(localS)== True):
        print( 'Local \"%s\" is VALID' % (localS))
     
##    if( checkValidDomain(domainS)== False):
##        print( 'Domain \"%s\" is NOT-VALID' % (domainS))
##    else :
##        print( 'Domain \"%s\" is NOT-VALID' % (domainS))
##
##    if( checkValidLocal(localS)== False):
##        print( 'Local \"%s\" is NOT-VALID' % (localS))
##    else :
##        print( 'Local \"%s\" is NOT-VALID' % (localS))
##
##
##    indexer = list()
##    sLen = len(sLine)
##    indexer = range(sLen)     #Create an array for 0:len(
##    sReverse = list()
##    sReverseLine = ''
##    
##    for index in indexer :
##        ##print ((sLen-1)-index)
##        sReverse.append( sLine[(sLen-1)-index])
##        sReverseLine +=  sReverse[index]
##        ##print(index)
##
##    print(sLine)
##    print(sReverse)
##    print(sReverseLine)
##    if( sLine == sReverseLine):
##        print( 'String \"%s\" is a palindrome' %(sLine))
##
################################################################################
#
################################################################################
main()
