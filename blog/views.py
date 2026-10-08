from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,BlogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def blogHome(request):
    allPosts =Post.objects.all()
    context = {"allPosts":allPosts}
    return render(request, "blog/blogHome.html",context)
    # return HttpResponse("this is home, we will keep aal the bhol psot here")


def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    post.views = post.views + 1
    post.save()
    
    comments = BlogComment.objects.filter(post=post,parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    print(replyDict)
    context = {"post":post,"comments":comments,"user":request.user,"replyDict":replyDict}
    
    return render(request, "blog/blogPost.html",context)

    # return HttpResponse(f"this is post:{slug}")


def postComment(request):
    if request.method == "POST":
        # sno = models.AutoField(primary_key=True)
        comment = request.POST.get("comments")
        user = request.user
        postSno = request.POST.get("postSno")
        post = Post.objects.get(sno=postSno)
        parentSno =  request.POST.get("parentSno")
        
        if parentSno =="":
            comment = BlogComment(comment=comment,user=user,post=post)
            comment.save()     
            messages.success(request,"your comments has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()     
            messages.success(request,"your Reply has been posted successfully")    
    return redirect(f"/blog/{post.slug}")
