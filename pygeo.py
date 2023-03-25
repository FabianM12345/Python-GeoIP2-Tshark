
import os #Importing this module allows me to run terminal commands with Python.
from datetime import datetime #Imports date and time module
import re #This module takes a regular expression pattern and a string and searches for that pattern within the string.
import geoip2.database #Gets the Geolocation of the IP address.

ip_add_list = [] #An Array with all the ip addresses extracted from the scan.
dest_ip = [] #An Arraty with only external Ip address you are communicating with.

#Runs the tshark commands and outputs it into a file.
def sniffer():
  now = datetime.now() # Current date and time.
  
  #Runs the commands.
  cmd = r'tshark' #Exe Tshark
  inter = ' -i '+' ' #Enter your interface in the blank area.
  pkt_count = ' -c '+' ' #Enter the number of Packets you would like to capture in the blank area.
  date_time = now.strftime("%m-%d-%Y%H:%M:%S") #Gets the current date and time
  global file_name #Creates a global variable for the file name.
  file_name = 'capture_op_'+str(date_time)+'.txt'
  to_file = ' > '
  command = cmd + inter + pkt_count + to_file + file_name
  os.system(command) #Runs the command in the terminal.
  
  #Parses through the file created and retrieves the IP address and puts it in an array. 
  op_file = open(file_name, 'r') #Opens the file and reads its contents.
  pattern = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' #The pattern to detect IP addresses.
  #Searches through the file to find IP addresses and adds them into an array.
  for i in op_file:
    ip_add = re.search(pattern, i)
    ip_add_list.append(ip_add.group())
    
  op_file.close()
      
#Gets the Dest IP and geolocates it. 
def geolocate_and_op():
  for i in ip_add_list:
    #Enter in your local IP address for the interface you selected.
    #If the ip address selected is not your local IP then it will be added to an array for destination IP addresses.
    #Enter your interfaces IP address in the blank area below. 
    if i != ' ':
      dest_ip.append(i)
  #Gets the IP address and searches for it in the database to return City, Country
  for IP in dest_ip:
    reader = geoip2.database.Reader(' ') #Enter the full path to the geolocator db in the blank area.
    response = reader.city(str(IP))
    print(str(IP)+'->'+'{}, {}'.format(response.city.name, response.country.iso_code))
    reader.close()
    
      
sniffer()
geolocate_and_op()
   
    

