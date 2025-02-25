from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all().order_by('-created_at')
    print("create")
    serializer_class = RecipeSerializer
