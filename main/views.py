from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.serializers import UpSerializer
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
            # return Response(serializer.data)
            time.sleep(2)

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

        return Response([
            # {
            #     # SOS Attempt 1
            #     'id': 0,
            #     'payload': 'sZPpC37SAVagSJ7oLB0OhLbE46Xr6/W167f7T7bjoLY=',
            #     'dataType': 'TEXT',
            #     'status': 1,
            # },
            # {
            #     # Fishpoint
            #     'id': 1,
            #     'payload': 'BSGtpoexRIPItsdaJ+5Tx7bE46Xr6/W167f7T7bjoLY=',
            #     'dataType': 'TEXT',
            #     'status': 2,
            # },
            # {
            #     # Logbook
            #     'id': 2,
            #     'payload': 'Or/4WbUm80bTH6WTSxr41O1rKfy6OIDIvYp2NDQ/SF8=',
            #     'dataType': 'TEXT',
            #     'status': 0,
            # },
        ])

    elif request.method == 'DELETE':
        id = request.GET.get('id')

        if id:
            time.sleep(2)
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

        return Response([
            # {
            #     # SOS failed response
            #     'id': 0,
            #     'payload': '43d1pfLHfRGrX/Py6h4yFkvlUO/2hBoS6r2Lw/obzPA=',
            #     'dataType': 'TEXT',
            #     'receivedAt': 1655975751,
            # },
            {
                # SOS success response
                'id': 1,
                'payload': '+ESdE5As2msp6icLbzEJ1+MnnP8YNbQwW93hP9n+t8Q=',
                'dataType': 'TEXT',
                'receivedAt': 1655975752,
            },
            # {
            #     # Fishpoint response
            #     'id': 2,
            #     'payload': 'ZNUl61XpxoC433T97NFNeANQ93hJFBt8PtGG/hDNzqUBKRTH7M5QMURjL2HEazD7YF6UFFIWyjxECHyVKNnyv3IBIyqKGT0KqiydzkPQUt8=',
            #     'dataType': 'TEXT',
            #     'receivedAt': 1655975753,
            # },
            {
                # Fishpoint response dekat JKT
                'id': 3,
                'payload': 'GCZ+MUyRwqcyLO+HSR76qohGl3waDVqE58v7usDZu3294dHENcWRCi1c6j1VygRFKkhv5+NyU8vNRRzn7D+SGlH9jFrxlFr1SLfK81rcapZK0XNcX4HuEJY2tQuAyZzl',
                'dataType': 'TEXT',
                'receivedAt': 1655975754,
            },
            {
                # Logbook Response
                'id': 4,
                'payload': 'Bh5c7h0e2wabR9alZEoNT3dn05XAB7gEpFZwWYdvc4Q=',
                'dataType': 'TEXT',
                'receivedAt': 1655975755,
            },
        ])

    elif request.method == 'DELETE':
        id = request.GET.get('id')

        if id:
            time.sleep(2)
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
    return Response({
        'success': True,
        'data': [{
            'imei': '300434066218150',
            'data': [
                {
                    # Logbook
                    'dataType': 'TEXT',
                    'payload': 'AWBDcWtFKRJYSF1ODTtn082axLpxpal4OPRYASFhgyQ=',
                    'bytes': 44,
                    'creditUsage': 0,
                    'transmitTime': '22-06-01 08:02:40'
                },
                {
                    # SOS
                    'dataType': 'TEXT',
                    'payload': 'vMWrA6YO1Uz0zYSQpErHmtgebK+ZvVWBMtfZLQyatnc=',
                    'bytes': 44,
                    'creditUsage': 0,
                    'transmitTime': '22-06-02 08:03:36'
                },
                {
                    # Fishpoints
                    'dataType': 'TEXT',
                    'payload': 'BSGtpoexRIPItsdaJ+5Tx7bE46Xr6/W167f7T7bjoLY=',
                    'bytes': 44,
                    'creditUsage': 0,
                    'transmitTime': '22-06-03 08:04:36'
                },
            ],
        }],
    })


@api_view(['POST'])
def to_dev(request):
    return Response({
        'success': True,
        'data': 'OK,2163231',
    })
