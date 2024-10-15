from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import cv2
import face_recognition
from .models import RecognitionResult
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import KnownIndividual, Result
import face_recognition
import cv2
import numpy as np



def add_individual(request):
    if request.method == 'POST':
        id_number = request.POST['id_number']
        name = request.POST['name']
        town = request.POST['town']
        additional_info = request.POST['additional_info']
        face_image = request.FILES['face_image']

        individual = KnownIndividual(
            id_number=id_number,
            name=name,
            town=town,
            additional_info=additional_info,
            face_image=face_image
        )

        # Generate and store face encoding
        image = face_recognition.load_image_file(face_image)
        face_encoding = face_recognition.face_encodings(image)[0]
        individual.face_encoding = face_encoding.tobytes()
        
        individual.save()
        return redirect('index')

    return render(request, 'add_individual.html')

def recognize_faces(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        uploaded_image_path = fs.path(filename)

        # Load the uploaded image
        image = face_recognition.load_image_file(uploaded_image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)

        # Load known face encodings
        known_face_encodings = []
        known_individuals = []
        for individual in KnownIndividual.objects.all():
            known_face_encodings.append(np.frombuffer(individual.face_encoding, dtype=np.float64))
            known_individuals.append(individual)

        matched_individual = None
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            if True in matches:
                match_index = matches.index(True)
                matched_individual = known_individuals[match_index]
                break

        # Create a new RecognitionResult instance
        result = Result(
            uploaded_image=uploaded_image,
            match_found=matched_individual is not None,
            matched_individual=matched_individual
        )

        # Draw rectangles around faces and label if matched
        image_cv = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            cv2.rectangle(image_cv, (left, top), (right, bottom), (0, 255, 0), 2)
            if matched_individual:
                cv2.putText(image_cv, matched_individual.name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Save the processed image
        processed_filename = f"processed_{filename}"
        cv2.imwrite(fs.path(processed_filename), image_cv)
        result.processed_image = processed_filename

        result.save()

        context = {
            'result': result,
            'uploaded_image_url': fs.url(filename),
            'processed_image_url': fs.url(processed_filename),
        }

        return render(request, 'result2.html', context)

    return redirect('index')





def index(request):
    return render(request, 'index2.html')

def recognize_face(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        uploaded_image_url = fs.url(filename)

        # Load the uploaded image
        image = face_recognition.load_image_file(fs.path(filename))

        # Find all face locations in the image
        face_locations = face_recognition.face_locations(image)

        # Create a new RecognitionResult instance
        result = RecognitionResult(original_image=uploaded_image, faces_detected=len(face_locations))

        if face_locations:
            for face_location in face_locations:
                top, right, bottom, left = face_location
                cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

            # Save the image with rectangles
            processed_filename = f"detected_{filename}"
            cv2.imwrite(fs.path(processed_filename), image[:, :, ::-1])
            detected_image_url = fs.url(processed_filename)

            # Update the RecognitionResult with the processed image
            result.processed_image = processed_filename

        # Save the RecognitionResult
        result.save()

        return render(request, 'result.html', {
            'uploaded_image_url': uploaded_image_url,
            'detected_image_url': detected_image_url if face_locations else None,
            'faces_found': len(face_locations)
        })

    return render(request, 'index.html')
