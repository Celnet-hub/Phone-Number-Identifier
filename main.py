import phonenumbers

from phonenumbers import timezone, geocoder, carrier

print('\nPlease include country code (ex: +234xxxx): ')

# collect input from user.
user_name = input('\nEnter owner of Phone Number: ')
user_input = input('\nEnter a Valid Phone Number: ')

phone_number = phonenumbers.parse(user_input)
timeZone = timezone.time_zones_for_number(phone_number)

# Getting carrier of a phone number
network_carrier = carrier.name_for_number(phone_number, 'en')

# Getting region information
region = geocoder.description_for_number(phone_number, 'en')


print(f'{user_name} phone number ({user_input}) details are as follow:\n')
print(f'Time Zone: {timeZone}')
print(f'\nNetwork Carrier: {network_carrier}')
print(f'\nRegion: {region}')