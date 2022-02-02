from page import Page
from typing import Optional


class Gallery(Page):
    def __init__(self, title: str):
        super().__init__(title)

    @property
    def body(self) -> Optional[str]:
        # Create gallery view
        html = str()
        html += '<div class="container" id="gallery">'

        html += '  <div class="row no-gutter">'
        html += '    <div class="col-xs-12 col-sm-6 left">'
        with open("gallery_left.txt", "r") as file:
            for line in file:
                name, img = line.split(',')
                html += '<div class="art">'
                html += f'  <img class="img-responsive" src={img} alt={name} />'
                html += f'  <div class="caption">{name}</div>'
                html += '</div>'
        html += '    </div>'
        html += '    <div class="col-xs-12 col-sm-6 right">'
        with open("gallery_right.txt", "r") as file:
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
