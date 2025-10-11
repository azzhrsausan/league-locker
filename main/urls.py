from django.urls import path
from main.views import show_main, create_item, show_item, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_item
from main.views import delete_item
from main.views import add_item_ajax



app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item/', create_item, name='create_item'),
    path('item/<str:id>/', show_item, name='show_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:item_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:item_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('item/<uuid:id>/edit', edit_item, name='edit_item'),
    path('item/<uuid:id>/delete', delete_item, name='delete_item'),
    path('create-item-ajax', add_item_ajax, name='add_item_ajax'),
]