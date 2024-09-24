from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from .const import DOMAIN

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Setze die Integration mit der Konfiguration aus dem Konfigurationsfluss auf."""
    hass.data.setdefault(DOMAIN, {})

    # Hier könntest du das Setup deiner Integration auf Basis der entry-Daten vornehmen
    hass.data[DOMAIN][entry.entry_id] = entry.data

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Entferne eine Instanz der Integration."""
    if entry.entry_id in hass.data[DOMAIN]:
        hass.data[DOMAIN].pop(entry.entry_id)

    return True