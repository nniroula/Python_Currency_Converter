"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Nabin Niroula
Date:   04/19/2021
"""

import introcs
import currency

def test_before_space():
	"""Test procedure for before_space"""
	print("Testing before_space")
	testCase1 = currency.before_space("hello world")
	introcs.assert_equals("hello", testCase1)

	testCase2 = currency.before_space(" My name")
	introcs.assert_equals("", testCase2)

	testCase3 = currency.before_space("  ")
	introcs.assert_equals("", testCase3)

	testCase4 = currency.before_space(" (((123abacyou")
	introcs.assert_equals("", testCase4)

def test_after_space():
	"""Test procedure for after_space"""
	print("Testing after_space")
	testCase1 = currency.after_space(" ")
	introcs.assert_equals("", testCase1)

	testCase2 = currency.after_space("hello world")
	introcs.assert_equals("world", testCase2)

	testCase3 = currency.after_space(" My name is ")
	introcs.assert_equals("My name is ", testCase3)

	testCase4 = currency.after_space("ok  ")
	introcs.assert_equals(" ", testCase4)

def test_first_inside_quotes():
	"""Test procedure for first_inside_quotes"""
	print("Testing first_inside_quotes")

	case1 = currency.first_inside_quotes('a"bc"d')
	introcs.assert_equals("bc", case1)

	case2 = currency.first_inside_quotes('123"4"56 "78" 9')
	introcs.assert_equals("4", case2)

	case3 = currency.first_inside_quotes(' "" ')
	introcs.assert_equals("", case3)

	case4 = currency.first_inside_quotes("\"OK\"")
	introcs.assert_equals("OK", case4)

def test_get_src():
	"""Test procedure for get_src"""
	print("Testing get_src")

	case1 = currency.get_src('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
	introcs.assert_equals('2 United States Dollars', case1)

	case2 = currency.get_src('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
	introcs.assert_equals("", case2)

	case3 = currency.get_src('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
	introcs.assert_equals('2 United States Dollars' , case3)

	case4 = currency.get_src('{"success": false, "src": "", "dst": "", "error": "Source currency code is invalid."}')
	introcs.assert_equals("", case4)


def test_get_dst():
	"""Test procedure for get_dst"""
	print("Testing get_dst")

	case1 = currency.get_dst('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
	introcs.assert_equals('1.772814 Euros', case1)

	case2 = currency.get_dst('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
	introcs.assert_equals("", case2)

	case3 = currency.get_dst('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
	introcs.assert_equals('1.772814 Euros', case3)

	case4 = currency.get_dst('{"success": false, "src": "", "dst": "", "error": "Source currency code is invalid."}')
	introcs.assert_equals("", case4)

def test_has_error():
	"""Test procedure for has_error"""
	print("Testing has_error")

	case1 = currency.has_error('{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}')
	introcs.assert_equals(True , case1)

	case2 = currency.has_error('{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}')
	introcs.assert_equals(False, case2)

	case3 = currency.has_error('{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}')
	introcs.assert_equals(False, case3)

	case4 = currency.has_error('{"success": true, "src": "", "dst": "", "error": "Invalid dst currency value."}')
	introcs.assert_equals(True, case4)


def test_service_response():
	"""Test procedure for service_response"""
	print("Testing service_response")

	case1 = currency.service_response('USD', 'EUR', 2.5)
	introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", "dst": "2.2160175 Euros", "error": ""}', case1)

	case2 = currency.service_response('US', 'EUR', 2.5)
	introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency US is not present."}', case2)

	case3 = currency.service_response('USD', 'EU', 2)
	introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency EU is not present."}', case3)

	case4 = currency.service_response('USD', 'EUR', -5.0)
	introcs.assert_equals('{"success": true, "src": "-5.0 United States Dollars", "dst": "-4.432035 Euros", "error": ""}', case4)

def test_iscurrency():
	"""Test procedure for iscurrency"""
	print("Testing iscurrency")

	case1 = currency.iscurrency("USD")
	introcs.assert_equals(True, case1)

	case2 = currency.iscurrency("AB")
	introcs.assert_equals(False, case2)

def test_exchange():
	"""Test procedure for exchange"""
	print("Testing exchange")

	case1 = currency.exchange('USD', 'EUR', 2)
	introcs.assert_floats_equal(1.772814, case1)

	case2 = currency.exchange('USD', 'EUR', -2)
	introcs.assert_floats_equal(-1.772814, case2)

#script to call all test functions
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print('All tests completed successfully.')
