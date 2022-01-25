"""
The "My Astuce Rouen" custom component.
To use the my_astuce_rouen component you will need to add the following to your
configuration.yaml file.
my_astuce_rouen:
"""
from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "my_astuce_rouen"


def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up a skeleton component."""
    # States are in the format DOMAIN.OBJECT_ID.
    hass.states.set('my_astuce_rouen.Hello_World', 'Works!')

    # Return boolean to indicate that initialization was successfully.
    return True