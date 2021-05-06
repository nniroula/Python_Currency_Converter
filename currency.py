"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Nabin Niroula
Date:   04/19/2021
"""

import introcs

APIKEY = 'kWOoUqiL9a2IJJ41Ee4BxfAZ7U6FM2qpCZf1VtM8v7Ae'

def before_space(s):
	"""
	Returns the substring of s up to, but not including, the first space.

	Example: before_space('Hello World') returns 'Hello'

	Parameter s: the string to slice
	Precondition: s is a string with at least one space in it
	"""
	assert type(s) == str, "Input must be a string"
# 	assert introcs.find_str(s, ' ') == True
	index = introcs.find_str(s, ' ')
	assert index >= 0
	before = s[0:index]
	return before

def after_space(s):
	"""
	Returns the substring of s after the first space

	Example: after_space('Hello World') returns 'World'

	Parameter s: the string to slice
	Precondition: s is a string with at least one space in it
	"""
	assert type(s) == str, "Invalide type"
# 	assert introcs.find_str(s, ' ') == True
	index = introcs.find_str(s, ' ')
	assert index >= 0
	after = s[index + 1:]
	return after

def first_inside_quotes(s):
	"""
	Returns the first substring of s between two (double) quote characters

	Note that the double quotes must be part of the string.  So "Hello World" is a
	precondition violation, since there are no double quotes inside the string.

	Example: first_inside_quotes('A "B C" D') returns 'B C'
	Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
	picks the first such substring.

	Parameter s: a string to search
	Precondition: s is a string with at least two (double) quote characters inside
	"""
	assert type(s) == str

	pos1 = introcs.find_str(s, '"')
	assert pos1 >= 0

	pos2 = introcs.find_str(s, '"', pos1 + 1)
	assert pos2 >= pos1 + 1

	return s[pos1+1: pos2]


def get_src(json):
	"""
	Returns the src value in the response to a currency query.

	Given a JSON string provided by the web service, this function returns the string
	inside string quotes (") immediately following the substring '"src"'. For example,
	if the json is

		'{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

	then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
	On the other hand if the json is

		'{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

	then this function returns the empty string.

	The web server does NOT specify the number of spaces after the colons. The JSON

		'{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

	is also valid (in addition to the examples above).

	Parameter json: a json string to parse
	Precondition: json a string provided by the web service (ONLY enforce the type)
	"""

	pos1 = introcs.find_str(json, '"')
	pos2 = introcs.find_str(json, '"', pos1 + 1)
	pos3 = introcs.find_str(json, '"', pos2 + 1)
	pos4 = introcs.find_str(json, '"', pos3 + 1)
	pos5 = introcs.find_str(json, '"', pos4 + 1)
	pos6 = introcs.find_str(json, '"', pos5 + 1)

	return json[pos5+1:pos6]

def get_dst(json):
	"""
	Returns the dst value in the response to a currency query.

	Given a JSON string provided by the web service, this function returns the string
	inside string quotes (") immediately following the substring '"dst"'. For example,
	if the json is

		'{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

	then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
	hand if the json is

		'{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

	then this function returns the empty string.

	The web server does NOT specify the number of spaces after the colons. The JSON

		'{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

	is also valid (in addition to the examples above).

	Parameter json: a json string to parse
	Precondition: json a string provided by the web service (ONLY enforce the type)
	"""

	pos1 = introcs.find_str(json, '"')
	pos2 = introcs.find_str(json, '"', pos1 + 1)
	pos3 = introcs.find_str(json, '"', pos2 + 1)
	pos4 = introcs.find_str(json, '"', pos3 + 1)
	pos5 = introcs.find_str(json, '"', pos4 + 1)
	pos6 = introcs.find_str(json, '"', pos5 + 1)
	pos7 = introcs.find_str(json, '"', pos6 + 1)
	pos8 = introcs.find_str(json, '"', pos7 + 1)
	pos9 = introcs.find_str(json, '"', pos8 + 1)
	pos10 = introcs.find_str(json, '"', pos9 + 1)

	return json[pos9+1:pos10]


def has_error(json):
	"""
	Returns True if the response to a currency query encountered an error.

	Given a JSON string provided by the web service, this function returns True if the
	query failed and there is an error message. For example, if the json is

		'{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

	then this function returns True (It does NOT return the error message
	'Source currency code is invalid'). On the other hand if the json is

		'{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

	then this function returns False.

	The web server does NOT specify the number of spaces after the colons. The JSON

		'{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

	is also valid (in addition to the examples above).

	Parameter json: a json string to parse
	Precondition: json a string provided by the web service (ONLY enforce the type)
	"""

	pos1 = introcs.find_str(json, '"')
	pos2 = introcs.find_str(json, '"', pos1 + 1)
	pos3 = introcs.find_str(json, '"', pos2 + 1)
	pos4 = introcs.find_str(json, '"', pos3 + 1)
	pos5 = introcs.find_str(json, '"', pos4 + 1)
	pos6 = introcs.find_str(json, '"', pos5 + 1)
	pos7 = introcs.find_str(json, '"', pos6 + 1)
	pos8 = introcs.find_str(json, '"', pos7 + 1)
	pos9 = introcs.find_str(json, '"', pos8 + 1)
	pos10 = introcs.find_str(json, '"', pos9 + 1)
	pos11 = introcs.find_str(json, '"', pos10 + 1)
	pos12 = introcs.find_str(json, '"', pos11 + 1)
	pos13 = introcs.find_str(json, '"', pos12 + 1)
	pos14 = introcs.find_str(json, '"', pos13 + 1)

	finalVal = len(json[pos13 + 1: pos14])
	return finalVal > 0


def service_response(src, dst, amt):
	"""
	Returns a JSON string that is a response to a currency query.

	A currency query converts amt money in currency src to the currency dst. The response
	should be a string of the form

		'{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

	where the values src-amount and dst-amount contain the value and name for the src
	and dst currencies, respectively. If the query is invalid, both src-amount and
	dst-amount will be empty, and the error message will not be empty.

	There may or may not be spaces after the colon.  To test this function, you should
	chose specific examples from your web browser.

	Parameter src: the currency on hand
	Precondition src is a nonempty string with only letters

	Parameter dst: the currency to convert to
	Precondition dst is a nonempty string with only letters

	Parameter amt: amount of currency to convert
	Precondition amt is a float or int
	"""
	assert type(src) == str
	assert len(src)> 0
	assert type(dst) == str
	assert len(dst) > 0
	assert type(amt) == float  #or assert type(amt) == int

	q = 'https://ecpyfac.ecornell.com/python/currency/fixed?src=src&dst=dst&amt=amt&key=kWOoUqiL9a2IJJ41Ee4BxfAZ7U6FM2qpCZf1VtM8v7Ae'
	readval = introcs.urlread(q)
	return readval

def iscurrency(currency):
	"""
	Returns True if currency is a valid (3 letter code for a) currency.

	It returns False otherwise.

	Parameter currency: the currency code to verify
	Precondition: currency is a nonempty string with only letters
	"""

	assert type(currency) == str
# 	assert len(currency) > 0
	var1 = len(currency)
	var3 = service_response(currency, currency ,0 ) # returns json string
	var4 = has_error(var3)
	var2 = 3
# 	return var1 and var2 and var3
	return var1 and not var4 and var2

def exchange(src, dst, amt):
	"""
	Returns the amount of currency received in the given exchange.

	In this exchange, the user is changing amt money in currency src to the currency
	dst. The value returned represents the amount in currency currency_to.

	The value returned has type float.

	Parameter src: the currency on hand
	Precondition src is a string for a valid currency code

	Parameter dst: the currency to convert to
	Precondition dst is a string for a valid currency code

	Parameter amt: amount of currency to convert
	Precondition amt is a float or int
	"""
	assert type(src) == str
	assert type(dst) == str
	assert type(amt) == float
