import datetime
from haystack import indexes
from blog.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    title = indexes.CharField(document=True)
    created_date = models.DateTimeField(default=timezone.now(), model_attr='created_date')
	published_date = models.DateTimeField(blank=True, null=True,model_attr='published_date')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(published_date__lte=datetime.datetime.now())
