from django.db import models
from django.utils import timezone

class EnableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=True)

class Period(models.Model):
    created_date = models.DateTimeField(null=False, auto_now_add=True)
    updated_date = models.DateTimeField(null=False, default=timezone.now)
    # 역참조 시 위에 선언한 Manager가 사용된다.
    objects = models.Manager()
    enabled_objects = EnableManager()

    class Meta:
        # 추상 모델을 설정(migrate 시 해당 모델의 테이블 생성X)
        abstract = True

