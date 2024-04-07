from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug = models.SlugField(unique=True)
    content = models.TextField()

    def get_ancestors(self):
        ancestors = []
        parent = self.parent
        while parent:
            ancestors.insert(0, parent)
            parent = parent.parent
        return ancestors

    def __str__(self):
        return self.title

