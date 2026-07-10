# Social-media-web-app

<p align="center">
  <a href="https://codealpha-projectsocial-media.onrender.com">
    <img src="https://img.shields.io/badge/Live%20Demo-Click%20Here-success?style=for-the-badge&logo=render" alt="Live Demo" />
  </a>
</p>


<p align="center"> <img src="https://user-images.githubusercontent.com/84091455/208230388-5ca38084-1973-49fd-883a-bbdb4f51d3a6.png" height=200 /> </p>
<br>

<p align="center">
<a href="https://codeclimate.com/github/sankri15/Social-media-web-app/maintainability">
<img src="https://api.codeclimate.com/v1/badges/b79b9943a5cb4340c05f/maintainability" /></a>
<a href="https://codeclimate.com/github/sankri15/Social-media-web-app/test_coverage">
<img src="https://api.codeclimate.com/v1/badges/b79b9943a5cb4340c05f/test_coverage" /></a>
</p>

<p align="center">
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>
</p>

### Pages

- Login Page
- Signup Page
- Create Profile Page
- Edit Profile Page
- Create Post Page
- Delete Post Page
- Update post page
- Password Reset Page
- Feed/Home page
- User Profile Page
- Search Results Page
- Post Comment Page

### Features

- Follow/Unfollow Users
- Like/Unlike the posts
- Download the post images
- Comment on user posts
- User suggestion section
- Search users through the search bar

### Tools and Techs

Backend Framework: `Django`
<br/><br/>
Front-end : `Bootstrap, SCSS, HTML,CSS, Javascript`
<br/><br/>
Database: `Sqlite3`
<br/><br/>

### Installation

1. - Fork the [repo](https://github.com/sankri15/Social-media-web-app)
   - Clone the repo to your local system
   ```git
   git clone https://github.com/sankri15/Social-media-web-app.git
   cd Social-media-web-app
   ```
   Make sure you have python installed on your system.
2. Create a Virtual Environment for the Project

   If u don't have a virtualenv installed

   ```bash
   pip install virtualenv
   ```
   **For Windows Users**
   ```bash
   virtualenv env
   env/Scripts/activate
   ```


   **For Linux Users**
   ```bash
   virtualenv env
   source env/Scripts/activate
   ```

   If you are giving a different name than `env`, mention it in `.gitignore` first

3. Install all the requirements

   ```bash
   pip install -r requirements.txt
   ```

    ```bash
   cd socials
   ```


4. Make migrations/ Create db.sqlite3

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a super user.
   This is to access Admin panel and admin specific pages.

   ```djangotemplate
   python manage.py createsuperuser
   ```
   

   Enter your username, email and password.

6. Run server
   ```bash
   python manage.py runserver
   
  
 ### Snapshots

**1. Signup Page**

![Signup page](https://user-images.githubusercontent.com/84091455/208101528-a448872c-6e8c-4f9e-b287-1c64a58d0c6f.png)

**2. Login Page**

![Login page](https://user-images.githubusercontent.com/84091455/208101465-29c16377-81a7-47c5-a051-c5ca103994a2.png)


**3. Other's Profile**

![127 0 0 1_8000_4_profile_(Nest Hub)](https://user-images.githubusercontent.com/84091455/208229214-687fcdea-72a0-4f86-afc4-1253629006e8.png)


**4. Search Result Users Page**

![Search Result](https://user-images.githubusercontent.com/84091455/208101657-497a2549-c882-4a50-93eb-fcd261201a13.png)

**5. Create a user profile page**

![Create user profile](https://user-images.githubusercontent.com/84091455/208101772-e022f7ee-5c8f-4799-b0be-b5d43effd1d9.png)
