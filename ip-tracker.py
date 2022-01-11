import socket
import sys
import pygeoip as geo
import subprocess as sp

ip_dat = geo.GeoIP('GeoLiteCity.dat')
name = input("Enter name of the website: ")
url = input("Enter URL: https://")

host = socket.gethostname()
ip1 = socket.gethostbyname(host)
print(f"User Hostname: {host}")
print(f"User IP Address: {ip1}")

try:
    s_generate = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully generated")
except socket.error as err:
    print("socket creation failed with error %s" % err)

port = 80               # Default Socket Port

try:
    host_ip = socket.gethostbyname(url)
except socket.gaierror:
    print("There was an error resolving the host")
    sys.exit()

s_generate.connect((host_ip, port))

print("The socket has successfully connected to", name)

print("Do you want further details about the IP? (y/n)")

choice = input("y for YES & n for NO: ")

if choice == 'y':
    lookup = ip_dat.record_by_addr(host_ip)
    print("")
    print("Below is the summary of the given IP address:")
    for key, val in lookup.items():
        print('%s : %s' % (key, val))
    print("Server Port: ", port)

    print("")
    print("Do you want to save this information? (y/n)")
    choice2 = input("y for YES & n for NO: ")

    if choice2 == 'y':
        dma = lookup['dma_code']
        areacode = lookup['area_code']
        metro_code = lookup['metro_code']
        zipcode = lookup['postal_code']
        country_code = lookup['country_code']
        country_code3 = lookup['country_code3']
        country_name = lookup['country_name']
        continent = lookup['continent']
        region_code = lookup['region_code']
        city = lookup['city']
        lat = lookup['latitude']
        lon = lookup['longitude']
        time_zone = lookup['time_zone']

        details = {'DMA Code': dma, 'Area Code': areacode, 'Metro Code': metro_code, 'Zip Code': zipcode, 'Standard Country Code': country_code, 'Country Code 3': country_code3, 'Country Name': country_name, 'Continent': continent, 'Region Code': region_code, 'City': city, 'Latitude': lat, 'Longitude': lon, 'Time Zone': time_zone, 'Port': port}
        with open("records.txt", 'w') as f:
            for key, value in details.items():
                f.write('%s:%s\n' % (key, value))

        print("Data is successfully written to records.txt")
        print("Opening file now...")

        program_name = "notepad.exe"
        file_name = 'records.txt'
        sp.Popen([program_name, file_name])

    elif choice2 == 'n':
        print("")

    else:
        print("Invalid Choice, Try again!!!")
        quit(1)

elif choice == 'n':
    print("Program Exited successfully.")

else:
    print("Invalid Choice, Try again!!!")
    quit(1)

sys.exit()
