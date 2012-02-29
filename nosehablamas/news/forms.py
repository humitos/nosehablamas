from django.forms import ModelForm

from news.models import News, Article


class NewsForm(ModelForm):

    class Meta:
        model = News
        fields = ('title', )


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ('url', 'news')
