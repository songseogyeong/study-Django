from django.shortcuts import render
from django.views import View


class MainView(View):
    # get 메소드를 사용하여 요청 받기:
    def get(self, request):
        # 오류가 없다면:
        try:
            # member = member 섹션을 담기
            # 자동으로 역직렬화된다.
            member = request.session['member']

        # KeyError 발생 시:
        except KeyError:
            # member = member의 값은 없다.
            member = None

        # render를 통해 main.html로 페이지 이동
        # main.html 속 context의 member의 값을 member 섹션 객체로 받아오기
        return render(request, 'main.html', context={'member': member})
