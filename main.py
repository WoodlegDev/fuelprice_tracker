import requests
import config
import smtplib
from email.message import EmailMessage
import time

# Set While Loop True
still_running: bool = True


def email_message():
    """Set E-Mail Message from config"""
    msg = EmailMessage()
    msg["Subject"] = f"Benzinpreis unter {config.max_price}€"
    msg["From"] = config.sender_email
    msg["To"] = config.receiver_email
    msg.set_content(f"Jetzt günstig tanken,\n\nNiedriger Preis bei {station_name} {station_brand}.\n"
                    f"Adresse: {station_street} {station_hn}, {station_postcode} {station_place}. \n"
                    f"Aktueller Preis: {station_price}")
    return msg


# Set Params from config
params = {
    "lat": config.lat,
    "lng": config.lng,
    "rad": config.rad,
    "type": config.fuel_type,
    "sort": config.sort,
    "apikey": config.apikey,
}

while still_running:

    # Get Data
    response = requests.get(url="https://creativecommons.tankerkoenig.de/json/list.php", params=params)
    data = response.json()

    if data["status"] == "ok":
        for station in data["stations"]:

            # Check for price
            if station["price"] < config.max_price:

                # Set Data
                station_name: str = station["name"]
                station_brand: str = station["brand"]
                station_place: str = station["place"]
                station_street: str = station["street"]
                station_hn: str = station["houseNumber"]
                station_postcode: int = station["postCode"]
                station_price: float = station["price"]
                station_is_open: bool = station["isOpen"]

                # Create Message
                message = email_message()

                # Send Email
                with smtplib.SMTP_SSL(config.sender_smtp, config.sender_port) as connection:
                    connection.login(user=config.sender_email, password=config.sender_email_password)
                    connection.send_message(message)
                print(f"Email sent. Station: {station_name}. Price: {station_price}€.")
                break

        # No Station found under max_price
        print(f"No Station found. Cheapest station {data['stations'][0]['name']}. Price: {data['stations'][0]['price']}")

    # Bad Response
    else:
        still_running = False
        print("An Error has occured.")

    # Wait for next request
    time.sleep(3600)



