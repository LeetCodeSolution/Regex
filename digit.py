digit = {}
digit[1] = '+100'
digit[2] = '5e2'
digit[3] = '-123'
digit[4] = '3.1416'
digit[5] = '-1E-16'

digit[6] = '12e'
digit[7] = '1a3.14'
digit[8] = '1.2.3'
digit[9] = '+-5'
digit[10] = '12e+5.4'

import re

pattern = re.compile('^(?:\+|\-)?(?:\d+)(?:\.\d+)?(?:(?:e|E)(?:\-|\+)?\d+)?$')

for item in digit.values():
    match_result = re.match(pattern, item)
    result = 'Yes' if match_result else 'No'
    print(item, result, match_result.group() if match_result else None)
