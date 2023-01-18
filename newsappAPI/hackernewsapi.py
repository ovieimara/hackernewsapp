# Create your views here.
import requests
from .constants import item_url, max_id_url, hacker_news_urls, count
from .models import Item
from rest_framework import status
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from django.http import Http404
from concurrent.futures import ThreadPoolExecutor
import concurrent
from datetime import datetime

status = [0]

def get_latest_news(url):
    response = requests.get(url)

    try:
        response.raise_for_status()
        return response.json()
    except:
        return list

def update_news():
    data = dict
    max_id_item = 0

    if status[0] == 1:
        return
    
    status[0] = 1
    print(f"STARTING JOB: {status[0]}")
    try:
        item = Item.objects.all().order_by('item_id')
        if item.exists():
            max_id_item = item.first().item_id 
            max_id_item = max_id_item if max_id_item else 0
    except Item.DoesNotExist:
        print(status.HTTP_404_NOT_FOUND)

    max_id = get_latest_news(max_id_url)
    id_diff = max_id - max_id_item
    try:
        if id_diff > 0:
            now = int(round(datetime.now().timestamp()))
            now_hash = hash(now)
            hacker_news_url = hacker_news_urls[now_hash % len(hacker_news_urls)]
            response = get_latest_news(hacker_news_url)
            data = storeItems(response[:count])
    except Exception as e:
        print(e)
    finally:
        status[0] = 0

    print(f"STOPPING JOB: {status[0]}")
    return data


def getItem(item, kids):
    response = get_latest_news( f"{item_url}{item}.json?print=pretty")
    if response.get('id'):
        id = response.pop('id')
        response['item_id'] = id
        response['source'] = 'HN'
        kids.append(response.get('kids'))

    return response

def getKids(items, items_arr):
    for item in items:
        response = get_latest_news( f"{item_url}{item}.json?print=pretty")
        id = response.pop('id')
        response['item_id'] = id
        response['source'] = 'HN'
        items_arr.append(response)

    return items_arr

def storeItems(items):
    data = []
    kids_dict = []
    with ThreadPoolExecutor() as executor:
        future_to_url = [executor.submit(getItem, item, kids_dict) for item in items]
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                f = future.result()
                data.append(f)
                print(f"downloading......{len(data)}--->{item_url}{f.get('item_id')}.json?print=pretty")
            except Exception as e:
                print('Looks like something went wrong:', e)
    

    with ThreadPoolExecutor() as executor:
        future_to_url = [executor.submit(getKids, kids_arr, data) for kids_arr in kids_dict]
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                f = future.result()
                # kids_data.append(f)
                print(f"downloading kids......{len(data)}")
            except Exception as e:
                print(f"Looks like something went wrong: {e}")
    

    items_serializer = ItemSerializer(data=data, many=True)
    items_serializer.is_valid(raise_exception=False)
    items_serializer.save()

    return items_serializer.data
 