# Django VK Cities #
*Django package for using VK.com cities database*

[![Build Status](https://travis-ci.org/pyvim/django-vk-cities.svg)](https://travis-ci.org/pyvim/django-vk-cities)
[![Coverage Status](https://coveralls.io/repos/pyvim/django-vk-cities/badge.svg?branch=master&service=github)](https://coveralls.io/github/pyvim/django-vk-cities?branch=master)

## Installation ##

`pip install django-vk-cities`

Add `vk_cities` to `INSTALLED_APPS`.

After run:
```bash
python manage.py migrate
python manage.py vk_cities download
```

## Configuration ##

Package using next settings variable:
```python
LANGUAGE_CODE = 'en-US'  # places names language
VK_CITIES_COUNTRIES = ['RU', 'UA']  # countries codes from ISO 3166-1
VK_APP_TOKEN = '<token>' # token from vk app (create from https://vk.com/apps?act=manage)
```

## Tests ##
```bash
tox
```

## Changelog ##
See [releases](https://github.com/pyvim/django-vk-cities/releases)

## License ##
See [LICENSE](https://github.com/pyvim/django-vk-cities/blob/master/LICENSE)
