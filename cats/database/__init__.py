import json
import os
import random


def save(name, cats):
    dir_ = os.path.dirname(__file__)
    path = os.path.join(dir_, name + '.json')

    with open(path, 'w') as f:
        json.dump(cats, f, indent=0)


def get_random():
    cats = _load_cats()
    return random.choice(cats)


def _load_cats():
    dir_ = os.path.dirname(__file__)

    cats = []

    for fn in os.listdir(dir_):
        _, ext = os.path.splitext(fn)
        if ext != '.json':
            continue

        with open(os.path.join(dir_, fn)) as f:
            cats.extend(json.load(f))

    return cats
