from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog/', views.Blog, name="blog" ),
    path('blog-single/<int:pid>', views.Blog_single, name="blog-single"),
    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),
    path('register/', views.Register, name="register"),
    path('profile/', views.Profile, name="profile"),
    path('create_post', views.Create_Post, name="create_post"),
    path('update_post/<int:uid>', views.Update_Post, name="update_post"),
    path('delete_post<int:uid>', views.Delete_Post,name="delete_post"),
    path('authors', views.Authors, name="authors"),
    path('create_author', views.Create_Author, name="create_author"),
    path('delete_author<int:cid>', views.Delete_Author, name="delete_author"),
    path('update_auhtor<int:cid>', views.Update_Author, name="update_author"),
    path('get_user', views.Get_User, name="get_user"),
    path('delete_user<int:nid>', views.Delete_User, name="delete_user"),
    path('update_user<int:nid>', views.Update_User, name="update_user")
]