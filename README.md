# Framework
라이브러리란, 개발자가 작성해놓은 코드 파일을 의미하고, </br>
API란, 여러 라이브러리가 모여있는 압축파일을 의미한다. </br>
 * 사용자가 폴더를 관리하기 때문에 주체는 사용자가 된다.
</br></br>

Framework란, API가 굉장히 많이 모여져서 덩치가 커져있는 것을 의미한다. 
* 프레임워크가 설정을 관리하기 때문에 주체는 프레임워크가 된다.
</br></br>

### 1. Framework 장점
개발에 필요한 구조를 이미 코드로 만들어 놓았기 때문에 실력이 부족한 개발자라 하더라도 </br>
반쯤 완성된 상태에서 필요한 부분을 조립하는 형태의 개발이 가능하다.
</br></br>

회사 입장에서는 Framwork를 사용하면 일정한 품질이 보장되는 결과물을 얻을 수 있고, </br>
개발자 입장에서는 완성된 구조에 자신이 맡은 서비스에 대한 코드를 개발해서 넣기 때문에 </br>
개발 시간을 단축할 수 있다.
</br></br>

## Ⅰ. Django Framework
파이썬으로 만들어진 오픈 소스 웹 애플리케이션 프레임워크이며, </br>
빠르고 쉽게 웹 사이트를 개발할 수 있는 구성 요소로 이루어진 웹 프레임워크이다.
</br></br>

### 1. Django Framework의 특징
① MVT 패턴 (소프트웨어 디자인 설계 패턴) </br>
Model: 테이블에 저장되어 있는 데이터를 불러온 뒤 담아놓는 역할 (모델 객체 생성) </br>
* DB 중심 > 파이썬 class로 모델 객체를 생성
* 모델 종류 두개 db랑 똑같은 거 1개, 화면에서 뿌릴거 1 개
</br></br>

View: 테이블에 접근한 뒤 화면에서 사용할 Model 객체를 완성시킨다.
* html > view > html
</br></br>

Templates: 클라이언트에게 보여질 화면 구성, 전달받은 Model 객체를 사용한다.
</br></br>

② 강력한 ORM </br>
ORM(Object Relational Mapping)은 객체 관계 매핑이며, </br>
객체 진영과 RDB 진영의 구조 차이를 자동으로 해결해주는 기술의 총칭이다. </br>
오로지 객체를 중심으로 설계가 가능하며, 직접 SQL문을 작성하지 않아도 </br>
자동으로 쿼리가 생성되어 실행된다.
</br></br>

③ 자체 템플릿 지원 </br>
HTML에서 연산이 가능하도록 도와주며, 자체 템플릿 태그가 있기 때문에 </br>
동적인 페이지를 구성할 수 있게 해준다.
</br></br>

④ 소스코드 변경 감지 </br>
.py 파일의 소스코드가 변경된다면, 이를 자동으로 감지하여 서버를 재시작해준다.
</br></br>

⑤ WAS(웹 어플리케이션 서버)에 종속적이지 않은 환경 </br>
서버를 실행하지 않아도 기능별 단위 테스트가 가능하기 때문에 </br>
버그를 줄이고 개발 시간을 단축할 수 있다.
</br></br>

### 2. Django Framework의 장점
① 확장성 </br>
객체를 기억하여 재사용할 수 있는 캐싱과 코드 재사용 기능으로 인해 확장성이 좋다.
</br></br>

② 보안 </br>
개발자가 SQL 주입, CSRF 공격 및 XSS와 같은 많은 보안 문제를 피할 수 있도록 도와준다.
</br></br>

③ 기본 라이브러리를 통한 빠른 개발 </br>
처음부터 코드를 작성하는 대신 여러 기능을 포함하는 패키지를 활용할 수 있다.
</br></br>

### 3. Django Framework의 목적
간단한 웹 앱을 제작하거나 Python을 필요로 하는 서비스들을 가볍게 제작하여, </br>
MSA로 나누어 개발하는 목적으로 사용된다.
</br></br>
</br></br>
</br></br>

