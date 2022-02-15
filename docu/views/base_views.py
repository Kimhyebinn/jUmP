from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question
from django.db.models import Q, Count

def index(request):
    """
    docu 목록 출력
    """
    # 입력
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recommend')  # 정렬 기준

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(author__username__icontains=kw)  # 질문 글쓴이 검색
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list':page_obj, 'page': page, 'kw': kw, 'so': so} #page, kw, so 추가
    return render(request, 'docu/question_list.html', context)

def detail(request, question_id):
    """
    docu 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'docu/question_detail.html', context)