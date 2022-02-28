
'''
this geocoder helps you find out which number is calling and where it is calling from
'''
import phonenumbers 
from phonenumbers import geocoder
from phonenumbers import carrier


number = input("please input  number that we can use: ")



ch_number = phonenumbers.parse(number, "CH")




print(geocoder.description_for_number(ch_number,  'en'))

service_provider = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_provider, "en"))