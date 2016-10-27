**Entities and actions**

**Prof**
```
Create/Edit Assignment
  Delete Assignment
  Grade
	one student
	all students
  Re-grade
  Create / Manage students
  Download student submissions
  Log_in
```


**Student**
```
Submit / re-submit solution
Log in
See previous submissions
```


**Dev**
```
Create prof
log in
```



**Grading Hierchy**

```
Class D
 	Assign 1
		Student A (11/12)
			Solution A (11/12)
				TestSuite A (5/6)
				TestSuiteB (6/6)
					testcase1 check
					testcase2    X
					testcase3    not graded


```




**Database relations**


Prof : email, pws, ''classes'', name

Student: email pws, ''classes, solutions''

Class: desc, ''assignments, prof, students''

Assignment: Desc, deadline, ''testsuites''

Solution: date submitted, code, ''student, assignment''

Grade:  date graded, grade, output, ''solution, testcase''

Test Suite:  nsfile, ''assignment''

Test Case:  desc ''nsfile''

TestCaseNSFileMap:  node, code, student filename,'' test case.''

ToGrade : Solution, status 
```
     "submittted for grading"
     "grading..."
     "grading suite 2/5"
```
