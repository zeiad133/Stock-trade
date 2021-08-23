from rest_framework import serializers

# Serializers define the API representation.


class OrderFormSerializer(serializers.Serializer):
  def validate(self, data):
    if data['lower_bound'] > data['upper_bound']:
        raise serializers.ValidationError({"Lower bound": "upper bound must greater than lower bound"})
    return data
  total = serializers.IntegerField(required=True, min_value= 1)
  user_id = serializers.IntegerField(required=True, min_value= 1)
  stock_id = serializers.CharField(required=True, max_length=200)
  upper_bound = serializers.IntegerField(required=True, min_value= 1)
  lower_bound = serializers.IntegerField(required=True, min_value= 1)
