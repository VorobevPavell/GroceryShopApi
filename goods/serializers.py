from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from goods.models import Token, Good


class TokenSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Token

    def validate(self, value):
        token_exist = Token.objects.filter(token=value).exists()
        if token_exist:
            return True
        else:
            return False


class GoodsSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Good

    def validate(self, value):
        amount = value.get('amount', 'none')
        price = value.get('price', 'none')
        if price < 0:
            raise ValidationError('Price must be more than 0')
        if amount < 0:
            raise ValidationError('Amount must be more than 0')
        if price > 0 and amount > 0:
            return value
