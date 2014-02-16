# -*- coding: utf-8 -*-
# Модуль проверки валидности e-mail
import re

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

# Функция отделяет username от hostname
def splitting(email):
    name = email[0:email.find('@')]
    domain = email[email.find('@')+1:]
    return name, domain

# Основная функция проверки e-mail на соответствие критериям
def emailcheck(email):
    name, domain = splitting(email)
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



