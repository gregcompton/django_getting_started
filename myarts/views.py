from myarts.models import Article
from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class ArticleListView(OwnerListView):
    model = Article
    # By convention:
    # template_name = "myarts/article_list.html"


class ArticleDetailView(OwnerDetailView):
    model = Article


class ArticleCreateView(OwnerCreateView):
    model = Article # this is the database
    # List the fields to copy from the Article model to the Article form
    fields = ['title', 'text'] # this is the form


class ArticleUpdateView(OwnerUpdateView):
    model = Article  # this is the database
    fields = ['title', 'text']  # this is the form
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']


class ArticleDeleteView(OwnerDeleteView):
    model = Article
