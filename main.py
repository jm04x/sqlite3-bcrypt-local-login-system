import bcrypt as b
import sqlite3 as sql

# Establish db connection and create table to store user info.
con = sql.connect('users.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS user (
	username TEXT,
	password TEXT)''')


def store_account(username, hashed_password):
	cur.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, hashed_password))
	con.commit()

	return


def hash_pass(password):
	password = password.encode('utf8')
	hashed_password = b.hashpw(password, b.gensalt())
	
	return hashed_password


def register():
	username = input('Username: ')
	while len(username) < 1:
		print('[!] Username must be 1 character or longer.')
		username = input('Username: ')
	password = input('Password: ')
	while len(password) < 3:
		print('[!] Password must be 3 character or longer.')
		password = input('Password: ')

	hashed_password = hash_pass(password)

	store_account(username, hashed_password)
	
	print('Account registered.')
	return main()


def main():
	# Main menu for program.
	print('Welcome. Please select an option below:')
	print('1. Register')
	print('2. Login')
	choice = input(': ')

	match choice:
		case '1':
			return register()
		case '2':
			return login()



if __name__ == '__main__':
	main()