Populated logins:
********************
ID 	1
erp	20210003441
pass	Getmein 1
Type	Teacher
--------------------
ID	2
erp	20210000100
pass	Getmein 1
Type	Teacher
--------------------
ID	3
erp	20210000001
pass	Getmein 1
Type	Student
--------------------
ID	4
erp	20210000002
pass	Getmein 1
Type	Student
--------------------
ID	5
erp	20210000003
pass	Getmein 1
Type	Student
--------------------
ID	6
erp	20210000004
pass	Getmein 1
Type	Student
********************

ENDPOINTS

CREATING USER:
METHOD - POST
http://127.0.0.1:8000/auth/users/

GET ALL USERS:
METHOD - GET
http://127.0.0.1:8000/user/user_list/

TOKEN GENERATION:
METHOD - POST
http://127.0.0.1:8000/auth/jwt/create/
body - erp & password

MANAGE ROLES: To switch between teacher/student privilages
METHOD - POST
http://127.0.0.1:8000/user/manage_role/<erp>/<0 for Teacher | 1 for student>

SCHEDULE CLASS:
METHOD - POST
http://127.0.0.1:8000/onlineclass/schedule/
body - start_time, end_time, teacher(id to be passed)

CHECK ALL SCHEDULED CLASSES:
METHOD - GET
http://127.0.0.1:8000/onlineclass/schedule/

JOIN OR LEAVE CLASS:
METHOD - POST
http://127.0.0.1:8000/onlineclass/join/<class id>/<1 for joining| 0 for leaving>

VIEW CLASS JOINING AND LEAVING LOGS:
METHOD - GET
http://127.0.0.1:8000/onlineclass/join/<class id>/

CLASS STATISTICS: User's total active time and attendance status
METHOD - GET
http://127.0.0.1:8000/onlineclass/statistics/<class id>/