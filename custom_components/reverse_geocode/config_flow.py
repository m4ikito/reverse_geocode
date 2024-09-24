import logging
from homeassistant import config_entries
import voluptuous as vol
from homeassistant.const import CONF_NAME, CONF_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

class ReverseGeocodeConfigFlow(config_entries.ConfigFlow, domain='reverse_geocode'):
    async def async_step_user(self, user_input=None):
        if user_input is None:
            return await self.async_show_form(step_id="user")

        return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

    async def async_show_form(self, step_id):
        return self.async_show_form(
            step_id=step_id,
            data_schema=vol.Schema({
                vol.Required(CONF_NAME): str,
                vol.Required("device_tracker"): str,  # Name des device_tracker
                vol.Required(CONF_SCAN_INTERVAL, default=60): int,  # Default auf 60 Sekunden
            }),
        )