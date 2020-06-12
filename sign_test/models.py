from django.db import models


class Users(models.Model):
    name       = models.CharField(max_length = 50)
    email      = models.CharField(max_length = 50)
    password   = models.CharField(max_length = 300)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.first_name

class Comments(models.Model) :
    UserId = models.CharField(max_length = 50)
    comment_data = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.id_data

#like 클래스 만들어서 fk로 comment랑 연결해준다.

class Likes(models.Model) :
    LikeId =  models.CharField(max_length = 50,default='')
    fk_comment = models.ForeignKey(Comments,on_delete=models.CASCADE)
    like = models.IntegerField(default=1)

    def __int__(self):
        return self.fk_comment


class Follows(models.Model) :
    user_id =  models.CharField(max_length = 50)
    follow=  models.ForeignKey(Users,on_delete=models.CASCADE)
    follow_check = models.IntegerField(default=1)

    def __int__(self):
        return self.follow_id

