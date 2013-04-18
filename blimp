#!/usr/bin/env python

import blimp
import os
import ConfigParser
import sys

def setup(config, parser):
  parser.read(config)
  if not parser.has_section('blimp'):
    parser.add_section('blimp')
  
  blimpArgs = ['username', 'api_key', 'app_id', 'app_secret']
  
  for arg in blimpArgs:
    if parser.has_option('blimp', arg):
      arg = parser.get('blimp', arg)
    else:
      parser.set('blimp', arg, raw_input('Insert your ' + arg + ' from Blimp: '))
      
  parser.write(open(config, 'w+'))
  
def reset(config, parser):
  open(config, 'w').close()
  setup(config, parser)
  
def mark(config, parser):
  parser.read(config)
  if not parser.has_section('blimp'):
    setup(config, parser)
    mark(config, parser)  
  query = sys.argv[2]
  matches = []
  api = blimp.Client(*[item[1] for item in parser.items('blimp')])
  for task in api.task.get()['objects']:
    if query in task['title'] and task['state'] == 'inactive':
      matches.append((task['id'], task['title']))    
  if len(matches) == 0:
    exit('No matches in Blimp')
  else:
    for index, match in enumerate(matches):
      print str(index + 1) + '. ' + match[1]
      option = raw_input('Select task to mark as done (0 to exit): ')
    if option == '0':
      exit()
    else:
      api.task.update(matches[int(option) - 1][0], {'state': 'review'})
      exit('Marked \'' + matches[int(option) - 1][1] + '\' as done in Blimp')  
  
def main():
  config = os.path.expanduser('~/.blimp') #if file doesn't exit, create it.
  parser = ConfigParser.ConfigParser()
  if len(sys.argv) < 3:
   exit(''''You must include one of the following options:\n
   setup - for first time installs
   reset - if you changed your initial keys
   mark \'keyword\' - mark a specific task as done\n''') 
  option = sys.argv[1] 
  
  if option == 'setup':
    setup(config, parser)
  elif option == 'reset':
    reset(config, parser)
  elif option == 'mark':
    if len(sys.argv) >= 3: 
      mark(config, parser)
    else:
      exit('Wrong parameters')
  else:
    exit('Sorry bro, can\'t do that')
  
if __name__ == '__main__':
  main()



    


    
