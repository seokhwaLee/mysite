from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline): #admin.TabularInline:테이블 형식 / admin.StackedInline : 따로따로 한줄씩 쌓음
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text'] #fields를 직접 명시해서 보여지는 데이터 순서를 변경할 수 있음
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] #pub_date필터할수있는 창 생김
    search_fields = ['question_text'] #question_text를 검색할 수 있는 검색창 생성
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields': ['pub_date']}), #다른 필드를 data information에 추가하고 싶으면 pub_date뒤에 추가해주면 된다.
    ]
    inlines = [ChoiceInline]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)  #QuestionAdmin에서 choice를 관리할 수 있도록 설정할 것