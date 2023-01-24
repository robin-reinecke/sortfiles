import os

current_folder = os.getcwd()
sorted_folder = os.path.join(current_folder, "sorted")
os.makedirs(sorted_folder, exist_ok=True)

document_folder = os.path.join(sorted_folder, "Documents")
os.makedirs(document_folder, exist_ok=True)

video_folder = os.path.join(sorted_folder, "Videos")
os.makedirs(video_folder, exist_ok=True)

image_folder = os.path.join(sorted_folder, "Images")
os.makedirs(image_folder, exist_ok=True)

pdf_folder = os.path.join(sorted_folder, "PDFs")
os.makedirs(pdf_folder, exist_ok=True)

other_folder = os.path.join(sorted_folder, "Others")
os.makedirs(other_folder, exist_ok=True)

for filename in os.listdir(current_folder):
    file_path = os.path.join(current_folder, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1]
        if file_extension in ('.doc', '.docx', '.pages'):
            os.rename(file_path, os.path.join(document_folder, filename))
        elif file_extension in ('.mp4', '.mkv', '.avi', '.mov'):
            os.rename(file_path, os.path.join(video_folder, filename))
        elif file_extension in ('.jpg', '.jpeg', '.png', '.gif'):
            os.rename(file_path, os.path.join(image_folder, filename))
        elif file_extension in ('.pdf'):
            os.rename(file_path, os.path.join(pdf_folder, filename))
        else:
            os.rename(file_path, os.path.join(other_folder, filename))
