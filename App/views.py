from django.http import HttpResponse
from django.shortcuts import render
from dwebsocket.decorators import accept_websocket, require_websocket


# Create your views here.


@accept_websocket
def echo(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        try:  # 如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return HttpResponse("this is a websocket url!")
    else:
        print("userid")
        for message in request.websocket:
            str = message.decode('utf-8')
            print("Client msg: " + str)
            str = "server's msg: " + str
            request.websocket.send(str)  # 发送消息到客户端


@require_websocket
def echo_once(request):
    '''只能发送一次消息就断开连接'''
    message = request.websocket.wait()
    str = message.decode('utf-8')
    print("Client msg: " + str)
    str = "server's msg: " + str
    request.websocket.send(str)