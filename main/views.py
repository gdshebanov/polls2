from django.shortcuts import render, reverse, redirect

def start_page(request):
    if request.session.get('allow') == True:
        return redirect('/polls_v2')
    return render(request, 'main/start_page.html')

def check(request):
    school_number = request.POST.get('school')
    if school_number is not None and school_number == '1285':
        request.session['allow'] = True
        return redirect('/polls_v2')
    else:
        return redirect('/')
