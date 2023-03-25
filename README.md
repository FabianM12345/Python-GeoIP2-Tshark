# Python-GeoIP2-Tshark
Python Script to get the geolocation of the IP addresses on a tshark scan. 

The purpose of this script is to use Python, Tshark, and Maxmind geolocation database to grab the destination IP addresses and to return the city and country 
the IP address is located in. 

--------------------------------------------------------------------------------------------------------------------------------------------------------------

Geolocator:

The first step is to go to Maxmind website and signup to get the latest database from them.

https://dev.maxmind.com/?lang=en

The second step is to unzip the file from their website and place it in the directory your Python project is in. 

After that run this command in the terminal/command prompt of your OS: 

  (Assuming your already have Python Installed.)

   'pip install geoip2'

This will install the geoip2 library for python.

-------------------------------------------------------------------------------------------------------------------------------------------------------------

Tshark:

To get Tshark you have to install wireshark onto your computer. But since I was using Kali Linux it already came with Wireshark and Tshark.

If you are using Windows then after installing Wireshark you should find Tshark in this directory:
 C:\Program Files\Wireshark

In Linux it should be in:
 /bin

The reason why I include this is because you may need the path to 'tshark.exe'.

---------------------------------------------------------------------------------------------------------------------------------------------------------

Libraries used in this script:
 os - I used this library to interact with the operating system and to run commands in the terminal with Python.
 datetime - I used this to get the current date and time.
 re - I used this to find a certain pattern within a string.
 geoip2.database - I used this to geolocate ip addresses.

 -------------------------------------------------------------------------------------------------------------------------------------------------------

How this script works:
  1. The sniffer() function runs the tshark commands in the terminal and then outputs the scan into a text file in your projects directory.
     Then the file is read and all the IP addresses in the text file are grabbed and moved into an array. If the IP address is the same as
     your local IP then it is discarded and if the IP address is not the same as your local IP it is added to another array for destination IP's.

  2. The geolocate_and_op() function then gets the IPs from the array with the destination IPs and returns their city and country.
      output should be:
       IP address -> City, Country
