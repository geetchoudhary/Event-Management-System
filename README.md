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

![checkinhome](https://drive.google.com/file/d/1E00Y3Dy4Y12WFC3QTArAiNTx0QwS-S8X/view?usp=sharing)

The visitor can only check in if he is already registered with a host by filling all the fields in the form.
 All the fields are mandatory to fill. The form is validated in the flask backend for any mistakes or null values and the check in is terminated. If the visitor was not expected
 a flash message will be shown which asks the visitor to contact host.

> The check in time for the visitor is taken automatically.

### Visitor Check Out

- **Check Out Page**

![check-out home](https://drive.google.com/file/d/1rDCTRXAE775O9aYIoxqXAH6fCiW1lLir/view?usp=sharing)

A separate check out page has been created where the user is required to mention the same mobile number they entered during check in.
 The checkout time is not required to be entered manually. If all details are correct and valid, the user will be checked out and will be sent all details through sms and email.



> The visitor will be redirected to the home page, that is, the check in page as soon as the check out is successful.

### Host Registration

- **Host Sign up**

![host-login](https://drive.google.com/drive/u/0/folders/1JOtZDW1pZdkBfe9Yhaw7AY4vXWtQpdJ1)

> For testing purposes the database includes a pre-made host

>username : admin, password : admin

- **Host Login**

![host-login](https://drive.google.com/file/d/1RxSZW5mxOYqMEe29rCcLbdawH_OvIMO9/view?usp=sharing)

- **Host Dashboard**

![host-dash](https://drive.google.com/file/d/1yn2s0Z59-I-34Qcz8CLFf4BFzCANKALD/view?usp=sharing)

The Host enters the details of the visitor he is expecting. Host needs to enter these details before so that the Visitor can check in.

### The Database

![firebase](https://drive.google.com/file/d/120dtX6norLIIl_Tw-Mlr9x6TBb1nftqQ/view?usp=sharing)

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
$ set FLASK_DEBUG=1
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
