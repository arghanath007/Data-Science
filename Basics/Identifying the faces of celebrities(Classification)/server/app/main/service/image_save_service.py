import os

def image_save(new_request):
    try:
        data=new_request.files
    except RequestEntityTooLarge as e:
        return apiResponse(False, f"File size is too Large", None, str(e)).__dict__, 413

    file=data['image']

    if 'image' not in data:
        message='No image part in the request'

    elif file.filename == '':
        message='No image selected for uploading'

    elif len(file.filename) > image_name_size:
        message='File name is too Large'
    elif file:
        filename=secure_filename(file.filename)

        file_path=UPLOAD_FOLDER + f"/{filename}"
        if os.path.exists(file_path) or os.path.isfile(file_path):
            os.remove(file_path)

        image_path=image_helper.save_image(data['image'], name=filename)

        message=None

    return image_path, message