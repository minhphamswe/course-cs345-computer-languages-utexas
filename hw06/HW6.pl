%% Student: Minh Pham
%% UTEID: mlp2279
%% CSID: minhpham
%% Section: TTh 5:30-6:00pm
%% TA: benself

%% 1. prolog query 1.

student(StudentID, _, 'Fred', LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _).

%% 2. prolog query 2.

student(StudentID, _, 'Fred', LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _).

%% 3. prolog query 3.

student(StudentID, _, 'Fred', LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
course(CourseNo, Description, _, _).

%% 4. prolog query 4.

student(StudentID, _, 'Fred', LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
course(CourseNo, Description, _, _),
instructor(InstructorID, _, IFirstName, ILastName, _, _, _).

%% 5. prolog query 5.

instructor(InstructorID, _, 'Nina', 'Schorin', _, _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
course(CourseNo, Description, _, _).

%% 6. prolog query 6.

course(CourseNo, 'Hands-On Windows', _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
instructor(InstructorID, _, FirstName, LastName, _, _, _).

%% 7. prolog query 7.

course(CourseNo, 'Hands-On Windows', _, _),
section(SectionID, CourseNo, _, _, _, InstructorID, _),
instructor(InstructorID, _, 'Anita', 'Morris', _, _, _),
student(StudentID, _, FirstName, LastName, _, _, _, _, _),
enrollment(StudentID, SectionID, _, _).

%% 8. prolog query 8.

course(_, Description, _, Prerequisite),
course(Prerequisite, _, _, _).

%% 9. prolog query 9.

course(_, Description, Cost, _), Cost < 1100.

%% 10. prolog rules for prereq
%% prereq(X,430).

im_prereq(0, Y):- course(Y, _, _, 0).
im_prereq(X, Y):- course(Y, _, _, X), Y \= 0.

prereq(X, Y):- im_prereq(X, Y).
prereq(Z, Y):- prereq(X, Y), im_prereq(Z, X).

