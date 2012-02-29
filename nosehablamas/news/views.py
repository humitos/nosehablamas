from django.shortcuts import render_to_response
from django.template import RequestContext

from news.models import News


def home(request):
    if request.method == 'GET':
        news = News.objects.all().order_by('-posted_at')
        kwargs = {
            'news': news,
        }
        context = RequestContext(request, kwargs)
        return render_to_response('news/home.html',
                                  context_instance=context)
