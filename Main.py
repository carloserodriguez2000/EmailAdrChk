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
#
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
    if(len( domainS) >63):
        print('Domain part is longer than 63 chars')
        return False
    
    else:
        return True
    
################################################################################
#
def checkValidLocal(localS):
    #code
    print( localS + 'cheking')
################################################################################
#
def main ():

    sLine = input( 'Enter an Email address to check syntax: ')
    sLine = cleanS( sLine)
    domainS = GetDomain(sLine)
    localS = GetLocalS(sLine)

    print('Domain=\"%s\". Local= \"%s\".' %(domainS, localS)) 

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
