from module.upload import upload
from module.delete_file import delete_file
from module.download import file_download
from module.gallery import add_gallery


def configure_route(app):
    
    add_gallery(app)
    upload(app)
    file_download(app)
    delete_file(app)
