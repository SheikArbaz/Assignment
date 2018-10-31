failed=[]
import pip
import os

def install(package):
	'''
	package: package name to be installed!
	returns code(0/1) for installed/failed
	'''
	if hasattr(pip, 'main'):
		return pip.main(['install', package])
	else:
		return pip._internal.main(['install', package])
def inst_(tokens):
	'''
	tokens: List of packages to be installed
	returns code(0/1) for all installed/ all not installed
	'''
	global failed
	import pip
	retcode = 0
	for line in tokens:
		pipcode = install(line.strip())
		# print ('hurrah!',line.strip(), pipcode)
		if pipcode==1:
			failed.append(line.strip())
		retcode = retcode or pipcode
	return retcode


file = open('dependencies.json','r')
text = ''
for i in file:
	text=text+i.strip()+' '
text = text.replace(',','').replace('{','').replace('}','')
raw_tokens = text.split()

tokens=[]
for i in raw_tokens:
	if i.lower()!='dependencies' and i!='=':
		tokens.append(i)
# for i in file:
# 	i=i.strip()
# 	print ('a:',i)
# 	if i!='{' and i!='}' and i.lower()!='dependencies':
# 		if i.endswith(','):
# 			i = i[:-1]
# 			tokens.append(i)

print(len(tokens), tokens)
result = inst_(tokens)
if result == 0:
	print('Success')
else:
	for i in failed:
		print (i)

