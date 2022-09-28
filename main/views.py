from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import InboxMessage, OutboxMessage
from main.serializers import (
    UpSerializer, OngoingSerializer, InboxSerializer,
    FromDevSerializer, ToDevSerializer)
import time

# Create your views here.


@api_view(['POST', 'GET', 'DELETE'])
def outbox(request):
    '''
    Kirim payload, dapatkan message dalam proses,
    atau hapus message tertentu di outbox
    '''
    if request.method == 'POST':
        serializer = UpSerializer(data=request.data)

        if serializer.is_valid():
            time.sleep(2)

            message = OutboxMessage(
                payload=serializer.data['payload'],
                data_type=serializer.data['dataType']
            )
            message.save()

            return Response({
                'success': True,
                'message': 'message queued to outbox',
            })

        return Response({
            'success': False,
            'message': serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        time.sleep(2)

        messages = OutboxMessage.objects.filter(
            ongoing=True, deleted=False).order_by('created_at')

        # Auto update status
        for message in messages:
            if message.status < 2:
                message.status = message.status + 1
            else:
                message.ongoing = False
            message.save()

        serializer = OngoingSerializer(messages, many=True)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        id = request.GET.get('id')

        if id:
            time.sleep(2)

            message = OutboxMessage.objects.filter(id=id).first()

            if message is not None:
                message.deleted = True
                message.save()

                return Response({
                    'success': True,
                    'message': 'message id deleted from outbox',
                })

        return Response({
            'success': False,
            'message': 'message id not found',
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'DELETE'])
def inbox(request):
    '''
    Dapatkan message atau hapus message tertentu di inbox
    '''
    if request.method == 'GET':
        time.sleep(2)

        messages = InboxMessage.objects.filter(
            deleted=False).order_by('created_at')
        serializer = InboxSerializer(messages, many=True)

        return Response(serializer.data)

    elif request.method == 'DELETE':
        id = request.GET.get('id')

        if id:
            time.sleep(2)

            message = InboxMessage.objects.filter(id=id).first()

            if message is not None:
                message.deleted = True
                message.save()

                return Response({
                    'success': True,
                    'message': 'message id deleted from outbox',
                })

        return Response({
            'success': False,
            'message': 'message id not found',
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def from_dev(request):
    messages = OutboxMessage.objects.filter(
        deleted=False, ongoing=False).order_by('created_at')
    serializer = FromDevSerializer(messages, many=True)

    return Response({
        'success': True,
        'data': [{
            'imei': '300434066218150',
            'data': serializer.data,
        }]
    })


@api_view(['POST'])
def to_dev(request):
    serializer = ToDevSerializer(data=request.data)

    if serializer.is_valid():
        message = InboxMessage(
            payload=serializer.data['payload'],
            data_type=serializer.data['dataType']
        )
        message.save()

        return Response({
            'success': True,
            'data': 'OK,2163231',
        })

    return Response({
        'success': False,
        'data': 'FAILED,12,RockBLOCK has no line rental',
    })
