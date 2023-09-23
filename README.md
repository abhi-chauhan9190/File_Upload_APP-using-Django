# File_Upload_APP-using-Django
In this Project I have Developed a Django APP in which different user can upload their files and images on the server.

A user can login or register their account 

Login Page looks like : 
<img width="960" alt="Screenshot 2023-09-23 191651" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/20b90581-f43a-414d-b7b7-d89914720ddf">

Registration Page  looks like :
<img width="960" alt="register1" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/01cc05d5-4bb2-400e-bff9-425c3fd63aaf">

<img width="960" alt="register2" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/02b5116e-16fc-41c2-84a8-ebbc9a710996">

If a user add wrong username or password in login page a message is displayed like shown in image:
<img width="960" alt="Screenshot 2023-09-23 191053" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/1bf600d6-944e-458e-a5c5-a29225cdae5b">

If a new user enters a username which is already present in the database a message is appeared informing the user like shown in figure:
<img width="960" alt="Screenshot 2023-09-23 191144" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/8479f5a7-3a49-4067-97ba-f2bd5ddff3eb">

After successfully login home screen appears 
If the user has not uploaded any file home screen will look like this:

<img width="960" alt="Screenshot 2023-09-23 185511" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/ed04e394-1200-4139-9df9-bea330373f05">

If user has already uploaded some files or images home screen will look like this:

<img width="960" alt="Screenshot 2023-09-23 190449" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/b29624c0-fcde-45e2-b6c2-cfec07474c08">

***User can only upload files after login
***User can only view files uploaded by him

To upload files user can click on the link upload files after which upload files page appear like shown in figure:

<img width="960" alt="Screenshot 2023-09-23 185533" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/7aedb630-33cd-4ac1-b6f5-4a9f07ddbe91">

Firstly user has to enter a title for files then to upload file he/she can click on choose file 
Note : User can add both files and images or can add only one thing also, like either file or image (title is the only required field)
After clicking on choose file a window will appear to upload files like:

<img width="960" alt="Screenshot 2023-09-23 190037" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/1812fc10-c1a7-424c-9a50-f32cbaa62d2a">

User can choose which file to upload from the window

After choosing the file user has to click on Upload button to upload the files 
After this a page will appear :
<img width="960" alt="Screenshot 2023-09-23 190121" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/54ec7ecc-e640-423f-ae3a-abd4ba577716">

Then after which user can go his home page to see newly uploaded file which will appear with the title ,date and time .
User Can see his file by clicking on file button .

<img width="960" alt="filebut" src="https://github.com/abhi-chauhan9190/File_Upload_APP-using-Django/assets/138496233/f38a9d2a-9b75-4eee-9ace-6cfcc724089e">

After uploading user can logout from the APP by clicking on the logout link.

You need to flow basic steps which are used to run any Django app
Like Writing this command on console ->   python manage.py runserver

{if you encounter any error try running following commands one by one:
1. python manage.py makemigrations
2. python manage.py migrate}

   Thank you for reading I hope you like my APP please share any suggestions and reviews .




