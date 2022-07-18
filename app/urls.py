from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.InsertPageView,name="insertpage"),  
    path("insert/",views.InsertData,name="insert"),  
    path("show/",views.read,name="show"),
    path("update/<int:id>",views.update,name="update"),
    path("save/<int:id>",views.save,name="save"),
    path("delete/<int:id>",views.delete,name="delete"),
]
