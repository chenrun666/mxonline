import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting:
    enable_themes = True
    use_bootswatch = True


class EmailVerifyRecordAdmin:
    list_display = ["code", "email", "send_type", "send_time"]  # 展示列
    search_fields = ["code", "email", "send_type"]  # 搜索字段
    list_filter = ["code", "email", "send_type", "send_time"]  # 筛选字段


class BannerAdmin:
    ist_display = ["title", "image", "url", "index", "add_time"]  # 展示列
    search_fields = ["title", "image", "url", "index"]  # 搜索字段
    list_filter = ["title", "image", "url", "index", "add_time"]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)  # 使用主题功能
