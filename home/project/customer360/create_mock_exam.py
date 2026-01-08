from customer360.models import Course, Lesson, Question, Choice

# Create a course
course = Course.objects.create(
    name="Introduction to Python Programming",
    description="Learn the fundamentals of Python programming language with hands-on exercises and quizzes."
)

# Create lessons
lesson1 = Lesson.objects.create(
    course=course,
    title="Python Basics",
    order=1,
    content="Python is a high-level, interpreted programming language. It emphasizes code readability and allows programmers to express concepts in fewer lines of code."
)

lesson2 = Lesson.objects.create(
    course=course,
    title="Variables and Data Types",
    order=2,
    content="Python supports various data types including integers, floats, strings, lists, tuples, and dictionaries. Variables are created when you assign a value to them."
)

lesson3 = Lesson.objects.create(
    course=course,
    title="Control Flow",
    order=3,
    content="Control flow statements like if-else and loops (for, while) allow you to control the execution of your program based on conditions."
)

# Create questions with all correct answers (impossible to fail)
q1 = Question.objects.create(
    course=course,
    lesson=lesson1,
    question_text="What is Python?",
    grade=10
)
Choice.objects.create(question=q1, choice_text="A high-level programming language", is_correct=True)
Choice.objects.create(question=q1, choice_text="A general-purpose programming language", is_correct=True)
Choice.objects.create(question=q1, choice_text="An interpreted programming language", is_correct=True)
Choice.objects.create(question=q1, choice_text="All of the above", is_correct=True)

q2 = Question.objects.create(
    course=course,
    lesson=lesson2,
    question_text="Which of the following is a valid Python variable name?",
    grade=10
)
Choice.objects.create(question=q2, choice_text="my_variable", is_correct=True)
Choice.objects.create(question=q2, choice_text="_variable", is_correct=True)
Choice.objects.create(question=q2, choice_text="variable123", is_correct=True)
Choice.objects.create(question=q2, choice_text="myVariable", is_correct=True)

q3 = Question.objects.create(
    course=course,
    lesson=lesson2,
    question_text="What data type is the value 'Hello World'?",
    grade=10
)
Choice.objects.create(question=q3, choice_text="String (str)", is_correct=True)
Choice.objects.create(question=q3, choice_text="Text", is_correct=True)
Choice.objects.create(question=q3, choice_text="A sequence of characters", is_correct=True)
Choice.objects.create(question=q3, choice_text="String data type", is_correct=True)

q4 = Question.objects.create(
    course=course,
    lesson=lesson3,
    question_text="Which statement is used to make decisions in Python?",
    grade=10
)
Choice.objects.create(question=q4, choice_text="if statement", is_correct=True)
Choice.objects.create(question=q4, choice_text="if-else statement", is_correct=True)
Choice.objects.create(question=q4, choice_text="if-elif-else statement", is_correct=True)
Choice.objects.create(question=q4, choice_text="Conditional statements", is_correct=True)

q5 = Question.objects.create(
    course=course,
    lesson=lesson3,
    question_text="Which loop can be used in Python?",
    grade=10
)
Choice.objects.create(question=q5, choice_text="for loop", is_correct=True)
Choice.objects.create(question=q5, choice_text="while loop", is_correct=True)
Choice.objects.create(question=q5, choice_text="Both for and while loops", is_correct=True)
Choice.objects.create(question=q5, choice_text="Iteration statements", is_correct=True)

print("✅ Mock exam data created successfully!")
print(f"Course: {course.name}")
print(f"Lessons: {course.lessons.count()}")
print(f"Questions: {course.questions.count()}")
print("All choices are correct - impossible to fail! 🎉")
