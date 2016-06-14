#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import generation_key_word as m


class testWordProperties(unittest.TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_geo_find(self):
		data = {
			'Москва':u'москва',
			'Новосибирск':u'новосибирск',
			'В киеве':u'киев',
			'Госсовет Крыма выделил 226,5 млн руб. на переселение семей из зоны Керченского моста' : u'крым',
			'Задержан мэр Горно-Алтайска ему предъявлено обвинение мошенничестве превышении полномочий' : u'горно-алтайск'
		}

		data_two_or_more = {
			'Из Киева в Германию' : [u'германия',u'киев'],
			'Россия перестала получать с Украины жизненно важный препарат мезатон' : [u'россия',u'украина']
		}
		for i in data:
			k = m.WordProperties(text = i)
			k.run()
			self.assertEqual(data[i], k.find_propertie([u'geo'])[0]) 

		for i in data_two_or_more:
			k = m.WordProperties(text = i)
			k.run()
			self.assertEqual(set(data_two_or_more[i]), set(k.find_propertie([u'geo']))) 

	def test_famn_find(self):
		data = {'Путин' : u'путин',
				'Владимирович' : u'владимирович',
				'Попов' : u'попов',
				'Обама' : u'обама',
				'Мухамед' : u'мухамед'}

		data_two_or_more = {
			'Мухамед Али прилетел к Ангеле Меркель' : [u'мухамед',u'меркель']
		}

		for i in data:
			k = m.WordProperties(text = i)
			k.run()
			self.assertEqual(data[i], k.find_propertie([u'famn',u'persn',u'patrn'])[0]) 


		for i in data_two_or_more:
			k = m.WordProperties(text = i)
			k.run()
			self.assertEqual(set(data_two_or_more[i]), set(k.find_propertie([u'famn',u'persn',u'patrn']))) 

	def test_abbr_find(self):
		data = {'РСДРП': u'рсдрп',
				'СССР': u'ссср',
				'КХЛ' : u'кхл'
		}

		data_two_or_more = {
			'Председатель СССР прилетел в США' : [u'ссср',u'сша'],
			'КГБ и ФСБ' : [u'кгб',u'фсб']
		}

		for i in data:
			k = m.WordProperties(text = i)
			k.run()
			self.assertEqual(data[i], k.find_propertie([u'abbr'])[0]) 		

		for i in data_two_or_more:
			k = m.WordProperties(text = i)
			k.run()
			self.assertEqual(set(data_two_or_more[i]), set(k.find_propertie([u'abbr']))) 

	def test_WordProperties(self):
		data = {
			'Путин' : {'person': [u'путин'], 'abr': [], 'geo': [], 'all': [u'путин']},
			'Париж столица Франции' : {'person': [], 'abr': [], 'geo': [u'париж',u'франция'], 'all': [u'париж',u'франция',u'столица']},
			'Владимир Владимирович Путин прибыл в Париж в сзязи с апокалипсисом' : {'person': [u'\u0432\u043b\u0430\u0434\u0438\u043c\u0438\u0440', u'\u043f\u0443\u0442\u0438\u043d', u'\u0432\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447'], 'abr': [], 'geo': [u'\u043f\u0430\u0440\u0438\u0436'], 'all': [u'\u0432\u043b\u0430\u0434\u0438\u043c\u0438\u0440', u'\u0430\u043f\u043e\u043a\u0430\u043b\u0438\u043f\u0441\u0438\u0441', u'\u043f\u0443\u0442\u0438\u043d', u'\u0432\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447', u'\u043f\u0430\u0440\u0438\u0436', u'\u0441\u0437\u044f\u0437\u0438']}
		}

		for i in data:
			k = m.WordProperties(text = i)
			k.run()
			self.assertEqual(set(data[i]), set(k.answer())) 		

