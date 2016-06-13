import os
import json
import re

class WordProperties(object):

	def __init__(self, debug = False, inputFile = 'program/input.txt', outputFile = 'program/output.txt'):
		self.inputFile = inputFile 
		self.outputFile = outputFile 
		self.debug = debug
		self.result = {}
		self._run()


	def  _run(self):
		jsonAnswer = '[]'
		answer = os.system(r'program/mystem ' + self.inputFile + ' ' + self.outputFile + ' -i -d --eng-gr -l --format json') 
		if self.debug:
			if not(answer == 0):
				print "Error! Mystem answer " + str(answer)
			else:
				print "Success! Mystem success"
		if (answer == 0):
			try: 
				jsonAnswer = open(self.outputFile, 'r').read()
			except FileNotFoundError:
				if self.debug:
					print "Error! File " + self.outputFile + " not found"
			output = json.loads(jsonAnswer)

			#print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++==="
			#for i in output:
			#	print (i['analysis'][0]['lex'] if len(i['analysis']) else '')
			#print "_______________________________________________________________"

			try:
				self.result = {(i['analysis'][0]['lex'] if len(i['analysis']) else i['text']):set(re.findall(r"[\w]+", (i['analysis'][0]['gr'] if len(i['analysis']) else ''))) for i in output} #Magic
			except Exception:
				if self.debug:
					print "Error! Re modul error"
		#print self.result

	def findAllPropertie(self, propertie):
		answerWordList = {}
		for i in self.result:
			#print set(propertie),self.result[i]
			if (set(propertie) & self.result[i]) and len(i) > 2:
				answerWordList[i] = self.result[i]
				if self.debug:
					print set(propertie) & self.result[i], i
		if self.debug:
			print "Success! Find in method 'findAllPropertie'.Finded result " + str(len(answerWordList)) + " in " + str(len(self.result)) + ' words'
		return answerWordList

	def findPropertiesOr(self, properties):
		properties = set(properties)
		answerWordList = {}
		for i in self.result:
			if (properties & self.result[i]) and len(i) > 2:
				answerWordList[i] = self.result[i]
				if self.debug:
					print properties & self.result[i], i
		if self.debug:
			print "Success! Find in method 'findPropertiesOr'.Finded result " + str(len(answerWordList)) + " in " + str(len(self.result)) + ' words'
		return answerWordList






	

a = WordProperties(debug = False)
k = a.findPropertiesOr(['geo','persn','famn','abbr','patrn'])

for i in k:
	print i
print "++++++++++++++++++++++=="

k = a.findAllPropertie(['geo'])

for i in k:
	print i
