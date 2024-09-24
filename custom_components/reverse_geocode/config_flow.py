from homeassistant import config_entries
from homeassistant.const import CONF_NAME, CONF_ENTITY_ID

class ReverseGeocodeConfigFlow(config_entries.ConfigFlow, domain="reverse_geocode"):
    """Handle a config flow for Reverse Geocode."""
    
    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(step_id="user")

        return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)
