from osint_sources.model import create_tables
from osint_sources.scraper import *
import sys, getopt
import argparse

def banner():
    print(r"""
	------------------------------------------
	|           ExposingIdentities            |
	|					  |
	| Authors: Ruth Gonzalez (@RuthGnz)       |
	|	   Miguel Hernandez (@MiguelHzBz) |
	| Version: 1.0                            |
	|					  |
	|                                         |
	------------------------------------------
	USAGE:
		python3 main.py [options]
		python3 -t -k <token>
		python3 -g -n "<name surname>"
		python3 -g -n "<name surname>" -i <imagePath>
		python3 -t -n "<name surname>" -s <number of twitter pages to search>
    """)

def getArguments(args):

	arguments={}
	parser = argparse.ArgumentParser(description='EI - This tool scrapping social media to get information from a target')
	parser.add_argument('-t','--tinder',dest='tinder', action='store_true', help='Insert this option to scrapper tinder database')
	parser.add_argument('-k','--token',dest='token', help='If you choose tinder option, provide a valid token')
	parser.add_argument('-w','--twitter',dest='twitter',action='store_true', help='Insert this option to scrapper Twitter')
	parser.add_argument('-g','--google',dest='google', action='store_true', help='Insert this option to scrapper google.')
	parser.add_argument('-f','--facebook',dest='facebook', action='store_true', help='Insert this option to scrapper google.')
	parser.add_argument('-n','--name',dest='name', help='Name of person you like to search.')
	parser.add_argument("-p",'--place',dest='place', help="Location you like to search")
	parser.add_argument("-i",'--image',dest='image', help="Image you like to search")
	parser.add_argument("-s",'--size',dest='size', help="Limit for searches")
	args = parser.parse_args()
	
	if not args.tinder and not args.google and not args.facebook and not args.twitter:
		print ("--------------")
		print ("Error in input arguments: ")
		print ("Need one type of input, -t/--tinder -g/--google -w/--twitter or -f/--facebook")
		print ("--------------")
		parser.print_help()
		sys.exit(-1)
	if args.tinder:
		if not args.token:
			print ("--------------")
			print ("Tinder token must be provided")
			print ("--------------")
			parser.print_help()
			sys.exit(-1)
		else:
			print ("Starting Tinder scrapper...")
			tinder(args.token)

	if args.google:
		if not args.name:
			print ("--------------")
			print ("Name must be provided")
			print ("--------------")
			parser.print_help()
			sys.exit(-1)
		else:
			if not args.place:
				args.place=''
			print ("Starting Google scrapper...")
			google(args.name,args.place,args.image)

	if args.twitter:
		if not args.name:
			print ("--------------")
			print ("Name must be provided")
			print ("--------------")
		elif not args.size:
			print ("--------------")
			print ("Size must be provided")
			print ("--------------")
		else:
			print ("Starting twitter scrapper...")
			twitter_scrapper(args.name,args.size)

	if args.facebook:
		if not args.name:					
			print ("--------------")
			print ("Name must be provided")
			print ("--------------")
		else:
			print ("Starting twitter scrapper...")
			facebook_scrapper(args.name)					
	return args


def main(argv):
	#tinder()
	#google_scrapper()
	banner()
	args = getArguments(argv)
	print (args)
	
if __name__ == '__main__':
	#create_tables()
	main(sys.argv)

