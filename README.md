# Reverse Geocode Integration

![GitHub](https://img.shields.io/github/license/m4ikito/reverse_geocode)
![HACS Badge](https://img.shields.io/badge/HACS-Default-orange.svg)

## Beschreibung

Die **Reverse Geocode Integration** für Home Assistant ermöglicht es, die geografischen Koordinaten (Breitengrad und Längengrad) eines Geräts in eine lesbare Adresse umzuwandeln. Diese Integration ist besonders nützlich für Standortdienste und Automatisierungen, die auf den aktuellen Standort eines Geräts basieren.

## Anforderungen

- Home Assistant Version: 2023.5.0 oder höher
- Python 3.8 oder höher

## Installation

1. Installiere [HACS](https://hacs.xyz/docs/installation/installation), falls noch nicht geschehen.
2. Suche in HACS nach "Reverse Geocode" und installiere die Integration.
3. Füge die folgende Konfiguration zu deiner `configuration.yaml` hinzu:
   ```yaml
   sensor:
     - platform: reverse_geocode
       name: "Location Sensor"
       entity_id: device_tracker.XYZ

## Verwendung

Nach der Installation und Konfiguration kannst du den Sensor im Lovelace-Dashboard verwenden. Füge eine Karte hinzu, um die Adresse des Geräts anzuzeigen.

## Entwickler

  • GitHub: m4ikito
	•	Repository: reverse_geocode
	•	Issues: Bei Problemen oder Verbesserungsvorschlägen öffne ein Issue.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die LICENSE Datei für weitere Details.
