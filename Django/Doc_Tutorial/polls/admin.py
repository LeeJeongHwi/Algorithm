from django.contrib import admin
from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model=Choice
    extra =3
    #Choice 모델을 위한 옵션 클래스
    #[StackedInline] 클래스를 상속 받음 / TabularInline으로 변경
    #이 클래스를 QuestionAdmin 클레스에 inlines 클래슬 변수에 추가
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information',{'fields':['pub_date']}),
    ]
    list_display = ('question_text','pub_date','was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date'] #필터 기능
    search_fields = ['question_text'] #검색 기능

# fieldsets 변수를 이용해 입력/수정 화면에서 각 항목들을 그룹화 하고 그룹의 이름까지 설정 할 수 있음
admin.site.register(Question,QuestionAdmin)


# Register your models here.
