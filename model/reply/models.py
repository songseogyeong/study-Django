from django.db import models
from model.models import Period
from member.models import Member
from post.models import Post


class Reply(Period):
    PRIVATE_STATUS = [
        (True, '비밀 댓글'),
        (False, '일반 댓글')
    ]

    reply_content = models.TextField(blank=False, null=False)
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    group_id = models.BigIntegerField(null=False, default=1)
    reply_depth = models.BigIntegerField(null=False, default=1)
    reply_private_status = models.BooleanField(null=False, default=1, choices=PRIVATE_STATUS)

    class Meta:
        db_table = 'tbl_reply'
        ordering = ['-id']

    def __str__(self):
        return self.reply_content

