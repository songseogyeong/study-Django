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

class PostFile(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, null=False)
    # 경로 =  %Y/%m/%d = 연도/월/일 = 현재시간을 기준으로 자동으로 들어감!
    # 풀경로 문자열을 파일 이름으로 지정됨!
    path = models.ImageField(null=False, blank=False, upload_to='post/%Y/%m/%d')

    class Meta:
        db_table = 'tbl_post_file'
