from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):        
            
        if [form.cleaned_data['is_main'] for form in self.forms if form.cleaned_data].count(True) == 1:
            # В form.cleaned_data будет словарь с данными каждой отдельной формы, которые вы можете проверить 
            return super().clean() # вызываем базовый код переопределяемого метода 
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен, а пользователю выведется соответствующее сообщение об ошибке 
        else:
            raise ValidationError('Основной раздел должен быть только один')  

    # -------- 2-ой способ для наглядности-----------------   
        # list_main_tags = []      
        # for form in self.forms:
        #     if form.cleaned_data:  
        #         list_main_tags.append(form.cleaned_data['is_main'])        
        # if list_main_tags.count(True) == 1:
        #     return super().clean()                
        # else:
        #     raise ValidationError('Основной раздел должен быть только один')


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'published_at']
    list_display_links= ['id', 'title']
    inlines = [ScopeInline,]


    
