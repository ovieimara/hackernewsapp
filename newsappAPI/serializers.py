from rest_framework import serializers
from .models import Item
from django.http import Http404


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'item_id', 'deleted', 'type', 'by', 'time', 'text', 'dead', 'parent', 'kids', 'score', 'title', 'descendants', 'poll', 'parts', 'url']
        
    
    def create(self, validated_data):
        # print('validated_data: ', validated_data)
        item_id = validated_data.get('item_id')
        if item_id:
            item = Item.objects.filter(item_id=item_id)
            if item.exists():
                return super().update(item.first(), validated_data)
        return super().create(validated_data)