def hi():
	print('hi there')
	print('how are you?')

hi()
def hi(name):
	if name == 'ola':
		print('hi ola')
	elif name == 'sonja':
		print('hi sonja')
	else:
		print('hi anon')
hi('ola')
def hi(name):
	print('hi ' + name + '!')
hi("rachel")
girls = ['rachel', 'monica', 'phoebe', 'ola', 'you']
for name in girls:
	hi(name)
	print('next girl')
for i in range (1, 6):
	print(i)
	