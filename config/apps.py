
import os


def apps_dir():
    return 'apps'


def installed_apps():
    apps_dir_ = apps_dir()

    apps = []
    for path in os.listdir(apps_dir_):
        if os.path.isdir(os.path.join(apps_dir_, path)) and not path.startswith('_'):
            apps.append(path)
    return apps
