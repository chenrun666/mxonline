import xadmin

from .models import CourseOrg, CityDict, Teacher


class CityDictAdmin:
    list_display = ["name", "desc", "add_time"]
    search_fields = ["name", "desc"]
    list_filter = ["name", "desc", "add_time"]


class CourseOrgAdmin:
    list_display = ["name", "desc", "add_time", "location", "has_auth", "index", "click_nums", "fav_nums", "image",
                    "address"]
    search_fields = ["name", "desc", "location", "has_auth", "index", "click_nums", "fav_nums", "image",
                     "address"]
    list_filter = ["name", "desc", "add_time", "location", "has_auth", "index", "click_nums", "fav_nums", "image",
                   "address"]


class TeacherAdmin:
    list_display = ["name", "add_time", "work_years", "work_company", "work_position", "points", "click_nums",
                    "fav_nums"]
    search_fields = ["name", "work_years", "work_company", "work_position", "points", "click_nums", "fav_nums"]
    list_filter = ["name", "add_time", "work_years", "work_company", "work_position", "points", "click_nums",
                   "fav_nums"]


xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
