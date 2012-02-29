from django.conf import settings


def articles(request):
    return {
        'ARTICLES_NUM': settings.ARTICLES_NUM
    }
