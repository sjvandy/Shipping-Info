# Shipping Cost Estimator
# Steven Vandegrift - 05/24/2025
import shippo
from shippo.models import components
import os
from dotenv import load_dotenv
from ascii import ascii_art

def clear_screen():
    os.system('clear')
    print(ascii_art, end='\n')

def get_address(prompt = ""):
    print(prompt)
    address = components.AddressCreateRequest(
        street1 = input("Street Address: "),
        city = input("City: "),
        state = input("State: "),
        zip = input("Zipcode: "),
        country = "US"
    )
    clear_screen()
    return address

def create_parcel(prompt = ""):
    print(prompt)
    while True:
        try:
            length = input("Length (in): ")
            width = input("Width (in): ")
            height = input("Height (in): ")
            weight = input("Weight (lbs): ")

            # Confirm there will be no conversion errors during parcel creation
            float(length)
            float(width)
            float(height)
            float(weight)

            return components.ParcelCreateRequest(
                length = length,
                width = width,
                height = height,
                distance_unit = components.DistanceUnitEnum.IN,
                weight = weight,
                mass_unit = components.WeightUnitEnum.LB
            )
        except:
            print("One of your dimentions or weight were not a real number, try again.")

if __name__ == "__main__":
    while True:
        # SETUP API
        load_dotenv()
        api_key = os.getenv("SHIPPO_API_KEY")

        if not api_key:
            print("--- Shippo API Key Not Found ---")
            print("Please enter your Shippo API key to continue.")
            print("You can get a free key from https://goshippo.com/")
                        
            new_api_key = input("Enter your API key: ")
        
            if new_api_key:                
                with open('.env', 'w') as f:
                    f.write(f'SHIPPO_API_KEY="{new_api_key}"')
                                
                api_key = new_api_key
                print("\nAPI Key saved to .env file for future use. Continuing...")
            else:                
                print("No API key provided. Exiting.")
                break

        shippo_sdk = shippo.Shippo(api_key_header=api_key)
        
        clear_screen()
        
        address_from = get_address("We will start by entering in the address you are sending from.")
        address_to = get_address("Next, enter the address we are sending the package to.")
        parcel = create_parcel("Fantastic, now we need to enter information about the parcel.")

        print("Loading Shipping Rates...")
        
        shipment = shippo_sdk.shipments.create(
            components.ShipmentCreateRequest(
                address_from=address_from,
                address_to=address_to,
                parcels=[parcel],
                async_=False
            )
        )
        clear_screen()

        cheapest_rate = None

        # Show shipping results
        for rate in shipment.rates:
            print(f"Rate: ${rate.amount}\tEstimated Days:{rate.estimated_days}\t{rate.provider} {rate.servicelevel.name}")
            if cheapest_rate == None or float(cheapest_rate.amount) > float(rate.amount):
                cheapest_rate = rate
        print(f"\nThe most affordable rate would be from {cheapest_rate.provider} {cheapest_rate.servicelevel.name} at a cost of ${cheapest_rate.amount}")

        run_again = input("Would you like to check the price of another shipment? type 'yes', or hit Enter to exit the program...")
        if run_again != 'yes':
            break

    

    

  