"""
API's for bitcoin app.
"""
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Bitcoin
from .serializers import BitcoinSerializer


class BitCoinApiView(generics.GenericAPIView):
    serializer_class = BitcoinSerializer
    queryset = Bitcoin.objects.all()
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        serializer = self.serializer_class(
            self.queryset.exclude(price=0), many=True
        )
        return Response(serializer.data)
