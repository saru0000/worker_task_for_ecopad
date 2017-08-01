#from celery.task import task
#from dockertask import docker_task
#from subprocess import call,STDOUT
#from jinja2 import Template
#from shutil import copyfile, move
#from glob import glob
#import requests,os
#from pymongo import MongoClient
#from datetime import datetime
#Default base directory 
#basedir="/data/static/"
#spruce_data_folder="/data/local/spruce_data"
#host= 'ecolab.cybercommons.org'
#host_data_dir = os.environ["host_data_dir"] 
# "/home/ecopad/ecopad/data/static"

#print "hello-world"

#New Example task
####
####
####

#def sum():
#    """ Example task that sum numbers from string in other file """
file = open('/home/ecolab/service/virtpy/dataincomingfolder/exampledata.txt', 'r')   
line = file.read()
total = sum(int(num) for num in line.split(','))
f = open( '~/service/codetestresult/resultofsum.txt', 'w' )
f.write(total)
f.close()
