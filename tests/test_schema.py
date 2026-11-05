from pathlib import Path

import pytest

from homeassistant.components.blueprint.models import Blueprint
from homeassistant.components.blueprint.schemas import BLUEPRINT_SCHEMA
from homeassistant.util import yaml as yaml_util

from tests import ROOT_PATH

BLUEPRINTS = sorted((ROOT_PATH / 'blueprints').glob('*.yaml'))


def test_blueprints_exist() -> None:
    assert BLUEPRINTS, "Aucun blueprint YAML trouvé"


@pytest.mark.parametrize('path', BLUEPRINTS, ids=lambda path: path.name)
def test_blueprint_schema(path: Path) -> None:
    blueprint = Blueprint(
        yaml_util.load_yaml_dict(path),
        path=path.name,
        expected_domain='automation',
        schema=BLUEPRINT_SCHEMA,
    )
    assert blueprint.validate() is None
