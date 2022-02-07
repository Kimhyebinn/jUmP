from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator

def index(request):
    """
    docu 목록 출력
    """
    # 입력
    page = request.GET.get('page', '1')

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 7)
    page_obj = paginator.get_page(page)

    context = {'question_list':page_obj}
    return render(request, 'docu/question_list.html', context)

def detail(request, question_id):
    """
    docu 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'docu/question_detail.html', context)

def answer_create(request, question_id):
    """
    docu 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('docu:detail', question_id=question_id)

    else:
        form = AnswerForm()
    context = {'question': question, 'form':form}
    return render(request, 'docu/question_detail.html', context)



def question_create(request):
    """
    docu 질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('docu:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'docu/question_form.html', context)

