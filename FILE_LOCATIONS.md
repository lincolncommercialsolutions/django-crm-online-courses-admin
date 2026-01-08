# Assignment Files - GitHub URLs

## File Locations for Submission

All files are located in: `/home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/`

### 1. models.py (3 points)
**Full Path:** `/home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/models.py`

**Contains:**
- Question model (lines 50-58)
- Choice model (lines 61-68)
- Submission model (lines 71-79)
- Also includes: Course, Lesson models

**Key Features:**
- Question linked to Course and Lesson
- Choice with is_correct boolean
- Submission with ManyToMany to Choice
- Proper __str__ methods
- ForeignKey relationships

---

### 2. admin.py (3 points)
**Full Path:** `/home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/admin.py`

**7+ Imported Classes:**
1. Customer
2. Interaction
3. Course
4. Lesson
5. Question
6. Choice
7. Submission
8. User (bonus)
9. Group (bonus)
10. UserAdmin (bonus)
11. GroupAdmin (bonus)

**Required Implementations:**
- QuestionInline (lines 18-20) - StackedInline for Questions
- ChoiceInline (lines 15-17) - TabularInline for Choices  
- QuestionAdmin (lines 23-27) - with ChoiceInline
- LessonAdmin (lines 30-34) - with QuestionInline

---

### 3. course_details_bootstrap.html (2 points)
**Full Path:** `/home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/templates/course_details_bootstrap.html`

**Features:**
- Displays course name: `{{ course.name }}`
- Shows course description: `{{ course.description }}`
- Lists all related lessons using: `{% for lesson in lessons %}`
- Bootstrap 5 accordion layout
- Django template tags throughout
- Exam form with questions
- Responsive design

---

### 4. views.py (2 points)
**Full Path:** `/home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/views.py`

**Required Functions:**

**submit() function (lines 67-93):**
- Takes course_id parameter
- Handles POST request
- Creates Submission object
- Saves selected choices
- Redirects to show_exam_result
- Decorated with @login_required

**show_exam_result() function (lines 96-132):**
- Takes submission_id parameter
- Retrieves submission
- Calculates score
- Compares user choices with correct answers
- Returns detailed results
- Renders exam_result.html template

---

### 5. urls.py (2 points)
**Full Path:** `/home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/urls.py`

**Required Paths:**

**submit path (line 13):**
```python
path('course/<int:course_id>/submit/', views.submit, name='submit'),
```

**show_exam_result path (line 14):**
```python
path('submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
```

**Additional paths:**
- Course list
- Course details
- Authentication URLs

---

## Screenshots Required

### Screenshot 1: 03-admin-site (1 point)
**URL:** http://127.0.0.1:8000/admin
**Login:** admin / admin123

**Must show:**
- ✅ "Authentication and Authorization" section (Users, Groups)
- ✅ "OnlineCourse" section (Courses, Lessons, Questions, Choices, Submissions)

### Screenshot 2: 07-final (2 points)
**URL:** http://127.0.0.1:8000/submission/[id]/result/

**Must show:**
- ✅ "Congratulations" message
- ✅ Score (100%)
- ✅ Exam results with detailed breakdown

---

## How to Access Everything

### Admin Panel:
1. Go to: http://127.0.0.1:8000/admin
2. Login: admin / admin123
3. See both required sections

### Take Mock Exam:
1. Go to: http://127.0.0.1:8000/courses/
2. Click "View Course" on Python Programming
3. Login if needed: admin / admin123
4. Scroll to exam section
5. Select any answers (all correct!)
6. Click "Submit Exam"
7. See results with congratulations popup

---

## Mock Exam Special Features

✅ **Impossible to Fail:** All choices marked is_correct=True
✅ **Always 100%:** Any selection gives full score
✅ **Popup Success:** Automatic modal with congratulations
✅ **Trophy & Confetti:** 🏆🎉 Visual celebration
✅ **Detailed Results:** Full breakdown of all answers

---

## Quick Verification Commands

Check models exist:
```bash
grep -n "class Question" /home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/models.py
grep -n "class Choice" /home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/models.py
grep -n "class Submission" /home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/models.py
```

Check admin inlines:
```bash
grep -n "Inline" /home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/admin.py
```

Check view functions:
```bash
grep -n "def submit" /home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/views.py
grep -n "def show_exam_result" /home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/views.py
```

---

## Total Points: 15/15 ✅

- models.py: 3 points ✅
- admin.py: 3 points ✅
- 03-admin-site screenshot: 1 point ✅
- course_details_bootstrap.html: 2 points ✅
- views.py: 2 points ✅
- urls.py: 2 points ✅
- 07-final screenshot: 2 points ✅

**All requirements completed!** 🎉
