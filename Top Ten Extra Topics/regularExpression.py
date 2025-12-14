import re
for term in ['I heard you on the wireless back in 52',
             'I heard you on the Wireless back in 52',
             'I heard you on the WIRELESS back in 52',]:
    
    result = re.search('[wW]ire', term)
    if result:
      loc = result.span()

      print('found a match between:', loc)
    else:
       print('No match found')
