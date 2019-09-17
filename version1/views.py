
from rest_framework import viewsets, response, status


from version1.serializers import \
    SingleVlanSerializer

# Create your views here.


class ShowConfigs(viewsets.ViewSet):

    def get_serializer(self, data=None):
        return SingleVlanSerializer(data=data)

    def ShowConfig(self, request):
        data = request.data
        serializer=SingleVlanSerializer(data=data)
        if serializer.is_valid():
            print('done')

        response_result = 'test ok'
        return response.Response(data=response_result, status=status.HTTP_200_OK)