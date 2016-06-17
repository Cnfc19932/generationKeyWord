#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import re

class WordProperties(object):

	def  _remove_bad_char(self, text = ''):
		"""Удаление плохих символов"""

		if text != '':
			self.text = text
		k = re.findall(ur'(?u)\w+[-]*\w+',self.text.decode('utf-8'))
		self.text = " ".join(k)
		#print self.text
		
	def answer(self):
		"""Формируем ответ"""

		answer = {'geo' : self.find_propertie([u'geo']), 'person' : self.find_propertie([u'famn',u'persn',u'patrn']), 'abr' : self.find_propertie([u'abbr']), 'all': self.find_propertie([u'S'])}
		return answer

	def __init__(self, text = '', debug = False, inputFile = str(os.path.dirname(__file__)) + '/program/input.txt', outputFile = str(os.path.dirname(__file__)) + '/program/output.txt'):
		self.text = ''
		self.inputFile = inputFile 
		self.outputFile = outputFile 
		self.debug = debug
		self.result = {}

		if text != '':
			self.text = text

	def run(self):
		if self.text != '':
			self._remove_bad_char()
			f = open(self.inputFile, 'w')
			f.write(self.text.encode('utf-8'))
			f.close()

		jsonAnswer = '[]'
		file_text = open(self.inputFile, 'r')
		if not(file_text.read() == ''):

			answer = os.system(str(os.path.dirname(__file__)) + r'/program/mystem ' + self.inputFile + ' ' + self.outputFile + ' -i -d --eng-gr -l --format json') 
			if self.debug:
				print "Ok! self.text not empty"
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

				try:
					self.result = {(i['analysis'][0]['lex'] if len(i['analysis']) else i['text']):set(re.findall(r"[\w]+", (i['analysis'][0]['gr'] if len(i['analysis']) else ''))) for i in output} 
				except Exception:
					if self.debug:
						print "Error! Re modul error"
			#print self.result
		else:
			if self.debug:
				print "Warning! self.text empty"
		file_text.close()

	def find_propertie(self, propertie):
		"""Ищем слова с нужным свойством"""

		answerWordList = []
		for i in self.result:
			
			if (set(propertie) & self.result[i]) and len(i) > 2:
				answerWordList.append(i) 
				if self.debug:
					print set(propertie) & self.result[i], i
		if self.debug:
			print "Success! Find in method 'findAllPropertie'.Finded result " + str(len(answerWordList)) + " in " + str(len(self.result)) + ' words'

		return answerWordList

if __name__ == "__main__":
	pass