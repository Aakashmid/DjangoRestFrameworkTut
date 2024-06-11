from rest_framework.pagination import CursorPagination

# we can make this class in other file pagination.py 
class CustomPagination(CursorPagination):
    page_size=4 # how many records will be on one page 
    ordering='name'
    cursor_query_param='mycursor'