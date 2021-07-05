import mysql.connector as mysql

bd = mysql.connect(host = 'localhost', user = 'root', passwd = '')
cursor = bd.cursor()

cursor.execute('CREATE DATABASE atividadeBD')

cursor.close()
bd.close()

bd = mysql.connect(host = 'localhost', user = 'root', passwd = '', database = 'atividadeBD')
cursor = bd.cursor()

cursor.execute('CREATE TABLE country(nomeCountry varchar(100) primary key, countryCode char(3))')
cursor.execute('CREATE TABLE city(id int not null auto_increment primary key, nome varchar(100), nomeCountry varchar(100), foreign key (nomeCountry) references country(nomeCountry))')
cursor.execute('CREATE TABLE countryLanguage(countryCode char(3) primary key, languageCountry varchar(50))')
cursor.execute('ALTER TABLE country ADD FOREIGN KEY (countryCode) REFERENCES countryLanguage(countryCode)')

insertCity = 'INSERT INTO city(nome, nomeCountry) VALUES(%s, %s)'
cityValues = [("São Paulo", "Brasil"), ("Camberra", "Austrália"), ("Washington DC", "Estados Unidos"), ("Copenhage", "Dinamarca"), ("Cairo", "Egito"), ("Buenos Aires", "Argentina"), ("Bruxelas", "Bélgica"), ("Berlim", "Alemanha"), ("Londres", "Inglaterra"), ("Madrid", "Espanha")]
insertCountry = 'INSERT INTO country(nomeCountry, countryCode) VALUES(%s, %s)'
countryValues = [("Brasil", "BRA"), ("Austrália", "AUS"), ("Estados Unidos", "EUA"), ("Dinamarca", "DEN"), ("Egito", "EGI"), ("Argentina", "ARG"), ("Bélgica", "BEL"), ("Alemanha", "ALE"), ("Inglaterra", "ING"), ("Espanha", "ESP"), ]
insertCountryLanguage = 'INSERT INTO countryLanguage(countryCode, languageCountry) VALUES(%s, %s)'
countryLanguageValues = [("BRA", "Português"), ("AUS", "Inglês"), ("EUA", "Inglês"), ("DEN", "Dinamarquês"), ("EGI", "Árabe"), ("ARG", "Espanhol"), ("BEL", "Neerlandesa"), ("ALE", "Alemão"), ("ING", "Inglês"), ("ESP", "Espanhol"), ]

cursor.executemany(insertCountryLanguage, countryLanguageValues)
cursor.executemany(insertCountry, countryValues)
cursor.executemany(insertCity, cityValues)


bd.commit()

consulta = 'SELECT city.id, country.nomeCountry, countrylanguage.countryCode, countryLanguage.languageCountry FROM city JOIN country ON country.nomeCountry = city.nomeCountry JOIN countryLanguage ON countrylanguage.countryCode = country.countryCode ORDER BY city.id'
cursor.execute(consulta)
registros = cursor.fetchall()

for reg in registros:
    print(reg)

cursor.close()
bd.close()