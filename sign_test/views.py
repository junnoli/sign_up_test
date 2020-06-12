import json
from django.views import View
from django.http  import JsonResponse,HttpResponse
from .models      import Users,Comments,Likes, Follows


#기본적인 정보를 보여주는 뷰 
#post방식이면 입력받은 데이터를  Users에 저장한다. 
#get 방식이면 Users에 저장된 데이터를 보여준다.

class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        Users(
            name     = data['name'],
            email    = data['email'],
            password = data['password']
        ).save()
        # Users.object.create() 이렇게도 사용가능 하다        
        return JsonResponse({'message':'SUCCESS'}, status=200)

    def get(self, request):
        user_data = Users.objects.values()
        return JsonResponse({'users':list(user_data)}, status=200)



#댓글 부분
#댓글 관련된 뷰를 하나 만든다.
#MainView와 동일하게 만들어 보자 유저정보가 아닌 댓글을 담는다고 생각하기 
class CommentView(View) : 
    def post(self, request):
        data = json.loads(request.body)
        Comments(
            UserId  = data['UserId'],
            comment_data = data['comment_data']
        ).save()
            
        return JsonResponse({'message':'SUCCESS'}, status=200)
#예외처리
    def get(self, request):
        user_data = Comments.objects.values()
        return JsonResponse({'Comments':list(user_data)}, status=200)




#로그인 처리 부분

class SignInView(View) :
    #post로 이름과 데이터를 받은 경우 post로 받은 데이터와 users에 저장된 데이터를 비교해서 
    #불러온다
    def post(self, request) : #post로 받은 request 데이터를 인자로 받는다
        data = json.loads(request.body) # data는 request의 데이터(내용)을 json형태로 불러온다

        try :#조건문을 건다. 만약 Users내 데이터 중에 request로 받아온 data['name']=키값이 존재한다면
            if Users.objects.filter(name = data['name']).exists():
                user = Users.objects.get(name = data['name'])#객체를 가져오는것 . Users의 데이터중 name = data['name']인 데이터를 새로운 객체로 만든다
                
                #새로 만든 객체에 담긴 password 데이터와 request로 받은 데이터를 비교해서 동일하면 200신호를 보낸다
                if user.password == data['password']:
                    return JsonResponse({'message':f'{user.email}님 로그인 성공!'}, status=200)
                    
                    #HttpResponse(status=200)
                #예외처리 
                return JsonResponse({'message' : "비밀번호가 틀렸습니다"},status =401) 
            return HttpResponse(status=400)
        
        #예외처리
        except KeyError :
            return JsonResponse({'message' : "INVALID_KEYS"},status =400) 
#빠진 로직 
#패스워드랑 아이디가 같은지 닉네임이나




#좋아요 구현하는 부분

class LikesView(View):
    def post(self, request):
        data = json.loads(request.body)
        comment_num = data["fk_comment"]

        #여기서 해당글에 대한 좋아요 로직이 필요하다.
        #만약 해당 아이디로 좋아요를 이미 눌렀으면 좋아요를 취소 한다.(좋아요 눌린걸 삭제)
        #만약 좋아요를 한 흔적이 없으면 좋아요 기록을 만든다. 
        
        try: 
            if Likes.objects.filter(fk_comment_id = data['fk_comment'] ).exists() and Likes.objects.filter(LikeId = data['LikeId'] ).exists() :
                Likes.objects.filter(fk_comment_id = data['fk_comment']) and Likes.objects.filter(LikeId = data['LikeId']).delete()
                return JsonResponse({'message':'좋아요를 취소합니다'}, status=200)
        
            else :

                Likes(
                LikeId= data['LikeId'],
                fk_comment  = Comments.objects.filter(id=comment_num).get(),
                like = data['like']
                ).save()
            # Users.object.create() 이렇게도 사용가능 하다        
                return JsonResponse({'message':'좋아요를 눌렀습니다'}, status=200)
        except :

             return JsonResponse({'message' : "INVALID_KEYS"},status =400) 

    def get(self, request):
        user_data = Likes.objects.values()
        return JsonResponse({'likes':list(user_data)}, status=200)




class FollowView(View):
    def post(self, request):
        data = json.loads(request.body)
        id_num = data["follow"] # post로 받은 자료중에 follow할 아이디 데이터를 받는다. 이를 id_num이라는 변수에 저장하여 Users 객체를 찾을때 사용한다. 

        #만약 유저 아이디로 팔로우를 이미 했으면 팔로우를 취소 한다.
        #만약 팔로우한 기록이 없으면 팔로우 기록을 만든다. 
        
        try: 
            if Follows.objects.filter(user_id = data['user_id'], follow_id = Users.objects.filter(name=id_num).get()).exists() :
                Follows.objects.filter(follow_id = Users.objects.filter(name=id_num).get(),user_id = data['user_id']).delete()
                return JsonResponse({'message':'팔로우를 취소합니다'}, status=200)
        
            else :

                Follows(
                user_id= data['user_id'],
                follow  = Users.objects.filter(name=id_num).get(),
                follow_check = data['follow_check']
                ).save()
    
                return JsonResponse({'message':'팔로우 했습니다'}, status=200)
        except :

             return JsonResponse({'message' : "INVALID_KEYS"},status =400) 

    def get(self, request):
        user_data = Follows.objects.values()
        return JsonResponse({'follows':list(user_data)}, status=200)