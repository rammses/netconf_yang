from rest_framework import serializers

class SingleVlanSerializer(serializers.Serializer):
    vlanid = serializers.CharField(required=True)
    vlan_name = serializers.CharField(required=True)

