# Shipping Cost Estimator
# Steven Vandegrift - 05/24/2025
import shippo
from shippo.models import components
import os
from dotenv import load_dotenv
from ascii import ascii_art

if __name__ == "__main__":

    # SETUP API
    load_dotenv()
    api_key = os.getenv("SHIPPO_API_KEY")

    if not api_key:
        raise ValueError("API key not found. Make sure you have a .env file with SHIPPO_API_KEY set.")

    shippo_sdk = shippo.Shippo(api_key_header=api_key)

    # SETUP USER INTERFACE
    os.system('clear')
    print(ascii_art, end='\n')
    print("We will start by entering in the address you are sending from.")
    address_from = components.AddressCreateRequest(
        street1 = input("Street Address: "),
        city = input("City: "),
        state = input("State: "),
        zip = input("Zipcode: "),
        country = "US"
    )
    os.system('clear')
    print(ascii_art, end='\n')
    print("Next, enter the address we are sending the package to.")
    address_to = components.AddressCreateRequest(
        street1 = input("Street Address: "),
        city = input("City: "),
        state = input("State: "),
        zip = input("Zipcode: "),
        country = "US"
    )
    os.system('clear')
    print(ascii_art, end='\n')
    print("Fantastic, now we need to enter information about the parcel.")
    parcel = components.ParcelCreateRequest(
        length = input("Length (in): "),
        width = input("Width (in): "),
        height = input("Height (in): "),
        distance_unit = components.DistanceUnitEnum.IN,
        weight = input("Weight (lbs): "),
        mass_unit = components.WeightUnitEnum.LB
    )

    print("Loading Shipping Rates...")
    
    shipment = shippo_sdk.shipments.create(
        components.ShipmentCreateRequest(
            address_from=address_from,
            address_to=address_to,
            parcels=[parcel],
            async_=False
        )
    )
    os.system('clear')
    print(ascii_art, end='\n')
    for rate in shipment.rates:
        print(f"{rate.provider} {rate.servicelevel.name}\t\t\tEstimated Days:{rate.estimated_days}\t Rate: ${rate.amount}\t ")

    

  