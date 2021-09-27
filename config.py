lat: float = 51.2200457368194
lng: float = 6.797644572684463
rad: float = 5  # Suchradius in km	Floatingpoint-Zahl, max: 25
fuel_type: str = "e5"	 # Spritsorte 'e5', 'e10', 'diesel' oder 'all'
sort: str = "price"  # Sortierung	price, dist (1)
apikey: str = "XXXXXXXXXXXXXXXXXXX" # API-Key: Requested at tankerkoenig

# Maximum Price
max_price: float = 1.54 # Edit

# E-Mail Settings
sender_email: str = "sender@email.de"
sender_email_password: str = "Password"
sender_smtp: str = "smtp.mail.de"
sender_port: int = 465

receiver_email: str = "your@email.de"
