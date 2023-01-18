from django.shortcuts import render
from rest_framework.decorators import api_view
from newsappAPI.models import Item
from newsappAPI.serializers import ItemSerializer
from django.core.paginator import Paginator, EmptyPage

@api_view(['GET'])
def latestView(request):
    items = Item.objects.all().exclude(type="comment")
    query_dict = request.GET
    query = query_dict.get("query")
    type = query_dict.get("type")
    page = query_dict.get("page")
    ordering = query_dict.get("ordering")

    if query is not None:
        items = items.filter(text__icontains=query)

    if not ordering:
        ordering = "title"

    ordering_fields = ordering.split(",")
    if items and ordering_fields:
        items = items.order_by(*ordering_fields)

    if items and type :
        items = items.filter(type=type)

    per_page = 5
    if not page:
        page = 1
    paginator = Paginator(items, per_page=per_page)
    try:
        items = paginator.page(number=page)
    except EmptyPage:
        items = None

    context = {"object": items}
    return render(request, "newsappweb/news.html", context)


@api_view(['GET'])
def newsDetailView(request, id):
    query_dict = request.GET
    query = query_dict.get("query")
    type = query_dict.get("type")
    page = query_dict.get("page")
    ordering = query_dict.get("ordering")

    items = Item.objects.all()
    if id:
        items = items.filter(parent=id)

    if not ordering:
        ordering = "title"

    ordering_fields = ordering.split(",")
    if items and ordering_fields:
        items = items.order_by(*ordering_fields)

    if items and type :
        items = items.filter(type=type)

    per_page = 5
    if not page:
        page = 1
    paginator = Paginator(items, per_page=per_page)
    try:
        items = paginator.page(number=page)
    except EmptyPage:
        items = None

    context = {"object": items}
    return render(request, "newsappweb/news.html", context)

