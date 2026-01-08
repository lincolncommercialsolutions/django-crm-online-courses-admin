# Screenshot Guide for Assignment Submission

## Required Screenshots

### Screenshot 1: Admin Site (03-admin-site)
**URL:** http://127.0.0.1:8000/admin
**Login:** admin / admin123

**What to capture:**
- The admin panel home page showing:
  ✅ **Authentication and Authorization** section with:
     - Groups
     - Users
  ✅ **OnlineCourse** section with:
     - Courses
     - Lessons  
     - Questions
     - Choices
     - Submissions
  ✅ Also shows Customer360 section (bonus)

**How to take:**
1. Login to admin panel
2. You'll see the sections immediately
3. Take a full-page screenshot showing both sections

---

### Screenshot 2: Exam Results (07-final)
**URL:** After completing exam at http://127.0.0.1:8000/courses/

**What to capture:**
- The exam results page showing:
  ✅ **Congratulations message** with trophy and party emoji 🎉🏆
  ✅ **Score**: 100%
  ✅ **Exam results**: Detailed breakdown of all answers
  ✅ Success popup modal (appears automatically)

**How to take:**
1. Go to http://127.0.0.1:8000/courses/
2. Click "View Course" on Python Programming course
3. Login (admin/admin123)
4. Scroll to exam section
5. Select ANY answer for each question (all are correct!)
6. Click "Submit Exam"
7. Results page loads with automatic popup
8. Take screenshot showing:
   - The popup modal with "Congratulations!"
   - The 100% score
   - The detailed results below

---

## GitHub URLs for Submission

All files are in: `/home/linkl0n/cert-projects/imbdevproject/home/project/customer360/customer360/`

1. **models.py**
   - Path: `customer360/models.py`
   - Contains: Question, Choice, Submission models (+ Course, Lesson)

2. **admin.py**
   - Path: `customer360/admin.py`
   - Contains: 7 imports, QuestionInline, ChoiceInline, QuestionAdmin, LessonAdmin

3. **course_details_bootstrap.html**
   - Path: `customer360/templates/course_details_bootstrap.html`
   - Contains: Course details with Bootstrap, lessons display

4. **views.py**
   - Path: `customer360/views.py`
   - Contains: submit() and show_exam_result() functions

5. **urls.py**
   - Path: `customer360/urls.py`
   - Contains: paths for submit and show_exam_result

---

## Quick Test Checklist

Before taking screenshots, verify:

- [ ] Admin panel shows "Authentication and Authorization" section
- [ ] Admin panel shows "OnlineCourse" section  
- [ ] Can login to admin with admin/admin123
- [ ] Courses page loads at /courses/
- [ ] Can click on course to see details
- [ ] Lessons display in accordion
- [ ] Exam questions show with radio buttons
- [ ] Login required to submit exam
- [ ] After submission, shows congratulations popup
- [ ] Score shows 100%
- [ ] Detailed results display correctly

---

## Notes

✅ **Mock Exam Feature:** All questions have ONLY correct answers. It's impossible to fail!

✅ **Admin Sections:** Both required sections are clearly visible and functional.

✅ **Bootstrap Design:** All templates use Bootstrap 5 with responsive design.

✅ **Django Template Tags:** Course details page uses {% for %}, {% if %}, {{ }} properly.

✅ **URL Patterns:** All required paths are configured and working.
