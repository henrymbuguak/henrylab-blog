from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import Context, RequestContext
from henrylab.models import Blog, Profile
from henrylab.forms import ProfileForm, ContactForm
from django.core.mail import send_mail

def index(request):
    return render_to_response('henrylab/home.html')

def post_list(request):
    posts = Blog.objects.order_by('-created')[:10]
    variables = RequestContext(request, {
        'posts':posts
    })
    return render_to_response('henrylab/post_list.html', variables)

def post_detail(request,pk):
    post = get_object_or_404(Blog, pk=pk)
    variable = RequestContext(request, {
        'post':post
    })
    return render_to_response('henrylab/post_detail.html',variable)

def about(request):
    return render_to_response('henrylab/about.html')

def contact_page(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(email)
                send_mail(subject, message, email, recipients)
                
            return HttpResponseRedirect('/contact/success/')
    else:
        form = ContactForm()
    variables = RequestContext(request, {
        'form':form
    })
    return render(request,'henrylab/contact_page.html', {'form':form})