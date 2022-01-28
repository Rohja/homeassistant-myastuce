import voluptuous as vol

from homeassistant import data_entry_flow, config_entries

from . import DOMAIN

@config_entries.HANDLERS.register(DOMAIN)
class MyAstuceConfigFlow(data_entry_flow.FlowHandler):
    """Handle a esphome config flow."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        # Specify items in the order they are to be displayed in the UI
        data_schema = {
            vol.Required("username"): str,
            vol.Required("password"): str,
        }

        if self.show_advanced_options:
            data_schema["allow_groups"] = bool

        return self.async_show_form(step_id="init", data_schema=vol.Schema(data_schema))