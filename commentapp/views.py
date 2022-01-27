from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        #article값이 비어있음
        #create.html에서 'article_pk'라는 이름의 input에 담아서 form으로 post메소드를 사용해 보냄
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.article.pk})
    #여기 object는 comment임. 즉 comment의 article의 pk를 가지고 있는 곳으로 돌아간다는 뜻
    #pk는 comment나 article 등 app마다 다름 > 그래서 comment의 article의 pk로 가는 거임

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name='commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail',kwargs={'pk':self.object.article.pk})