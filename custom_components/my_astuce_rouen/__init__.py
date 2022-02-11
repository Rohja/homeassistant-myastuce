"""
The "My Astuce Rouen" custom component.
To use the my_astuce_rouen component you will need to add the following to your
configuration.yaml file.
my_astuce_rouen:
"""
from __future__ import annotations
import logging

import voluptuous as vol

from homeassistant.core import HomeAssistant
from homeassistant.helpers import config_validation as cv
from homeassistant.helpers.typing import ConfigType


# The domain of your component. Should be equal to the name of your component.
DOMAIN = "my_astuce_rouen"
_LOGGER = logging.getLogger(__name__)

CONF_LINES_NAME = "lines"
CONF_LINE_NAME = "line"
CONF_STATION_NAME = "station"
CONF_LINE_DIRECTION = "direction"

LINE_STOP_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_LINE_NAME): cv.string,
        vol.Required(CONF_LINE_NAME): cv.string,
        vol.Required(CONF_LINE_NAME): vol.All(vol.Coerce(int), vol.Range(min=1, max=2))
    }
)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Optional(CONF_LINES_NAME, default={}): vol.All(
            cv.ensure_list, [LINE_STOP_SCHEMA]
        )
    }),
}, extra=vol.ALLOW_EXTRA)

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    _LOGGER.info("Config:", config)
    hass.states.set('my_astuce_rouen.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True