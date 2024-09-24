from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_NAME

# Neue Konstante für den Device Tracker definieren
CONF_DEVICE_TRACKER = "device_tracker"

class ReverseGeocodeConfigFlow(config_entries.ConfigFlow, domain="reverse_geocode"):
    """Handle a config flow for Reverse Geocode."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is None:
            return await self.async_show_form(step_id="user")

        return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)

    async def async_show_form(self, step_id: str, user_input=None):
        return self.async_show_form(
            step_id=step_id,
            data_schema=self._get_data_schema(),
        )

    def _get_data_schema(self):
        from homeassistant.helpers import config_entry_flow
        from homeassistant.helpers import schema

        return schema.Schema(
            {
                schema.string(CONF_NAME): str,
                schema.string(CONF_DEVICE_TRACKER): str,
            }
        )