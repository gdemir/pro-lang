#!/usr/bin/python
#-*- coding:utf-8 -*-

global token, i, error

def token_split(string):
	global token

	exp = "+-*)(/"
	ws = " \t\r\n"
	j = 0
	token_list = []
	temp = ""
	for char in string:
		if char in exp:
			if temp: token_list.append(temp)
			token_list.append(char)
			temp = ""
		elif not char in ws:
			temp = temp + char
	if temp: token_list.append(temp)
	return token_list

def is_digit(string):
	for char in string:
		if char == '.': continue
		if not ord('0') <= ord(char) and ord(char) <= ord('9'):
			return False
	return True

def match(expectedToken):
	global token, i, error

	if token[i] != expectedToken:
		error = "İşleç Hatası"
		return False
	i = i + 1


def main(TOKEN):
	global token, i, error

	i = 0
	token = token_split(TOKEN)
	result = exp()
	if result:
		return result
	else:
		return error


def exp():
	global token, i, error
	
	temp = term()
	if not temp:
		return False

	if i < len(token):
		if ( token[i] == '+'):
			match('+')
			tmp = term()
			if not tmp: return False
			temp =  temp + tmp
		elif ( token[i] == '-'):
			match('-')
			tmp = term()
			if not tmp: return False
			temp =  temp - tmp
	return temp

def term():
	global token, i, error
	
	temp = factor()
	
	if i < len(token):
		if ( token[i] == '*'):
			match('*')
			temp = temp * factor()
		elif ( token[i] == '/'):
			match('/')
			tmp = factor()
			if tmp != 0: temp = temp / tmp
			else:
				error = "Sıfır'a bölüm tanımsızdır!"
				return False
	return temp

def factor():
	global token, i, error

	temp = None
	if i < len(token):
		if ( token[i] == '('):
			match('(')
			temp = exp()
			match(')')
		elif is_digit(token[i]):
			temp = float(token[i])
			i = i + 1
		else:
			error = "Sayı yerine işleç girdiniz!"
			return False
	if temp == None:
		error = "Karakter giriniz!"
		return False
	else: return temp
