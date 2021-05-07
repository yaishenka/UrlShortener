from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, mixins, permissions
from rest_framework.decorators import permission_classes
from rest_framework.views import Response

from .models import Url
from .serializers import UrlSerializer


def goodby(request):
    return HttpResponse("Unknown url!")


def goto(request, link):
    try:
        url = Url.objects.get(short_url=link)
    except Url.DoesNotExist:
        return HttpResponse("Unknown url!")

    link = url.full_url
    url.used += 1
    url.save()
    return redirect(link)


@permission_classes((permissions.IsAuthenticated,))
class ListAllUrls(generics.ListAPIView):
    serializer_class = UrlSerializer

    def get_queryset(self):
        queryset = Url.objects.filter(creator=self.request.user)
        return queryset

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@permission_classes((permissions.IsAuthenticated,))
class UrlManagerView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = UrlSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

    def get_object(self):
        return get_object_or_404(Url, short_url=self.request.data["short_url"])

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
