from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    class Meta:
        ordering = ['-id']  # 최신 글부터 출력
