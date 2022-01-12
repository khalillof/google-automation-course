#!/usr/bin/env python3
import sys
import os
import re

""" 
Find an error
In this lab, we'll search for the CRON error that failed to start. To do this, we'll use a python script to search log files for
 a particular type of ERROR log. In this case, we'll search for a CRON error within the fishy.log file that failed to start 
by narrowing our search to "CRON ERROR Failed to start.

Make the file executable before running it
sudo chmod +x find_error.py
Now, run 
./find_error.py ~/data/fishy.log
Now enter
CRON ERROR Failed to start
now see result by running ...
cat ~/data/errors_found.log
"""
def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors

  
def file_output(returned_errors):
  #with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
  with open('./data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)