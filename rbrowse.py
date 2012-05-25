#!/usr/bin/python3

def print_topics(topics, lo, hi):
   for i in range(lo, hi):
      print('{} {}'.format(i,topics[i][1]))

def load_page(page):
   attempts = 0
   while attempts < 10:
      try:            
         page = urllib.request.urlopen(page).read().decode()
         break
      except:
         attempts = attempts + 1
   if attempts >= 10:
      print('10 Request Limit Reached')
      print('Failed to Connect')
      sys.exit()
   else:
      return page

def show_help():
   print('# - open the numbered topic on the front page')
   print('next - view the next 10 links')
   print('back - view the previous 10 links')
   print('exit/quit - exit the script')
   print('front - return to the front page')
   print('r/[subreddit] - begin browsing a subreddit')
   print('help - view the above instructions') 

import sys
import re
import urllib.request

reddit_home = 'http://www.reddit.com'

page = load_page(reddit_home)
reg_topic = re.compile('<a class="title " href="(.*?)"(?: rel="nofollow")? >(.*?)</a>.*?(?:<time title=)"(.*?)".*?<a class="comments" href="(.*?)" target="_parent" >(.*?) comments</a>', re.DOTALL|re.MULTILINE)
reg_comment = re.compile('<div class="md"><p>(.*?)</p>\n</div>', re.DOTALL|re.MULTILINE)
topics = re.findall(reg_topic, page)

lo=1
hi=11

command = ''

while (command != 'exit' and command != 'quit'):

   if (command == 'help'):
      show_help()
      command = input()

   if (command == 'next'):
      if lo <= 11: lo = lo + 10
      if hi <= 21: hi = hi + 10
   if (command == 'back'):
      if lo >= 11: lo = lo - 10
      if hi >= 21: hi = hi - 10
      
   if (command == 'front'):
      page = load_page(reddit_home)
      topics = re.findall(reg_topic, page)
   if (re.match("r/.*", command) != None):
      page = load_page(reddit_home + '/' + command + '/')
      topics = re.findall(reg_topic, page)   


   if (command.isdigit()):
      topic_num = int(command)
         
      if (topic_num < len(topics)):
         topic_title = topics[topic_num][1]
         topic_url = topics[topic_num][0]
         topic_date = topics[topic_num][2]
         comments_url = topics[topic_num][3]
         comments_page = load_page(comments_url)
         comment_count = topics[topic_num][4]
         comments = re.findall(reg_comment, comments_page)
         
         print(topic_title)
         print(topic_url)
         print('Posted on ' + topic_date)
         print('')
         for i in range(1,min(4, len(comments))):
            print('{} {}'.format(i,comments[i]))
      
      while (command != 'back'):
         command = input()
      
   print_topics(topics,lo,hi)
   command = input()
