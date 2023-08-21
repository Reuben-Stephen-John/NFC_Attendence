This is a Django project that provides a REST API for managing NFC user data, meetings, and attendance.

To get started, clone the repository and install the dependencies:

```
git clone https://github.com/[your-github-username]/backendnfc.git
cd backendnfc
pip install -r requirements.txt
```

Next, create a new database and run the migrations:

```
python manage.py migrate
```

Now you can start the development server:

```
python manage.py runserver
```

The API will be available at http://localhost:8000/api/.

## User model

The `NFCUser` model stores information about NFC users, such as their username, email, NFC serial number, roll number, and faculty registered.

## Meeting model

The `Meeting` model stores information about meetings, such as their name, club, and created date.

## Attendance model

The `Attendance` model stores information about attendance, such as the meeting id, NFC user id, status, and date.

## API endpoints

The API provides the following endpoints:

* `/users/` - Get a list of all NFC users
* `/users/create/` - Create a new NFC user
* `/meetings/` - Get a list of all meetings
* `/meetings/create/` - Create a new meeting
* `/attendances/` - Get a list of all attendance records
* `/attendances/create/` - Create a new attendance record

## Authentication

The API requires authentication for all endpoints except `/users/create/`. You can use the following credentials to create a token:

* username: `admin`
* password: `password`

Once you have a token, you can use it to authenticate your requests by adding the following header to your requests:

```
Authorization: Bearer <token>
```

## Testing

You can run the tests with the following command:

```
python manage.py test
```

## Deployment

To deploy the API to a production server, you can use a WSGI server such as Gunicorn or Apache.

### Instructions:
I am powered by PaLM 2, which stands for Pathways Language Model 2,