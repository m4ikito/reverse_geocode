from homeassistant.helpers.entity import Entity
from homeassistant.helpers import config_validation as cv
from homeassistant.const import CONF_ENTITY_ID

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    device_tracker_entity_id = config.get(CONF_ENTITY_ID)

    # Überprüfen, ob der device_tracker vorhanden ist
    device_tracker = hass.states.get(device_tracker_entity_id)
    if device_tracker is None:
        _LOGGER.error(f"Device tracker '{device_tracker_entity_id}' not found.")
        return

    # Werte abrufen
    latitude = device_tracker.attributes.get("latitude")
    longitude = device_tracker.attributes.get("longitude")

    # Hier fügen wir Sensoren hinzu
    async_add_entities([ReverseGeocodeSensor(latitude, longitude)], True)

class ReverseGeocodeSensor(Entity):
    def __init__(self, latitude, longitude):
        self._latitude = latitude
        self._longitude = longitude
        self._attr_name = "Reverse Geocode Sensor"  # Beispielname

    @property
    def state(self):
        return f"{self._latitude}, {self._longitude}"

    @property
    def name(self):
        return self._attr_name