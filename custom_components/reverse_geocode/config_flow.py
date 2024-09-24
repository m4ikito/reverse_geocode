from homeassistant import config_entries
import voluptuous as vol
from homeassistant.const import CONF_NAME

DOMAIN = "reverse_geocode"

class ReverseGeocodeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=vol.Schema({
                vol.Required(CONF_NAME): str,  # Frage nach dem Namen
            }))

        # Überprüfen, ob der Benutzername eingegeben wurde
        if CONF_NAME not in user_input:
            return self.async_show_form(step_id="user", data_schema=vol.Schema({
                vol.Required(CONF_NAME): str,
            }))

        return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)