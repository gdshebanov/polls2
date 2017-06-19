from django.shortcuts import render, redirect
from .models import Poll, Choice, Vote
from ipware.ip import get_ip

def polls(request):
    if request.session.get('allow') == False:
        return redirect('/')
    args={}
    users_ip = get_users_ip(request)
    polls = Poll.objects.all()
    args['polls'] = polls
    return render(request, 'polls/polls_list.html', args)

def poll_detail(request, poll_id):
    if request.session.get('allow') == False:
        return redirect('/')
    args={}
    poll = Poll.objects.get(pk=poll_id)
    choices = Choice.objects.filter(poll=poll).all()
    ip = get_users_ip(request)
    can_vote = poll.can_vote(ip)
    args['poll'] = poll
    args['choices'] = choices
    args['can_vote'] = can_vote
    return render(request, 'polls/poll_detail.html', args)

def vote(request, poll_id):
    if request.session.get('allow') == False:
        return redirect('/')
    args = {}
    poll = Poll.objects.get(pk=poll_id)
    ip = get_users_ip(request)
    can_vote = poll.can_vote(ip)
    if can_vote:
        choice_id = request.POST.get('choice')
        if choice_id is not None:
            choice = Choice.objects.get(pk=choice_id)
            users_name = request.POST.get('name')
            vote = Vote(ip_address=ip, voter_name=users_name, poll=poll, choice=choice)
            vote.save()
    return poll_detail(request, poll_id)

def get_users_ip(request):
    ip = get_ip(request)
    return ip