# Model
Django에서 models.Model이라는 추상화된 클래스를 사용하여 데이터베이스에 테이블을 정의할 수 있다. </br>
models.Model을 상속받은 클래스로 구현할 수 있으며, 내부 클래스로 Meta 클래스를 선언할 수 있다.
</br></br>

## Ⅰ. Model Convention (협약)
모델 내 코드를 작성할 때 아래의 순서에 맞춰 작성하는 것을 권장한다.
</br></br>

1. constant for choices
2. All databases Field
3. Custom manager attributes
4. class Meta
5. def _ _ str _ _()
6. def save()
7. def get_absolute_url()
8. Any custom methods
</br></br>

### 1. constant for choices
DB에 저장할 값과 실제 화면에 보여지는 값이 다를 경우 미리 튜플 형태로 선언해 놓고 사용한다.
```
CONSTANT = [
    ('DB 저장 값', '화면 출력 값'),
    ...
]
```
* python에는 상수가 없기 때문에 tuple 사용
</br></br>

### 2. All databases Field
```
ForeignKey(to, verbose_name, related_name, related_query_name, on_delete, null)
OneToOneField(to, verbose_name, related_name, related_query_name, on_delete, null)
ManyToManyField(to, verbose_name, related_name, related_query_name, on_delete, null)
```

related_name
역참조가 필요한 다대다 또는 일대다 관계에서 유용하게 사용된다. </br>
B 필드에 a 객체를 참조 시 b.a 로 접근할 수 있으나 </br>
역참조인 a.b로는 접근할 수 없다. A 필드에 b객체가 없기 때문이다. </br>
_set 객체를 사용하면 역참조가 가능하고 a.b_set으로 역참조가 가능하다. </br>
만약, _set 객체의 이름을 다른 이름으로 사용하고자 할 때 바로 related_name을 사용한다.
</br></br>

#### 2-1. 문자열
문자열 필드는 null=False로 하고 필수 요소가 아니라면 blank=True로 설정한다. </br>
이렇게 설정하는 이유는 null과 빈 값을 "null이거나 빈 문자일 경우 빈 값이다"라고 </br>
검사할 필요 없이 빈 문자열인지로만 판단할 수 있게 되기 때문이다.
</br></br>

① 최대 길이 제한이 필요한 경우 </br>
CharField(verbose_name, max_length, choices, unique, blank, null, default) </br>
* unique 키는 작성해도 적용되지 않음
</br></br>

② 최대 길이 제한이 필요 없는 경우 </br>
TextField(verbose_name, null=False, blank=True)
</br></br>

#### 2-2. 정수
max_length를 지정하지 않고 기본적으로 byte가 정해져있다. </br></br>

PositiveSmallIntegerField(verbose_name, choices, null, default) </br>
SmallIntegerField(verbose_name, choices, null, default) </br>
IntegerField(verbose_name, choices, null, default): 4byte </br>
BigIntegerField(verbose_name, choices, null, default)
* 일반적으로 integerField 사용
</br></br>
BooleanField(verbose_name, default): 1byte
</br></br>

#### 2-3. 날짜
DateField(verbose_name, null, default) </br>
TimeField(verbose_name, null, default) </br>
DateTimeField(verbose_name, null, default)
</br></br>

① auto_now_add = True </br>
최초 한번만 자동으로 필드 값을 현재 시간으로 설정한다. </br>
보통 등록 날짜 항목으로 사용된다.
</br></br>

② auto_now = True </br>
객체가 변경될 때마다 자동으로 필드 값을 현재 시간으로 수정한다. </br>
보통 수정된 날짜 항목으로 사용된다. </br>
하지만, save()를 사용해야 적용되고 update()를 사용하면 적용되지 않는다. </br>
auto_now = True처럼 사용하고 싶다면, default = timezone.now를 사용하는 것이 올바르다.
</br>
* django.utils.timezone.now으로 설정한 뒤 update할 때 마다 그 때의 now로 넣어준다.
</br></br>

