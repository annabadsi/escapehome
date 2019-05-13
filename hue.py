from phue import Bridge

# IP Adresse der Hue Bridge rausfinden:
# https://www.meethue.com/api/nupnp
IP_ADDRESS = '192.168.178.67'

b = Bridge(IP_ADDRESS)

# nur einmal, zu Hue Bridge connecten
# b.connect()

# API Status
# - Lampen: Zustand, Name, Produktname
# - Gruppen: Wohnzimmer, Küche, Zimmer,..
# - Configuration: "Natürliches Aufwachen" Einstellungen
# - Regeln: Dimmer Tastenbelegung,
# - Sensoren: Bewegungsmelder -  Zustand, Temperatur
b.get_api()
