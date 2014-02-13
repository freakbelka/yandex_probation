# -*- coding: utf-8 -*-
import re

valid = (

    # hostname validation
    'freakbelka@gma2il.com',
    'freakbelka@gma1-il.com',
    'freakbelka@gf.mg',
    'freakbelka@gm_ail.com',
    'freakbelka@gm12ail.com',

    # username validation
    'frea_k1342.be-lka@gma2il.com',
    'freak"belka"@gma2il.com',
    'freak"b:elka!"@gma2il.com',
    'fre"a:"kb"!el:"ka@gmail.com'
    )

invalid = (

    # hostname validation
    'freakbelka@@gmail.com',
    'freakbelka@sd',
    'freakbelka@sdfs"dsd',
    'freakbelka@-gmail.com',
    'freakbelka@gm2ail-.com',
    'freakbelka@gm3ail.-com',
    'freakbelka@gmail.com-',
    'freakbelka@gm3ail.com.',

    # username validation
    'freak"belka@gma2il.com',
    'frealbel+ka@gma2il.com',
    '@gma2il.com',
    'freakb..elka@gma2il.com',
    'freak!belka@gma2il.com',
    'fre"a:"kb!"el:"ka@gmail.com'
    )  

# Функция проверки попадания символов '!,:' в парные двойные кавычки
def checkquote(name):
    if re.search(r'["!:,]', name):
        quotes = re.findall(r'["!:,]', name) 

        symbols = '' 
        flag = True
        lst = [] 

        # Преобразовываем список в строку
        for i in quotes:
            symbols += i

        # Создаем список индексов всех элементов строки, не являющихся символом "
        for i in range(len(quotes)):
            if quotes[i] != '"':
                lst.append(i)
        
        # Проверяем наличие нечетного количества кавычек перед и как минимум одной после каждого элемента строки
        for i in range(len(lst)):
            if len(re.findall(r'"', symbols[:lst[i]])) % 2 != 0 and symbols[lst[i]+1:].find(r'"') != -1:
                flag = flag and True
            else:
                flag = flag and False
        return not flag 
    else:
        return False

# Основная функция проверки e-mail на соответствие критериям
def emailcheck(name, domain):
    match_name = re.match(r'[a-z\d"\_\-\.\:\!\,]{1,128}$', name)
    match_domain = re.match(r'^[^\-\.@][a-z\d\_\-\.]{3,256}$', domain)

    # Проверка соответствия условию для имени
    if not match_name:
        return False
    elif  '..' in name or len(re.findall(r'"', name)) % 2 != 0 or checkquote(name):
        return False

    # Проверка соответствия условию для доменной части
    if not match_domain:
        return False
    elif '.-' in domain or '-.' in domain or domain.endswith('-') or domain.endswith('.'):
        return False
   
    return True

# Функция отделяет username от hostname и вызывает функцию для проверки валидности введеного e-mail
def splitting(email):
	name = email[0:email.find('@')]
	domain = email[email.find('@')+1:]
	print (email)

	if emailcheck(name,domain):
		print ("SUCCESS \n")
	else:
		print ("FAILED \n")

# Вызов функции для проверки валидных адресов
for email in valid:
    splitting(email)

# Вызов функции для проверки невалидных адресов
for email in invalid:
    splitting(email)
