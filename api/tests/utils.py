from pathlib import Path
from typing import Union


def get_scrapper_fixture_dir(context_name: str) -> str:
    """Call it whit __file__

    Make sure you have a fixture folder next to your tests
    """
    return Path(context_name).parent.joinpath("fixtures").as_posix()
