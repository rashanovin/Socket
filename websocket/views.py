from django.shortcuts import render


def test(request):

    return render(request, template_name='websocket.html')
