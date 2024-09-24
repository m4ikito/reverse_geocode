import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback

from .const import DOMAIN  # Importiere deine Domain-Konstante

@callback
def configured_instances(hass):
    """Gibt eine Liste der konfigurierten Instanzen zurück."""
    return set(entry.title for entry in hass.config_entries.async_entries(DOMAIN))

class ReverseGeocodeConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Reverse Geocode."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            # Prüfe, ob diese Instanz bereits konfiguriert ist
            if user_input["name"] in configured_instances(self.hass):
                errors["base"] = "name_exists"
            else:
                # Erstelle die Konfigurationseinträge
                return self.async_create_entry(
                    title=user_input["name"],
                    data=user_input,
                )

        # Standard-Daten für die Eingabemaske
        data_schema = vol.Schema({
            vol.Required("name"): str,
            vol.Required("device_tracker"): str,
        })

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )