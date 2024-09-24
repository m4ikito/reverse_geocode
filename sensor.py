import logging
import requests
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME, CONF_ENTITY_ID
from homeassistant.helpers.entity import Entity

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "Reverse Geocode"

# Füge die Option für den Device Tracker hinzu
PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_ENTITY_ID): cv.entity_id,
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    entity_id = config.get(CONF_ENTITY_ID)  # Hol dir den Device Tracker aus der Konfiguration
    
    device_tracker = hass.states.get(entity_id)
    latitude = device_tracker.attributes.get("latitude")
    longitude = device_tracker.attributes.get("longitude")

    if latitude and longitude:
        add_entities([ReverseGeocodeSensor(name, latitude, longitude)])

class ReverseGeocodeSensor(Entity):
    def __init__(self, name, lat, lon):
        self._name = name
        self._state = None
        self._latitude = lat
        self._longitude = lon
    
    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        self._state = self.reverse_geocode(self._latitude, self._longitude)

    def reverse_geocode(self, lat, lon):
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1"
        try:
            response = requests.get(url)
            data = response.json()
            if 'error' not in data:
                return data.get("display_name", "Unknown location")
            else:
                return "Location not found"
        except Exception as e:
            _LOGGER.error(f"Error fetching data from Nominatim: {e}")
            return "Error"
