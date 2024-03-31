from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from API_server import serializers

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs']
        
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            print(serializer.validated_data)
            return Response({'message': f'Hello {name}'})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    
    def patch(self, request):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request):
        """Delete an object"""
        return Response({'method': 'DELETE'})