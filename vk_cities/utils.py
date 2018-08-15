# coding=utf-8

import logging

import vklancer.api

from . import models


logger = logging.getLogger(__name__)


def download(country_codes, language, token, update=False):
    countries = download_countries(country_codes, language, token, update)
    regions = download_regions(countries, language, token, update)
    download_cities(regions, language, token, update)


def download_countries(codes, language, token, update=False):
    """Download countries from VK.com and save to database."""
    API = vklancer.api.API(token=token)
    kwargs = {'lang': language.split('-')[0].lower()}
    countries = []

    if codes:
        kwargs['code'] = ','.join(codes)

    for item in API.database.getCountries(**kwargs)['response']['items']:
        queryset = models.Country.objects.filter(vk_id=item['id'])

        if queryset.exists():
            country = queryset.last()

            if update:
                queryset.update(name=item['title'])

                logger.info('Updated country: {}'.format(country))
        else:
            country = models.Country.objects.create(
                vk_id=item['id'], name=item['title']
            )

            logger.info('Added country: {}'.format(country))

        countries.append(country)

    return countries


def download_regions(countries, language, token, update=False):
    API = vklancer.api.API(token=token)
    kwargs = {'lang': language.split('-')[0].lower()}
    regions = []

    for country in countries:
        data = API.database.getRegions(country_id=country.vk_id, **kwargs)

        for item in data['response']['items']:
            kwargs = {
                'name': item['title'],
                'country': country,
            }

            queryset = models.Region.objects.filter(vk_id=item['id'])

            if queryset.exists():
                region = queryset.last()

                if update:
                    queryset.update(**kwargs)

                    logger.info('Updated region: {}'.format(region))
            else:
                region = models.Region.objects.create(
                    vk_id=item['id'], **kwargs
                )

                logger.info('Added region: {}'.format(region))

            regions.append(region)

    return regions


def download_cities(regions, language, token, update=False):
    API = vklancer.api.API(token=token)
    language = language.split('-')[0].lower()
    cities = []
    country_id = 0



    for region in regions:
        page = 0

        while True:
            data = API.database.getCities(
                region_id=region.vk_id, country_id=region.country.vk_id,
                offset=page*1000, count=1000, lang=language
            )

            if country_id != region.country.vk_id:
                country_id = region.country.vk_id
                data_witch_important = API.database.getCities(
                    country_id=region.country.vk_id,
                    offset=0, count=1000, lang=language
                )

                witch_important = [item for item in data_witch_important['response']['items']
                                   if 'important' in item]
                items = [*data['response']['items'], *witch_important]
            else:
                items = data['response']['items']

            if not items:
                break

            for item in items:
                kwargs = {
                    'name': item['title'],
                    'region': region,
                    'area': item.get('area', '')
                }

                queryset = models.City.objects.filter(vk_id=item['id'])

                if queryset.exists():
                    city = queryset.last()

                    if update:
                        queryset.update(**kwargs)

                        logger.info('Updated city: {}'.format(city))
                else:
                    city = models.City.objects.create(
                        vk_id=item['id'], **kwargs
                    )

                    logger.info('Added city: {}'.format(city))

                cities.append(city)

            page += 1

    return cities
