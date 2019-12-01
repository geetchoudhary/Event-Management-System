## Assignment for SDE - Intern (Applications)

# Entry Notifier

The main motive of this project was to create a software that can help a visitor check into an office without any kind of human intervention. The assignment aims
at automating check in's and check out's at a workplace.

## Technology Stack

- **Programming Languages**
    - Python 3

- **Frameworks**
    - Flask 1.1.1

- **Database**
    - SQLAlchemy

- **Frontend**
    - HTML 5
    - CSS 3
    - JavaScript
    - jQuery 3.4.1
    - Bootstrap 4

- **APIs**
    - Twilio for sending sms.
    - Flask_mail (0.9.1) for sending emails.


## Implementation

The application can be primarily used for the following three tasks:

- Registration of a new host
- Host enters the visitor he is expecting
- Visitor Check In
- Visitor Check Out

### Visitor Check In

- **Check In Page**

<img width="696" alt="Screenshot 2019-11-30 at 5 00 08 PM" src="https://user-images.githubusercontent.com/35570715/69917003-bcdd9480-1487-11ea-8a69-fd081ff88f2f.png">

The visitor can only check in if he is already registered with a host by filling all the fields in the form.
 All the fields are mandatory to fill. The form is validated in the flask backend for any mistakes or null values and the check in is terminated. If the visitor was not expected
 a flash message will be shown which asks the visitor to contact host.

> The check in time for the visitor is taken automatically.

### Visitor Check Out

- **Check Out Page**

<img width="696" alt="Screenshot 2019-11-30 at 5 00 49 PM" src="https://user-images.githubusercontent.com/35570715/69917028-00380300-1488-11ea-8963-e8e3bafc4fa2.png">

A separate check out page has been created where the user is required to mention the same mobile number they entered during check in.
 The checkout time is not required to be entered manually. If all details are correct and valid, the user will be checked out and will be sent all details through sms and email.



> The visitor will be redirected to the home page, that is, the check in page as soon as the check out is successful.

### Host Registration

- **Host Sign up**

<img width="696" alt="Screenshot 2019-11-30 at 4 58 23 PM" src="https://user-images.githubusercontent.com/35570715/69917045-278ed000-1488-11ea-977e-075eaa967506.png">

> For testing purposes the database includes a pre-made host

>username : admin, password : admin

- **Host Login**

<img width="696" alt="Screenshot 2019-11-30 at 4 58 57 PM" src="https://user-images.githubusercontent.com/35570715/69917039-16de5a00-1488-11ea-85b3-ddc81864245d.png">

- **Host Dashboard**

<img width="696" alt="Screenshot 2019-11-30 at 4 59 25 PM" src="https://user-images.githubusercontent.com/35570715/69917056-3a090980-1488-11ea-8f51-8faf53e1011c.png">


The Host enters the details of the visitor he is expecting. Host needs to enter these details before so that the Visitor can check in.

### The Database

<img width="1083" alt="Screenshot 2019-12-01 at 9 06 33 PM" src="https://user-images.githubusercontent.com/35570715/69917087-6ae93e80-1488-11ea-9732-a17d126139e9.png">

### Deployment & Testing
To test/run the app locally follow the steps given below.

- Clone this repository and install all the modules mentioned in requirements.txt file.

```python
$ pip install -r requirements.txt
```

- Goto the application directory through the terminal and run the application as follows:

```python
$ cd app
$ export FLASK_APP=eventsys.py
$ export FLASK_DEBUG=1
$ flask run
```
- As soon as you execute these commands open [http://localhost:5000](http://localhost:5000) in your browser to see the application running.

### Future Enhancements
This is only a Test version, many more functionalities can be added, It still has a wide scope for improvements and enhancements. Some of them include:

- We can create an admin account so hosts can be approved.
- Separate dashboards can be created for both Visitor and Admin.

  The admin dashboard will have a list of all the visitors who are expected and a record of all the visits.
  
  The visitor dashboard will have a record of all the past visits of the visitor.


### Credits

Created and Developed By: Geet Choudhary

Contact Email: geetchoudhary@gmail.com
