##Installation
	git clone https://github.com/Cnfc19932/generationKeyWord.git

##Example
	a = WordProperties(text = 'Обама и Путин приехали в СССР для саммита в Лондоне')
	a.run()
	print a.answer()
###Answer
	{'person': [u'путин', u'путин'], 'abr': [u'ссср'], 'geo': [u'лондон', u'ссср'], 'all': [u'саммит', u'путин', u'лондон', u'ссср', u'обама']}