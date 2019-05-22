import random

from rest_framework.views import APIView
from rest_framework.response import Response

from .helpers import BoardHelper


class OseroView(APIView):
    def post(self, request):
        your_stone = request.data["your_stone"]
        squares = request.data["squares"]
        can_put_list = BoardHelper.get_can_put_list(squares, your_stone)

        point = random.choice(can_put_list)

        return Response({
            "x": point[0],
            "y": point[1],
        })