created_date = models.DateTimeField(auto_now_add = True)
</br></br>

### 3. Custom manager attributes
데이터베이스와 상호작용하는 인터페이스(틀)이며, Model.objects 속성을 통해 사용한다. </br>
Custom Manager와 Custom QuerySet을 통해 사용할 수 있으며, </br>
공통적으로 상요되는 쿼리 공통 함수로 정의할 수 있는 실제 동작들을 숨길 수 있다.
</br></br>

### 4.  class Meta
Model 클래스 안에 선언되는 내부 클래스이며, 모델에 대한 기본 설정들을 변경할 수 있다. </br>
Meta 클래스가 작동하기 위해서는 정해진 속성과 속성 값을 작성해야 하고, </br>
이를 통해 Django를 훨씬 편하게 사용할 수 있다.
</br></br>

#### 4-1. 데이터 조회 시 정렬 방법 설정
① 오름차순 </br>
ordering = ['필드명']
</br></br>

② 내림차순 </br>
ordering = ['-필드명']
</br></br>

#### 4-2. 테이블 생성 시 이름 설정
db_table = '테이블명'
</br></br>

#### 4-3. 테이블 생성할 것인지 설정
abstract = False
* True 시 ORM에서 해당 테이블 제외하고 생성
* False가 디폴트 값이기 때문에 생략 가능
</br></br>

### 5. def _ _ str _ _()
객체 조회 시 원하는 데이터를 직접 눈으로 확인하고자 할 때 사용하며, </br>
객체 출력 시 자동으로 사용되는 메소드이다. </br>
모델 필드 내에서 재정의하여 원하는 필드를 문자열로 리턴하면 </br>
앞으로 객체 출력 시 해당 값이 출력된다.
</br></br>

### 6. def save()
모델 클래스를 객체화한 뒤 save()를 사용하면 INSERT 또는 UPDATE 쿼리가  발생한다. </br>
이는 Django ORM이 save()를 구현해놨기 때문이다. </br>
save() 사용 시, INSERT 또는 UPDATE 쿼리 발생 외 다른 로직이 필요할 경우 재정의할 수 있다.
* dict 구조, key 값이 없으면 추가, key 값이 있으면 수정
</br></br>

하지만, 재정의 시 객체를 대량으로 생성하거나 수정할 때 동작하지 않는다.
</br></br>

### 7. def get_absolute_url()
모델에 대해서 상세보기(DetailView)를 제작한다면, redirect(모델 객체)를 통해 </br>
자동으로 get_absolute_url()을 호출한다. </br>
추가 혹은 수정 서비스 이후 상세보기 페이지로 이동하게 된다면, </br>
매번 redirect에 경로를 작성하지 않고 get_absolute_url()을 재정의해서 사용하는 것을 추천한다.
* absolute_url: 절대 경로
</br></br>

### 8. Any custom methods
</br></br>

### ○ 예시
```
class Member(models.Model):

    MEMBER_STATUS = [
        ('A', '관리자'),
        ('M', '일반 회원')
    ]

    member_email = models.CharField(null=False, blank=False, max_length=50)
    member_password = models.CharField(null=False, blank=False, max_length=20)
    member_name = models.TextField(null=False, blank=False)
    member_age = models.PositiveIntegerField(null=False, default=0)
    member_status = models.CharField(null=False, choices=MEMBER_STATUS, default='M')

    class Meta:
        ordering = ['-id']
        db_table = 'tbl_member'

    def __str__(self):
        return self.member_email

    # 상세보기 이동
    def get_absolute_url(self):
        return f"/member/detail/{self.id}"

    post = Post.object.all().first()
    redirect(f"/member/detail/{post.get_absolute_url()}")
```
* 위와 같이 모델 생성 가능
</br></br>
</br></br>
</br></br>
