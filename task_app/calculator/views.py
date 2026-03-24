from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def add_two_numbers(request: Request):
    a = int(request.query_params.get('a'))
    b = int(request.query_params.get('b'))

    reult = a+b
    return Response({
        'a': a,
        'b': b,
        'result': a + b
    })