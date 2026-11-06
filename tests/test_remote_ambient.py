from collections.abc import Awaitable, Callable

import pytest

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
from pytest_homeassistant.common import async_mock_service


@pytest.fixture
def automation_config() -> ConfigType:
    """Configure le blueprint pour une vanne et un capteur dans le salon."""
    return {
        'alias': "Température ambiante du salon",
        'use_blueprint': {
            'path': 'remote-ambient.yaml',
            'input': {
                'valves': ['climate.living_room'],
                'temp_sources': ['sensor.living_room_temperature'],
                'active': True,
            },
        },
    }


async def test_valve_receives_ambient_temperature(
    hass: HomeAssistant,
    run_automation: Callable[[int], Awaitable[None]],
) -> None:
    """Une vanne disponible reçoit 21,5 °C et utilise son capteur externe."""
    # prépare une température ambiante de 21,5 °C
    hass.states.async_set('sensor.living_room_temperature', '21.5')

    # et une vanne disponible
    hass.states.async_set('climate.living_room', 'heat')
    hass.states.async_set('number.living_room_external_temperature_input', '20')
    hass.states.async_set('select.living_room_temperature_sensor_select', 'internal_temperature',
        {'options': ['internal_temperature', 'remote_temperature']},
    )

    # Ces faux services enregistrent les appels sans commander de vraie vanne.
    temperature_updates = async_mock_service(hass, 'number', 'set_value')
    sensor_selection_updates = async_mock_service(hass, 'select', 'select_option')

    # exécute les actions sans attendre réellement les cinq secondes
    await run_automation(5)

    # vérifie la température transmise et la sélection du capteur externe
    assert len(temperature_updates) == 1
    assert temperature_updates[0].data == {
        'entity_id': ['number.living_room_external_temperature_input'],
        'value': 21.5,
    }

    assert len(sensor_selection_updates) == 1
    assert sensor_selection_updates[0].data == {
        'entity_id': ['select.living_room_temperature_sensor_select'],
        'option': 'remote_temperature',
    }
