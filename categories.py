REPLACEMENTS = {
    "doc": "Docs",
    "lttp": "ALTTP",
    "wind waker": "The Wind Waker",
    "tww": "The Wind Waker",
    "cvcotm": "Castlevania - Circle of the Moon",
    "unittests": "Tests",
    "unit tests": "Tests",
    "bhc": "BizHawkClient",
    "pokémon rb": "Pokemon Red/Blue",
    "pokemon rb": "Pokemon Red/Blue",
    "sdv": "Stardew Valley",
    "cc": "commonclient",
    "v6": "VVVVVV",
    "sm": "Super Metroid",
    "sm64": "Super Mario 64",
    "witness": "The Witness",
}

CATEGORIES_THAT_GO_AT_THE_TOP = [
    "core",
    "multiserver",
    "webhost",
    "ci",
    "tests",
    "docs",
    "commonclient",
    "bizhawkclient",
    "ger",
    "launcher",
    "setup",
    "options",
    "docker",
]


def clean_category(category: str) -> str:
    category = REPLACEMENTS.get(category.lower(), category)
    if category.endswith(".py"):
        category = category[:-3]
    return category
