import xadmin

from .models import Course, Lesson, Video, CourseResource


class CourseAdmin:
    list_display = ["name", "desc", "detail", "degree", "learn_times", "students", "fav_nums", "image", "click_num",
                    "add_time"]
    search_fields = ["name", "desc", "detail", "degree", "learn_times", "students", "fav_nums", "image", "click_num",
                     "add_time"]
    list_filter = ["name", "desc", "detail", "degree", "learn_times", "students", "fav_nums", "image", "click_num",
                   "add_time"]


class LessonAdmin:
    list_display = ["name", "course", "add_time"]
    search_fields = ["name", "course"]
    list_filter = ["name", "course__name", "add_time"]


class VideoAdmin:
    list_display = ["name", "lesson", "add_time"]
    search_fields = ["name", "lesson"]
    list_filter = ["name", "lesson", "add_time"]


class CourseResourceAdmin:
    list_display = ["name", "course", "download", "add_time"]
    search_fields = ["name", "course", "download"]
    list_filter = ["name", "course", "download", "add_time"]


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
