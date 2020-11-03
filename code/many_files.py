import os
for filename in os.listdir(os.getcwd()):
   with open(os.path.join(os.cwd(), filename), 'r') as f: # open in readonly mode