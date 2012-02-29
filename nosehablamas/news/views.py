import urllib2
import opengraph
import mimetypes

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.files.base import ContentFile

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from news.models import News
from news.forms import NewsForm, ArticleForm

from BeautifulSoup import BeautifulSoup


def home(request):
    if request.method == 'GET':
        news = News.objects.all().order_by('-posted_at')
        news_form = NewsForm()
        article_form = ArticleForm()
        kwargs = {
            'news': news,
            'news_form': news_form,
            'article_form': article_form,
        }
        context = RequestContext(request, kwargs)
        return render_to_response('news/home.html',
                                  context_instance=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success('Se agrego correctamente la noticia.')
            return redirect('news__home')
        else:
            kwargs = {
                'form': form,
            }
            context = RequestContext(request, kwargs)
            return render_to_response('news/home.html',
                                      context_instance=context)


def _parse_title(graph, soup):
    if graph.is_valid():
        title = graph.get('title', False)
        if title:
            return title
    # if no opengraph or no title
    return soup.find('title').text


def _parse_description(graph, soup):
    if graph.is_valid():
        description = graph.get('description', False)
        if description:
            return description
    # if no opengraph or no title
    return soup.find('p').text


def _parse_image(graph, soup):
    if graph.is_valid():
        image = graph.get('image', False)
        if image:
            mimetype = mimetypes.guess_type(image)
            content = ContentFile(urllib2.urlopen(image).read())
            return mimetype, content
    else:
        # if no opengraph or no title
        images = soup.findAll('img')
        val = URLValidator(verify_exists=True)
        for i in images:
            try:
                image_url = i.get('src')
                val(image_url)
                mimetype = mimetypes.guess_type(image_url)
                content = ContentFile(urllib2.urlopen(image_url).read())
                return mimetype, content
            except ValidationError:
                continue
    return 'jpg', ContentFile('')


def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # Parse link
            article = form.save(commit=False)
            soup = BeautifulSoup(urllib2.urlopen(article.url).read())
            graph = opengraph.OpenGraph(url=article.url)

            article.title = _parse_title(graph, soup)
            article.description = _parse_description(graph, soup)
            extension, content = _parse_image(graph, soup)
            article.save()
            article.image.save('article-%d.%s' % (article.id, extension),
                               content)
            article.save()

            messages.success(request, 'Se agrego correctamente el articulo.')
            return redirect('news__home')
        else:
            messages.error(request, 'Se produjo un error al '
                           'agregar ese articulo.')
            return redirect('news__home')
