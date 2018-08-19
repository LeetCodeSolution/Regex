import re

email = 'cqc@cuiqingcai.com'
pattern = re.compile('\w+@\w+\.\w+')
result = re.match(pattern, email)
print(result)
print(result.group())