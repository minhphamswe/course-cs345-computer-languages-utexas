%% Student: Minh Pham
%% UTEID: mlp2279
%% CSID: minhpham
%% Section: TTh 5:30-6:00pm
%% TA: benself

%% For the Prolog database in PrologDB.pl, re-write the following
%% SQL queries in Prolog and put them in HW6.pl.

%% 1. select s.student_id, last_name, section_id
%%    from student s, enrollment e
%%    where s.student_id = e.student_id and
%%          first_name = 'Fred'

student(StudentID, _, 'Fred', LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _).

%% 2. select s.student_id, last_name, e.section_id, course_no,
%%           instructor_id
%%    from student s, enrollment e, section c
%%    where s.student_id = e.student_id and
%%          e.section_id = c.section_id and
%%          first_name = 'Fred'

student(StudentID, _, 'Fred', LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _).

%% 3. select s.student_id, last_name, e.section_id, r.course_no,
%%           instructor_id, description
%%    from student s, enrollment e, section c, course r
%%    where s.student_id = e.student_id and
%%          e.section_id = c.section_id and
%%          c.course_no = r.course_no and
%%          first_name = 'Fred'

student(StudentID, _, 'Fred', LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
course(CourseNo, Description, _, _).

%% 4. select s.student_id, s.last_name, e.section_id, r.course_no,
%%           i.instructor_id, description, i.first_name, i.last_name
%%    from student s, enrollment e, section c, course r, instructor i
%%    where s.student_id = e.student_id and
%%          e.section_id = c.section_id and
%%          c.course_no = r.course_no and
%%          c.instructor_id = i.instructor_id and
%%          s.first_name = 'Fred'

student(StudentID, _, 'Fred', LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
course(CourseNo, Description, _, _),
instructor(InstructorID, _, IFirstName, ILastName, _, _, _).

%% 5. select i.instructor_id, c.course_no, description, section_id
%%    from instructor i, section s, course c
%%    where i.instructor_id = s.instructor_id and
%%          s.course_no = c.course_no and
%%          first_name = 'Nina' and last_name = 'Schorin'

instructor(InstructorID, _, 'Nina', 'Schorin', _, _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
course(CourseNo, Description, _, _).

%% 6. select c.course_no, first_name, last_name, i.instructor_id,
%%           s.section_id
%%    from course c, section s, instructor i
%%    where c.course_no = s.course_no and
%%          s.instructor_id = i.instructor_id
%%          and description = 'Hands-On Windows'
course(CourseNo, 'Hands-On Windows', _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
instructor(InstructorID, _, FirstName, LastName, _, _, _).

%% 7. select c.course_no, p.first_name, p.last_name,
%%           i.instructor_id, s.section_id
%%    from course c, section s, instructor i, enrollment e,
%%         student p
%%    where c.course_no = s.course_no and
%%          s.instructor_id = i.instructor_id and
%%          e.student_id = p.student_id and
%%          s.section_id = e.section_id and
%%          description = 'Hands-On Windows' and
%%          i.first_name = 'Anita' and i.last_name = 'Morris'
course(CourseNo, 'Hands-On Windows', _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
instructor(InstructorID, _, 'Anita', 'Morris', _, _, _),
student(StudentID, _, FirstName, LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _).

%% 8. select c.description, c.prerequisite
%%    from course c, course p
%%    where c.prerequisite = p.course_no
course(_, Description, _, Prerequisite),
course(Prerequisite, _, _, _).

%% 9. select cost, description
%%    from course
%%    where cost < 1100

course(_, Description, Cost, _), Cost < 1100.

%% 10. Look at the ancestor rules in the file 11Prolog Examples.p
%% and write a set of rules for prereq that will find all of the
%% prerequisite courses for a course such as prereq(A, 430) would
%% give:
%% A = 350 ? ;
%% A = 0 ? ;
%% A = 204 ? ;
%% A = 80 ? ;
%% A = 120 ? ;
%% A = 122 ? ;
%% A = 20 ? ;
%% A = 125 ? ;

im_prereq(0, Y):- course(Y, _, _, 0).
im_prereq(X, Y):- course(Y, _, _, X), Y \= 0.

prereq(X, Y):- im_prereq(X, Y).
prereq(Z, Y):- prereq(X, Y), im_prereq(Z, X).

