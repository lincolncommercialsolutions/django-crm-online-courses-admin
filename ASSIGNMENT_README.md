# Customer 360 & Online Course Platform

A comprehensive platform combining Customer Relationship Management (CRM) with an Online Course and Examination system built with Django and Bootstrap 5.

## 🎯 Assignment Requirements - ALL COMPLETED ✅

### Required Features (All Implemented)

#### 1. Models (models.py) ✅
- **Course** - Online course model
- **Lesson** - Course lessons with order
- **Question** - Exam questions linked to courses/lessons
- **Choice** - Multiple choice answers (all marked as correct for mock exam)
- **Submission** - User exam submissions

#### 2. Admin Panel (admin.py) ✅
- **QuestionInline** - Inline for adding questions within course/lesson admin
- **ChoiceInline** - Inline for adding choices within question admin
- **QuestionAdmin** - Question administration with ChoiceInline
- **LessonAdmin** - Lesson administration with QuestionInline
- **7 Imported Classes:** User, Group, UserAdmin, GroupAdmin, Course, Lesson, Question, Choice, Submission
- **Authentication and Authorization** section (Django default)
- **OnlineCourse** section with all models registered

#### 3. Course Details (course_details_bootstrap.html) ✅
- Bootstrap 5 responsive design
- Course name and description display
- All related lessons shown using Django template tags
- Accordion layout for lessons
- Exam questions with multiple choice interface
- Login-protected exam submission

#### 4. Views (views.py) ✅
- **submit()** - Handles exam submission, creates Submission object
- **show_exam_result()** - Displays exam results with score calculation
- Both functions properly implemented with authentication

#### 5. URLs (urls.py) ✅
- Path for `submit`: `/course/<int:course_id>/submit/`
- Path for `show_exam_result`: `/submission/<int:submission_id>/result/`
- Authentication URLs included

#### 6. Mock Exam - Impossible to Fail ✅
- All questions have ONLY correct answers (all choices marked `is_correct=True`)
- Any choice selected will be correct
- Guaranteed 100% success rate
- Congratulations popup with confetti emoji 🎉
- Score display with detailed results
- Bootstrap modal popup on results page

## 🌟 Features

### Customer Management (CRM)
- ✅ Add, view, and manage customer information
- ✅ Store customer details (name, email, phone, address)
- ✅ View all customers in an organized table
- ✅ Track customer interactions across multiple channels
- ✅ View interaction analytics for the last 30 days

### Online Course System
- ✅ Browse available courses
- ✅ View course details with lessons
- ✅ Take exams with multiple choice questions
- ✅ Login required for exam submission
- ✅ View detailed exam results with score

### Exam Features (Mock Exam - Impossible to Fail)
- ✅ **All answers are correct** - Every choice is marked as correct
- ✅ Guaranteed 100% success
- ✅ Beautiful results page with animations
- ✅ Success modal popup with "Congratulations" message
- ✅ Score display (always 100%)
- ✅ Detailed breakdown of answers
- ✅ Confetti and trophy icons 🎉🏆

### Admin Panel Features
- ✅ Full admin interface at `/admin`
- ✅ **Authentication and Authorization** section (User, Group management)
- ✅ **OnlineCourse** section (Course, Lesson, Question, Choice, Submission)
- ✅ Inline editing for Questions and Choices
- ✅ Customer and Interaction management

## 📁 Project Structure

```
customer360/
├── customer360/              # Django app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── base.html                    # Base template
│   │   ├── index.html                   # Customer list
│   │   ├── add.html                     # Add customer
│   │   ├── interact.html                # Record interaction
│   │   ├── summary.html                 # Analytics
│   │   ├── course_list.html             # Course listing
│   │   ├── course_details_bootstrap.html # Course details & exam
│   │   ├── exam_result.html             # Exam results with popup
│   │   └── registration/
│   │       └── login.html               # Login page
│   ├── models.py           # Data models (Customer, Interaction, Course, Lesson, Question, Choice, Submission)
│   ├── views.py            # Views (includes submit and show_exam_result)
│   ├── admin.py            # Admin config (7 imports, inlines)
│   ├── urls.py             # URL routing (includes submit and show_exam_result paths)
│   └── settings.py         # Django settings
├── static/css/             # Static files
├── create_mock_exam.py     # Script to create sample exam data
└── manage.py               # Django management
```

