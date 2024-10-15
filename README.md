# Facial Recognition Django Web Application

This Django-based web application provides a facial recognition system with database matching capabilities. It allows users to upload images for face recognition, add known individuals to the database, and match recognized faces against the stored data.

## Features

- Upload and recognize faces in images
- Add known individuals to the database with personal information
- Match recognized faces against the database
- Display matched individual's information
- Simple and intuitive web interface

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/facial-recognition-django.git
   cd facial-recognition-django
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

## Usage

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Open a web browser and navigate to `http://localhost:8000`

3. Use the web interface to:
   - Add known individuals to the database
   - Upload images for face recognition
   - View recognition results and matched individual information

4. Access the admin interface at `http://localhost:8000/admin` to manage the database entries

## Project Structure

- `recognition_app/`: Main Django app directory
  - `models.py`: Defines database models for KnownIndividual and RecognitionResult
  - `views.py`: Contains views for index, add_individual, and recognize_face
  - `urls.py`: Defines URL patterns for the app
  - `templates/`: Contains HTML templates for the web interface
  - `static/`: Contains static files (CSS, JavaScript, etc.)

## Contributing

Contributions to this project are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django framework
- face_recognition library
- OpenCV

## Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.