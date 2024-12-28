# Face-recognization
We  created this project using a Conventional Neural network (CNN) by OpenCV (Computer Vision)

#Make Sure Python, MYSQL, and its lib are installed on your machine 

Create a Folder[Name] and make sure all these python and haar_cascade files  are in it
Create a new folder called datasets in the same Folder[Name]


# SQL QUERY 

create database students;
use  students;
create table student(Rollno INT NOT NULL,Name VARCHAR(50) NOT NULL,
                     Attendance INT NOT NULL, Date DATETIME NOT NULL,
					 PRIMARY KEY (Rollno));
Insert into student(ROllno, Name, Attendance, date) 
				    values (528, 'Goutham',1,current_timestamp);
Insert into student(ROllno, Name, Attendance, date) 
				    values (526,' sai',0,current_timestamp);
Insert into student(ROllno, Name, Attendance, date) 
				    values (420, 'Aj',0,current_timestamp);
update student set Attendance=0 where Rollno= 528;
update student set Attendance=0;
set sql_safe_updates = 0;
select *from  student;


Press "ENTER" after you run "face_recognize" to end the program 



