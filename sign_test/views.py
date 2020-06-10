import json
from django.views import View
from django.http  import JsonResponse,HttpResponse
from .models      import Users,Comments

#기본적인 정보를 보여주는 뷰 
#post방식이면 입력받은 데이터를  Users에 저장한다. 
#get 방식이면 Users에 저장된 데이터를 보여준다.
class MainView(View):
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
            id_data   = data['id_data'],
            comment_data = data['comment_data']
        ).save()
        # Users.object.create() 이렇게도 사용가능 하다        
        return JsonResponse({'message':'SUCCESS'}, status=200)

    def get(self, request):
        user_data = Comments.objects.values()
        return JsonResponse({'Comments':list(user_data)}, status=200)




#로그인 처리 부분

class SignUpView(View) :
    #post로 이름과 데이터를 받은 경우 post로 받은 데이터와 users에 저장된 데이터를 비교해서 
    #불러온다
    def post(self, request) : #post로 받은 request 데이터를 인자로 받는다
        data = json.loads(request.body) # data는 request의 데이터(내용)을 json형태로 불러온다

        try :#조건문을 건다. 만약 Users내 데이터 중에 request로 받아온 data['name']=키값이 존재한다면
            if Users.objects.filter(name = data['name']).exists():
                user = Users.objects.get(name = data['name'])#새로운 객체를 만든다 . Users의 데이터중 name = data['name']인 데이터를 새로운 객체로 만든다
                
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
