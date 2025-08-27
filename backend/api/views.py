from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from .models import Post
from .models import Contact
from .serializers import PostSerializer, FeedbackSerializer

class PostViewSet(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        
        if self.request.method == 'POST':
            serializer.save(author=self.request.user)
            return [permissions.IsAuthenticated()]  # Only you can create
            
        return [permissions.AllowAny()]  # Everyone can view
    
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
  # Only logged-in users can edit/delete

    def perform_update(self, serializer):
        
        if (self.request.method == 'POST') or (self.request.method == 'PUT') or (self.request.method == 'DELETE'):
            serializer.save(author=self.request.user)
            return [permissions.IsAuthenticated()]  # Only you can create
            
        return [permissions.AllowAny()]  # Everyone can view
    
class Feedback(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAuthenticated()]  # Only logged-in users can view
        return [permissions.AllowAny()]  # Everyone can POST

    def perform_create(self, serializer):
            serializer.save()
            return [permissions.AllowAny()]  # Everyone can view

            
        
        

        
    