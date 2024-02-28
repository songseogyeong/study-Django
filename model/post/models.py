from django.db import models
from member.models import Member
from model.models import Period


class Post(Period):
    # CASCADE : ForeignKeyField를 포함하는 모델 인스턴스(row)도 같이 삭제한다.
    # PROTECT : 해당 요소가 같이 삭제되지 않도록 ProtectedError를 발생시킨다.
    # SET_NULL : ForeignKeyField 값을 NULL로 바꾼다. null=True일 때만 사용할 수 있다.
    # SET_DEFAULT : ForeignKeyField 값을 default 값으로 변경한다. default 값이 있을 때만 사용할 수 있다.
    # SET() : ForeignKeyField 값을 SET에 설정된 함수 등에 의해 설정한다.
    # DO_NOTHING : 아무런 행동을 취하지 않는다. 참조 무결성을 해칠 위험이 있어서 잘 사용되지는 않는다.
    post_title = models.CharField(max_length=50, null=False, blank=False)
    post_content = models.CharField(max_length=300, null=False, blank=False)
    member = models.ForeignKey(Member, null=False, on_delete=models.PROTECT)

    class Meta:
        db_table = 'tbl_post'
        ordering = ['-id']