from django.db import models


class Member(models.Model):
    member_email = models.TextField(null=False, blank=False)
    member_password = models.TextField(null=False, blank=False)
    member_name = models.TextField(null=False, blank=False)

    class Meta:
        db_table = 'tbl_member'
