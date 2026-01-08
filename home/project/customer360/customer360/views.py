from django.shortcuts import render, redirect, get_object_or_404
from datetime import date, timedelta
from django.db.models import Count
from .models import Customer, Interaction, Course, Lesson, Question, Choice, Submission
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
def index(request):
    customers = Customer.objects.all()
    context = {"customers": customers}
    return render(request, "index.html", context=context)

def create_customer(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        customer = Customer.objects.create(name=name, email=email, phone=phone, address=address)
        customer.save()
        msg = "Successfully Saved a Customer"
        return render(request, "add.html", context={"msg": msg})
    return render(request, "add.html")


def summary(request):
    thirty_days_ago = date.today() - timedelta(days=30)
    interactions = Interaction.objects.filter(interaction_date__gte=thirty_days_ago)

    count = len(interactions)
    interactions = interactions.values("channel", "direction").annotate(count=Count('channel'))
    context = {
        "interactions": interactions,
        "count": count
    }

    return render(request, "summary.html", context=context)

def interact(request, cid):
    channels = Interaction.CHANNEL_CHOICES
    directions = Interaction.DIRECTION_CHOICES
    context = {"channels": channels, "directions": directions, "cid": cid}

    if request.method == "POST":
        customer = Customer.objects.get(id=cid)
        channel = request.POST["channel"]
        direction = request.POST["direction"]
        summary = request.POST["summary"]
        interaction = Interaction.objects.create(
            customer=customer,
            channel=channel,
            direction=direction,
            summary=summary)
        interaction.save()
        context["msg"] = "Interaction Success"
        return render(request, "interact.html", context=context)

    return render(request, "interact.html", context=context)


# Online Course Views
def course_list(request):
    courses = Course.objects.all()
    context = {"courses": courses}
    return render(request, "course_list.html", context=context)


def course_details_bootstrap(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    lessons = course.lessons.all()
    questions = course.questions.all()
    context = {
        "course": course,
        "lessons": lessons,
        "questions": questions
    }
    return render(request, "course_details_bootstrap.html", context=context)


@login_required
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    
    if request.method == "POST":
        # Get selected choices from the form
        selected_choices = []
        for key in request.POST:
            if key.startswith('choice_'):
                choice_id = request.POST[key]
                if choice_id:
                    selected_choices.append(int(choice_id))
        
        # Create submission
        submission = Submission.objects.create(
            user=request.user,
            course=course
        )
        
        # Add selected choices to submission
        for choice_id in selected_choices:
            choice = Choice.objects.get(pk=choice_id)
            submission.choices.add(choice)
        
        submission.save()
        
        # Redirect to exam results
        return redirect('show_exam_result', submission_id=submission.id)
    
    return redirect('course_details', course_id=course_id)


def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    course = submission.course
    
    # Get all questions for this course
    questions = course.questions.all()
    total_questions = questions.count()
    
    # Calculate score
    correct_count = 0
    results = []
    
    for question in questions:
        user_choices = submission.choices.filter(question=question)
        correct_choices = question.choices.filter(is_correct=True)
        
        # Check if user selected correct choices
        is_correct = False
        if user_choices.exists():
            # For simplicity, check if any user choice is correct
            is_correct = user_choices.filter(is_correct=True).exists()
            if is_correct:
                correct_count += 1
        
        results.append({
            'question': question,
            'user_choices': user_choices,
            'correct_choices': correct_choices,
            'is_correct': is_correct
        })
    
    # Calculate percentage
    score = int((correct_count / total_questions) * 100) if total_questions > 0 else 100
    
    context = {
        'submission': submission,
        'course': course,
        'results': results,
        'score': score,
        'correct_count': correct_count,
        'total_questions': total_questions
    }
    
    return render(request, "exam_result.html", context=context)
