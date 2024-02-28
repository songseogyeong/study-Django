from django.db import models

from member.models import Member
from post.managers import PostManager


class Post(models.Model):
    post_title = models.CharField(null=False, blank=False, max_length=30)
    post_content = models.TextField(null=False, blank=False)
    post_view_count = models.BigIntegerField(null=False, blank=False, default=0)
    # False: 삭제, True: 게시중
    post_status = models.BooleanField(null=False, blank=False, default=True)
    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.PROTECT)

    objects = models.Manager()
    enabled_objects = PostManager()

    class Meta:
        db_table = 'tbl_post'
        ordering = ['-id']

    def get_absolute_url(self):
        return f'/post/detail/?id={self.id}'
