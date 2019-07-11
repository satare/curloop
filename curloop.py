from __future__ import print_function
import os
import sys
import argparse
import requests
import time
import json
import base64

def parseResponse(response,args):
    if args is None : 
        
        print(str(response.status_code)+" "+response.reason)
    elif args == 1 :
        #Be carefull, the requests may not be a success every time...
        print (response.text)
    else :
        print("headers:"+str(response.headers))
        print("response:"+str(response.text))
        print("took:"+str(response.elapsed))
    

def main(arguments):
    cpt=None
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'url', 
        help="Url to scrape", 
        type=str)
    parser.add_argument(
        '-n', 
        '--number', 
        help="Number of iterations",
        type=int)
    parser.add_argument(
        '-t',
        '--time', 
        help="Time in seconds between loops",
        type=int)
    parser.add_argument(
        '-v',
        '--verbose', 
        help="Level of verbosity",
        action='count')
    args = parser.parse_args(arguments)
    while True :
        try: #catch the Keyboard Interrupt
            response=str()
            url = args.url
            try : # Catch MissingShema Exception
                response = requests.get(url)
            except requests.exceptions.MissingSchema as ex1:
                print (ex1.args[0])
                break
            except requests.exceptions.ConnectionError as ex2 :
                print (ex2.args[0])
                break
            parseResponse(response, args.verbose)
            if args.number: # This loop is not infinite
                if cpt is None: # First run, we must set the counter
                    cpt=args.number
                cpt-=1 # get better every time
                if not cpt>0 : 
                    return        
            if not args.time is None: # take your time ... 
                time.sleep(args.time)
            else:
                time.sleep(1) #Default Behavior : Wait 1 sec between each loop
        except KeyboardInterrupt:
            print ("Bye!")
            break

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))