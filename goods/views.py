from django.http.response import HttpResponse
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from goods.serializers import TokenSerializer, GoodsSerializer
from goods.models import Token, Good
from uuid import uuid4


def validate_token(request):
    try:
        token = request.GET.get('token')
        token_exists = Token.objects.filter(token=token).exists()

        if token_exists:
            message = ""
        else:
            message = "Token must be present"
    except ValidationError:
        message = "Token is invalid"
    return message


# ---------- api ---------- #
class GetTokenApiView(APIView):
    serializer_class = TokenSerializer
    http_method_names = ['get']

    @staticmethod
    def get(request):
        new_token = uuid4()
        token_instance = Token()
        token_instance.create_token(new_token)
        return Response({'token': new_token}, status=201)


class GoodsApiView(APIView):
    serializer_class = GoodsSerializer
    http_method_names = ['get']

    @staticmethod
    def get(request):
        goods = Good.objects.all()
        serializer = GoodsSerializer(goods, many=True)
        if validate_token(request) == "":
            return Response(serializer.data)
        else:
            return HttpResponse(validate_token(request), status=401)


class NewGoodApiView(APIView):

    @staticmethod
    def get(request):
        tokens = Token.objects.all()
        serializer = GoodsSerializer(tokens, many=True)
        if validate_token(request) == "":
            return Response(serializer.data)
        else:
            return HttpResponse(validate_token(request), status=401)

    @staticmethod
    def post(request):
        good = GoodsSerializer(data=request.data)
        if validate_token(request) == "":
            if good.is_valid():
                good.save()
                return HttpResponse("<h1>Good was successfully added<br>Good id: </h1>" + str(good.instance.id))
            else:
                return Response(good.errors, status=400)
        else:
            return HttpResponse(validate_token(request), status=401)
