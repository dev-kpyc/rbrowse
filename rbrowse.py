#!/usr/bin/python3

def print_titles(titles, lo, hi):
   for i in range(lo, hi):
      print('{} {}'.format(i,titles[i][1]))

import sys
import re
import urllib.request

attempts = 0
while attempts < 10:
   try:
      attempts = attempts + 1   
      frontpage = urllib.request.urlopen('http://www.reddit.com').read().decode()
      break
   except:
      print('Connecting ...')
if attempts >= 10:
   print('10 Request Limit Reached')
   print('Failed to Connect')
   sys.exit()
   #class="subreddit hover" >pics</a>
title = re.compile('<a class="title " href="(.*?)"(?: rel="nofollow")? >(.*?)</a>.*?(?:<time title=)"(.*?)".*?(?:class="subreddit hover" >)(.*?)</a>', re.DOTALL | re.MULTILINE)
titles = re.findall(title,frontpage)

lo=1
hi=11

command = ''

while (command != 'exit'):

   if (command == 'next'):
      if lo <= 11: lo = lo + 10
      if hi <= 21: hi = hi + 10
   if (command == 'back'):
      if lo >= 11: lo = lo - 10
      if hi >= 21: hi = hi - 10

   if (command.isdigit()):
      pagenum = int(command)
         
      if (pagenum < len(titles)):
         print(titles[pagenum][1])
         print(titles[pagenum][0])
         print('Posted to r/{} on {}'.format(titles[pagenum][3], titles[pagenum][2]))
      
      while (command != 'back'):
         command = input()  
      
   print_titles(titles,lo,hi)  
   command = input()
