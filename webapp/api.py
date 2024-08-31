from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Photo, Album

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_favorites(request, item_type, item_id):
    user = request.user
    if item_type == 'photo':
        item = Photo.objects.get(id=item_id)
        if user in item.favorite_users.all():
            return Response({'error': 'Already in favorites'}, status=status.HTTP_400_BAD_REQUEST)
        item.favorite_users.add(user)
        return Response({'success': 'Added to favorites'}, status=status.HTTP_200_OK)
    elif item_type == 'album':
        item = Album.objects.get(id=item_id)
        if user in item.favorite_users.all():
            return Response({'error': 'Already in favorites'}, status=status.HTTP_400_BAD_REQUEST)
        item.favorite_users.add(user)
        return Response({'success': 'Added to favorites'}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid item type'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_favorites(request, item_type, item_id):
    user = request.user
    if item_type == 'photo':
        item = Photo.objects.get(id=item_id)
        if user in item.favorite_users.all():
            item.favorite_users.remove(user)
            return Response({'success': 'Removed from favorites'}, status=status.HTTP_200_OK)
        return Response({'error': 'Not in favorites'}, status=status.HTTP_400_BAD_REQUEST)
    elif item_type == 'album':
        item = Album.objects.get(id=item_id)
        if user in item.favorite_users.all():
            item.favorite_users.remove(user)
            return Response({'success': 'Removed from favorites'}, status=status.HTTP_200_OK)
        return Response({'error': 'Not in favorites'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Invalid item type'}, status=status.HTTP_400_BAD_REQUEST)