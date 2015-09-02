# -*- coding: utf-8 -*-
import requests
from models import Estate
import urllib
from urlparse import urlparse
from django.core.files import File

__author__ = 'guest007'

source = 'http://www.jm.se/bostader/sok-bostad/#c=stockholm&tab=objects&listmode=box'
ajax = "http://www.jm.se/Ajax/ResidenceSearch/Search/"
params = {
    "c": "stockholm",
    "tab": "objects",
    "listmode": "box",
    "vacant": "false",
    "lang": "sv"
}
base = 'http://www.jm.se'

def get_jm_json(**options):
    url = options.get('url')
    url = url if url else ajax

    result = {}
    obj_per_page = 60
    r = requests.post(url, data=params)
    j = r.json()['SearchResultData']
    count_obj = j['HitCountObjects']
    pages = count_obj / obj_per_page
    obj_last_page = count_obj % obj_per_page
    pages  = pages + 1 if obj_last_page else 0

    for p in range(pages):
        params['p'] = p + 1
        r = requests.post(url, data=params)
        j = r.json()['SearchResultData']
        for o in j['SearchResultsObjects']:
            data = [o['ProjectName'],
                    o['StatusName'],
                    o['Area'],
                    o['Url'],
                    o['ObjectImageUrl']
                    ]
            result[o['PageId']] = data

    # Some actions with saved objects
    estates = Estate.objects.filter(is_publish=True)
    for est in estates:
        # Check and change status for existing objects
        try:
            obj = result.pop(est.pageid)
            if est.status != obj[1]:
                est.status = obj[1]
                est.save()
        except KeyError:
            # Unpublish missed objects
            est.is_publish = False
            est.save()

    # Save
    for rec in result:
        try:
            img_url = base + result[rec][4]

            estate = Estate(pageid=rec,
                            title=result[rec][0],
                            status=result[rec][1] if result[rec][1] else '',
                            area=result[rec][2],
                            url=base+result[rec][3])
            name = urlparse(img_url).path.split('/')[-1]
            content = urllib.urlretrieve(img_url)

            estate.image.save(name, File(open(content[0])), save=True)
        except Exception as e:
            print e
            print rec


