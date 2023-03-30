import os

def handle_uploaded_file(f, email):
    folder_path = 'media/' + email
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(folder_path + '/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
