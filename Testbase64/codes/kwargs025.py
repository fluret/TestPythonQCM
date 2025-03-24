def fonction_travail(**kwargs):
    base = {"config": {"debug": False}}
    return {**base, "config": {**base["config"], **kwargs}}

print(fonction_travail(debug=True))