import asyncio
from collections.abc import AsyncIterator, Awaitable, Callable
from datetime import timedelta
from pathlib import Path
from shutil import copytree

import pytest

from homeassistant.core import HomeAssistant
from homeassistant.setup import async_setup_component
from homeassistant.helpers.typing import ConfigType
from homeassistant.util import dt as datetime_util
from pytest_homeassistant.common import async_fire_time_changed

from tests import ROOT_PATH


@pytest.fixture
def hass_config_dir(hass_tmp_config_dir: str) -> str:
    """Préparer une configuration isolée contenant tous les blueprints."""
    copytree(
        ROOT_PATH / 'blueprints',
        Path(hass_tmp_config_dir) / 'blueprints' / 'automation',
        dirs_exist_ok=True,
    )

    return hass_tmp_config_dir


@pytest.fixture
async def automation_id(
    hass: HomeAssistant,
    automation_config: ConfigType,
) -> AsyncIterator[str]:
    """Charger l'automatisation définie par le test et nettoyer ses déclencheurs."""
    automation_loaded = await async_setup_component(
        hass,
        'automation',
        {'automation': automation_config},
    )

    assert automation_loaded
    await hass.async_block_till_done()

    automations = hass.states.async_all('automation')
    assert len(automations) == 1, "Le test doit définir une seule automatisation"
    entity_id = automations[0].entity_id

    try:
        yield entity_id
    finally:
        await hass.services.async_call(
            'automation',
            'turn_off',
            {'entity_id': entity_id},
            blocking=True,
        )


@pytest.fixture
def run_automation(
    hass: HomeAssistant,
    automation_id: str,
) -> Callable[[int], Awaitable[None]]:
    """Exécuter les actions en simulant les secondes d'attente."""
    async def run(seconds: int) -> None:
        execution = hass.async_create_background_task(
            hass.services.async_call(
                'automation',
                'trigger',
                {'entity_id': automation_id},
                blocking=True,
            ),
            'test automation',
        )

        # Laisser l'action delay installer son timer sans attendre sa fin.
        for _ in range(10):
            await asyncio.sleep(0)

        async_fire_time_changed(hass, datetime_util.utcnow() + timedelta(seconds=seconds))
        await execution

    return run
