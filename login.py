import bcrypt as b
import sqlite3 as sql

# Establish db connection and create table to store user info.
try:
	con = sql.connect('users.db')
	cur = con.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS user (
		username TEXT,
		hashed_password TEXT)''')
except:
	raise Exception('[!] Database creation failed.')


def store_account(username, hashed_password):
	cur.execute("INSERT INTO user (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
	con.commit()

	return


def hash_pass(password):
	hashed_password = b.hashpw(password.encode('utf8'), b.gensalt())
	
	return hashed_password


def check_password(password, username):
	cur.execute('SELECT hashed_password FROM user WHERE username = ?', (username,))
	result = cur.fetchone()[0]
	if b.checkpw(password.encode('utf-8'), result):
		return True
	else:
		return False
	

def check_exists(username):
	cur.execute('SELECT COUNT(*) FROM user WHERE username = ?', (username,))
	occurences = cur.fetchone()[0]
	if occurences == 0:
		return False
	else:
		return True


def register():
	while True:
		username = input('Username: ')
		if len(username) < 1:
			print('[!] Username must be 1 character or longer.')
		elif check_exists(username) == True:
			print('[!] Username already exists.')
		else:
			break
	
	while True:
		password = input('Password: ')
		if len(password) < 3:
			print('[!] Password must be 3 character or longer.')
		else:
			break		

	hashed_password = hash_pass(password)
	store_account(username, hashed_password)
	print('Account registered.')

	return 


def login():
	while True:
		username = input('Username: ')
		if check_exists(username) == False:
			print('[!] Account does not exists. Please register or sign in with a created account.')
		else:
			break
	
	while True:
		password = input('Password: ')
		if check_password(password, username) == False:
			print('[!] The password you have entered is incorrect. Please try again.')
		else:
			print('Logged in!')
			break
			

def main():
	while True:
		print('Welcome. Please select an option below:')
		print('1. Register')
		print('2. Login')
		choice = input(': ')

		match choice:
			case '1':
				register()
			case '2':
				login()


if __name__ == '__main__':
	main()