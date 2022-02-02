import os.path
import shutil
from typing import Optional
from page import Page, CommonPage


def create_gallery(src_path: str, dest_path: str, website_name: str):
    if not os.path.exists(src_path):
        ValueError('src_path %s DNE')
    if not os.path.exists(dest_path):
        ValueError('src_path %s DNE')

    # Delete everything in destination
    for filename in os.listdir(dest_path):
        file_path = os.path.join(dest_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    # Create main index
    galleries = []
    with open(src_path + '/index.txt') as index_file:
        index_html = '<div class="container" id="galleryNav">\n'\
                     '  <div class="row no-gutter">\n'
        for line in index_file:
            name, folder, img = line.split(',')
            img = img.rstrip()
            galleries.append(folder)
            # copy image from source to dest
            file_src_path = src_path + '/' + img
            file_dest_path = dest_path + '/' + img
            shutil.copy(file_src_path, file_dest_path)

            index_html += '    <div class="col-xs-12 col-sm-6 col-md-3">\n'\
                          '      <div class="art">\n'\
                          f'        <img class="img-responsive" src="/{file_dest_path}" alt="{name}" />\n'\
                          f'        <div class="caption">{name}</div>\n'\
                          '      </div>\n'\
                          '    </div>\n'
        index_html += '  </div>\n'\
                      '</div>\n'

        gallery_title = f"{website_name} - Artwork"
        main_index = CommonPage(gallery_title, index_html)
        main_index.write(dest_path + "/index.html")

    # todo: create galleries
    # index = Gallery(f"{website_name}", "gallery_left.txt", "gallery_right.txt")
    # index.write("index.html")


class Gallery(Page):
    def __init__(self, title: str, left: str, right: str):
        super().__init__(title)
        self.left = left
        self.right = right

    @property
    def body(self) -> Optional[str]:
        # Create gallery view
        html = str()
        html += '<div class="container" id="gallery">'

        html += '  <div class="row no-gutter">'
        html += '    <div class="col-xs-12 col-sm-6 left">'
        with open(self.left, "r") as file:
            for line in file:
                name, img = line.split(',')
                html += '<div class="art">'
                html += f'  <img class="img-responsive" src={img} alt={name} />'
                html += f'  <div class="caption">{name}</div>'
                html += '</div>'
        html += '    </div>'
        html += '    <div class="col-xs-12 col-sm-6 right">'
        with open(self.right, "r") as file:
            for line in file:
                name, img = line.split(',')
                html += '<div class="art">'
                html += f'  <img class="img-responsive" src={img} alt={name} />'
                html += f'  <div class="caption">{name}</div>'
                html += '</div>'
        html += '    </div>'
        html += '  </div>'
        html += '</div>'
        return html
