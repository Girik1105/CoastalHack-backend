from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from . import models, serializers


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def create_community(request):
    user = request.user
    data = request.data

    
    community = models.community.objects.create(
        name = data['name'],
        description = data['description'],
        owner = user,
        cover = data['cover']
    )

    print(community)

    serializer = serializers.community_serializer(community, many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def list_community(request):
    communities = models.community.objects.all()
    
    paginator = PageNumberPagination()
    paginator.page_size = 10
    data = paginator.paginate_queryset(communities, request)
    serializer = serializers.community_serializer(data, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def edit_community(request, slug):
    user = request.user
    data = request.data

    community = models.community.objects.get(slug=slug)

    if user == community.owner:
        serializer = serializers.community_serializer(community, data = data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'Invalid Data': 'The data u entered is invalid'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_community(request, slug):
    user = request.user 
    community = models.community.objects.get(slug=slug)

    if user == community.owner:
            community.delete()
            return Response({'successful':'successfully deleted'},status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def add_remove_members(request, slug):
    user = request.user 
    community = models.community.objects.get(slug=slug)

    if user != community.owner:
        if models.member.objects.filter(user=user, community=community).exists():
            member = models.member.objects.get(user=user, community=community)
            member.delete()
            return Response({'Successful':'Member deleted sucessfully'}, status=status.HTTP_200_OK)
        else:
            member = models.member.objects.create(user=user, community=community, is_verified=True)
            serializer = serializers.member_serializer(member, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        oldest_member = models.member.objects.filter(community=community).order_by('joined_since')[1:2].first()
        community.owner = oldest_member.user
        community.save()
        return Response({'Successful':'Member deleted sucessfully'}, status=status.HTTP_200_OK)