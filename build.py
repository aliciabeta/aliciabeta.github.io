def build_header(title: str):
    with open("header.template", "r") as file:
        header_html = file.read().rstrip()
    if title is not None:
        header_html = header_html.replace('<title></title>', f'<title>{title}</title>')
    return header_html


def build_footer():
    with open("footer.template", "r") as file:
        footer_html = file.read().rstrip()
    return footer_html


def build_about(title: str):
    with open("about/index.html", "w") as about_html:
        about_html.write(build_header(title))
        with open("about/about.template", "r") as template:
            about_html.write(template.read())
        about_html.write(build_footer())


def build_index_html(title: str):
    with open("index.html", "w") as index_html:
        index_html.write(build_header(title))
    
        # Create gallery view
        index_html.write('<div class="container" id="gallery">')
    
        index_html.write('  <div class="row no-gutter">')
        index_html.write('    <div class="col-xs-12 col-sm-6 left">')
        with open("gallery_left.txt", "r") as file:
            for line in file:
                name, img = line.split(',')
                index_html.write('<div class="art">')
                index_html.write(f'  <img class="img-responsive" src={img} alt={name} />')
                index_html.write(f'  <div class="caption">{name}</div>')
                index_html.write('</div>')
        index_html.write('    </div>')
        index_html.write('    <div class="col-xs-12 col-sm-6 right">')
        with open("gallery_right.txt", "r") as file:
            for line in file:
                name, img = line.split(',')
                index_html.write('<div class="art">')
                index_html.write(f'  <img class="img-responsive" src={img} alt={name} />')
                index_html.write(f'  <div class="caption">{name}</div>')
                index_html.write('</div>')
        index_html.write('    </div>')
        index_html.write('  </div>')
        index_html.write('</div>')
    
        index_html.write(build_footer())


def build():
    build_index_html('Alicia Beta')
    build_about('Alicia Beta - About')


if __name__ == "__main__":
    build()
