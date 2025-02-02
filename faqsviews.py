from django.core.cache import cache

class FAQViewSet(viewsets.ModelViewSet):
    ...

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)
        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, timeout=60 * 15)  # Cache for 15 minutes
        return response