## 🚀 Running the Application

### Access Points

**Main Application:** http://127.0.0.1:8000/
- Customer Management
- Interaction Tracking
- Analytics Dashboard

**Online Courses:** http://127.0.0.1:8000/courses/
- Browse courses
- View course details
- Take exams (login required)

**Admin Panel:** http://127.0.0.1:8000/admin
- **Username:** admin
- **Password:** admin123
- Manage all data
- View "Authentication and Authorization" section
- View "OnlineCourse" section

### Taking the Mock Exam

1. Navigate to http://127.0.0.1:8000/courses/
2. Click on "Introduction to Python Programming"
3. Review the lessons (optional)
4. Scroll to the exam section
5. Click "Login to Take Exam" (if not logged in)
6. Login with: **admin** / **admin123**
7. Select any answer for each question (ALL ARE CORRECT!)
8. Click "Submit Exam"
9. See the congratulations popup! 🎉
10. View your 100% score and detailed results

## 📊 Mock Exam Details

The mock exam is designed to be **impossible to fail**:

- **Course:** Introduction to Python Programming
- **Lessons:** 3 lessons covering Python basics
- **Questions:** 5 multiple choice questions
- **Special Feature:** ALL choices for ALL questions are marked as correct
- **Result:** Guaranteed 100% score regardless of selections
- **Popup:** Automatic success modal with congratulations message

### Sample Questions (All Choices Correct):
1. What is Python? (4 correct choices)
2. Which is a valid variable name? (4 correct choices)
3. What data type is 'Hello World'? (4 correct choices)
4. Which statement makes decisions? (4 correct choices)
5. Which loop can be used? (4 correct choices)

## 🎨 UI/UX Features

- Modern Bootstrap 5 design
- Gradient backgrounds
- Smooth animations
- Success modal popup
- Responsive layout
- Bootstrap Icons throughout
- Card-based interface
- Hover effects

## 📋 Admin Panel Sections

### Authentication and Authorization ✅
- Users
- Groups

### OnlineCourse ✅
- Courses (with QuestionInline)
- Lessons (with QuestionInline)
- Questions (with ChoiceInline)
- Choices
- Submissions

### Customer360 (CRM)
- Customers
- Interactions

## 🔧 Technology Stack

- **Backend:** Django 6.0.1
- **Frontend:** Bootstrap 5.3, Bootstrap Icons
- **Database:** SQLite3
- **Python:** 3.12.3
- **Authentication:** Django Auth System

## 📝 Assignment Submission Checklist

- ✅ **models.py** - Contains Question, Choice, and Submission models
- ✅ **admin.py** - 7+ imported classes, QuestionInline, ChoiceInline, QuestionAdmin, LessonAdmin
- ✅ **Admin Site** - Both "Authentication and Authorization" and "OnlineCourse" sections visible
- ✅ **course_details_bootstrap.html** - Course details with lessons using Django templates and Bootstrap
- ✅ **views.py** - Contains submit() and show_exam_result() functions
- ✅ **urls.py** - Contains paths for submit and show_exam_result
- ✅ **Mock Exam** - Impossible to fail, shows congratulations message, score, and results

## 🎓 Testing the Mock Exam

To verify the mock exam works correctly:

1. Visit: http://127.0.0.1:8000/courses/
2. Click "View Course" on Python Programming
3. Login as admin/admin123
4. Select ANY answers (they're all correct!)
5. Submit the exam
6. **Expected Result:**
   - Popup appears with "Congratulations! 🎉"
   - Score shows 100%
   - All answers marked as correct
   - Detailed results breakdown displayed

## 📸 Screenshots Needed for Submission

1. **03-admin-site**: Admin panel showing both sections
2. **07-final**: Exam results page with congratulations, score, and results

---

**Project Status:** ✅ All assignment requirements completed!
**Server:** 🟢 Running at http://127.0.0.1:8000/
**Mock Exam:** 🎉 Impossible to fail - 100% guaranteed!
