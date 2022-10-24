from django.contrib import admin
from .models import Order, StatusCrm, ComentCrm


# Register your models here.
class Coment(admin.StackedInline):
    # Модель, поля которой будут объединены с выбранной админ-панелью
    model = ComentCrm
    fields = ('coment_dt', 'coment_text')
    readonly_fields = ('coment_dt',)
    # Количество блоков (элементов) модели, которые отображаются для выбранного элемента админ-панели
    extra = 1


# Класс кастомизации панели приложения в админ-панели
class OrderAdm(admin.ModelAdmin):
    # Поля, которые отображаются в панели приложения
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    # Поля, при нажатии на которые открывается редактирование элемента
    list_display_links = ('id', 'order_name')
    # Добавляет поле поиска и указывает поля, по которым будет выполняться поиск
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    # Добавляет панель фильтра и указывает поля, по которым будет происходить фильтрация элементов
    list_filter = ('order_status',)
    # Указывает поля элемента, которые можно редактировать в панели приложения
    list_editable = ('order_status', 'order_phone')
    # Количество элементов, которые будут отображаться на одной "странице"
    list_per_page = 10
    # Максимальное количество элементов, которые будут отображаться, если нажать "Показать все"
    list_max_show_all = 100
    # Поля элемента, которые отображаются при редактировании
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    # Поля только для чтения, которые отображаются при редактировании
    readonly_fields = ('id', 'order_dt')
    # Поле класса Coment
    inlines = [Coment, ]


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
admin.site.register(ComentCrm)
