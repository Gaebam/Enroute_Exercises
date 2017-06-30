from urllib.parse import quote
from urllib.request import urlopen
import json
import mysql.connector
import sshtunnel

_host = 'irock.enroute.xyz'
_ssh_port = 22
_username = 'mquiroga'
_password = 'm4rc0Qu1r0g4!'
_remote_bind_address = 'localhost'
_local_mysql_port = 9990
_local_bind_address = '127.0.0.1'
_remote_mysql_port = 3306
_db_user = 'mquiroga'
_db_password = 'm4rc0Qu1r0g4!'
_db_name = 'aquiroga'

def log_request(mm: str, mn: str, mx: str) -> None:
	_SQL = """INSERT INTO results_api (address, lat, lng) values (%s, %s, %s)"""
	with sshtunnel.SSHTunnelForwarder(
	        (_host, _ssh_port),
	        ssh_username=_username,
	        ssh_password=_password,
	        remote_bind_address=(_remote_bind_address, _remote_mysql_port),
	        local_bind_address=(_local_bind_address, _local_mysql_port)
	) as tunnel:
	    conn = mysql.connector.connect(
	        user=_db_user,
	        password=_db_password,
	        host=_local_bind_address,
	        database=_db_name,
	        port=_local_mysql_port)

	    cursor = conn.cursor()
	    cursor.execute(_SQL, (mm,
							  mn,
							  mx, ))
	    conn.commit()
	    cursor.close()
	    conn.close()

def log_request_error(i: str, sts: str) -> None:
	_SQL = """INSERT INTO error_api (address, status) values (%s, %s)"""
	with sshtunnel.SSHTunnelForwarder(
	        (_host, _ssh_port),
	        ssh_username=_username,
	        ssh_password=_password,
	        remote_bind_address=(_remote_bind_address, _remote_mysql_port),
	        local_bind_address=(_local_bind_address, _local_mysql_port)
	) as tunnel:
	    conn = mysql.connector.connect(
	        user=_db_user,
	        password=_db_password,
	        host=_local_bind_address,
	        database=_db_name,
	        port=_local_mysql_port)

	    cursor = conn.cursor()
	    cursor.execute(_SQL, (i,
							  sts, ))
	    conn.commit()
	    cursor.close()
	    conn.close()

service = 'geocode'
output = 'json'
parameter = 'address'

with open('addr.txt') as adds:
	for i in adds:
		add = quote(i)
		p_url = ('https://maps.googleapis.com/maps/api/'+ service +'/' + output + '?'+ parameter + '=' + add)
		open_url = urlopen(p_url)
		resp_url = open_url.read().decode('utf-8')

		json_url=json.JSONDecoder().decode(resp_url)

		if json_url['status'] != 'ZERO_RESULTS':
			mm = json_url['results'][0]['formatted_address']
			mn = json_url['results'][0]['geometry']['location']['lat']
			mx = json_url['results'][0]['geometry']['location']['lng']
			print(mm)
			print(mn)
			print(mx)
			print('')
			archivo = open('results.txt','a')
			print(mm, file=archivo)
			print(mn, file=archivo)
			print(mx, file=archivo)
			print('', file=archivo)
			archivo.close()
			log_request(mm,mn,mx)
			
		else:
			sts = json_url['status']
			archivo2 = open('errores.txt','a')
			print(i, file=archivo2)
			print(sts, file=archivo2)
			archivo2.close()
			log_request_error(i, sts)




