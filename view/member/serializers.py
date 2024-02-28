from rest_framework import serializers

from member.models import Member


# 직렬화
# 주솟값을 json(문자열) 값으로 변환

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        # Member 모델의
        model = Member
        # 모든 필드를 직렬화 하기
        fields = '__all__'