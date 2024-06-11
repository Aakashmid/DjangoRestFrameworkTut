from rest_framework.pagination import LimitOffsetPagination

# we can make this class in other file pagination.py 
class CustomPagination(LimitOffsetPagination):
    default_limit=4   #default record at one page will be four
    max_limit=9  # max limit that client can pass parameter would be 9
    limit_query_param='r_limit'
    offset_query_param='myoffset'
