from django.views.generic.base import TemplateView


class ArticlesView(TemplateView):
    template_name = 'blog/articles.html'

articles = ArticlesView.as_view()
