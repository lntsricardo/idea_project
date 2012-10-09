#!/usr/bin/python

from dao import * 

print('## INFO: Iniciando...')
id_user = input('User id: ')
print('## INFO: Salvando id_user')
user = input('Write yout name: ')
print('## INFO: Salvando user')
id_type = input('User type: (1-Adm, 2-Idea Creator, 3-Investor')
print('## INFO: Salvando id_type')

user_dao.insert_user(id_user, user, id_type)
