import phonenumbers
from phonenumbers import geocoder, carrier


# Parse phone number
phone_number = input("Enter phone number (in international format): ")
try:
    parsed_number = phonenumbers.parse(phone_number, None)
except phonenumbers.NumberParseException:
    print("Invalid phone number")
    exit()

# Check if phone number is valid
if not phonenumbers.is_valid_number(parsed_number):
    print("Invalid phone number")
    exit()

def validate_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException:
        return False

# Function to get phone number information
def get_phone_number_info(phone_number):
    parsed_number = phonenumbers.parse(phone_number)
    location = geocoder.description_for_number(parsed_number, "en")
    service_provider = carrier.name_for_number(parsed_number, "en")
    number_type = phonenumbers.number_type(parsed_number)
    return location, service_provider, number_type


if validate_phone_number(phone_number):
    location, service_provider, number_type = get_phone_number_info(phone_number)
    print("Phone number is valid")
    print(f"Location: {location}")
    print(f"Service Provider: {service_provider}")
    print(f"Number Type: {number_type}")
else:
    print("Invalid phone number.")

# Get local format of the phone number
local_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)

# Get international format of the phone number
international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

# Get country prefix of the phone number
country_prefix = "+" + str(parsed_number.country_code)

# Get country name of the phone number
country_name = phonenumbers.region_code_for_number(parsed_number)

# Get country code of the phone number
country_code = phonenumbers.country_code_for_region(country_name)

# Get line type of the phone number
line_type = phonenumbers.number_type(parsed_number)

# Print results
print("Phone number is valid")
print("Local format: ", local_format)
print("International format: ", international_format)
print("Country prefix: ", country_prefix)
print("Country name: ", country_name)
print("Country code: ", country_code)
print("Line type: ", line_type)










