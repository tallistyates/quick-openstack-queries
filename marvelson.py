#!/usr/bin/python3
import requests
import argparse
import time
import hashlib


#Define API
XAVIER = 'http://gateway.marvel.com/v1/public'

#Calculate a hash to pass through to our Marvel API call
def hashbuilder(curtime, privkey, pubkey):
    return hashlib.md5((curtime + privkey + pubkey).encode('utf-8')).hexdigest()

#Perform a call API  
def marvelcharcall(curtime, hashy, pubkey, lookmeup):
    marvelurl = XAVIER + '/characters'
    marvelurl += "?name="+lookmeup+"&ts="+curtime+"&apikey="+pubkey+"&hash="+hashy
    hulk = requests.get(marvelurl)
    print(marvelurl)
    print(hulk)
    return hulk.json()

def main():
    with open('marvelpub') as pubkeyfile:
        beast = pubkeyfile.read()

    with open('marvelpriv') as privkeyfile:
        storm = privkeyfile.read()
        curtime =  str(int(time.time()))
        charlook = input("What characters are we looking up?")
        hashy = hashbuilder(curtime, storm, beast)
        print(marvelcharcall(curtime, hashy, beast, charlook))
main()