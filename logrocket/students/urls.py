from django.urls import re_path
from .views import students_list, students_detail

urlpatterns = [
    # will handle both creations (POST) and listing (GET):
    re_path(r"students/$", students_list),
    # will remove (DELETE) or update (PUT) the data of a single student:
    re_path(r"students/([0-9])$", students_detail),
]

"""
When the paths and converters syntax are not sufficient
for defining your URL patterns,
you can also use regular expressions.
To do so, use re_path() instead of path().

Explanation:
^ asserts position at start of a line
([0-9]) a single character present in the list below [0-9] (case sensitive)
$ asserts position at the end of a line
"""
