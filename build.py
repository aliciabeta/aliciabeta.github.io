def build_header(title: str):
    header_html = open("header.template", "r").read().rstrip()
    if title is not None:
        header_html = header_html.replace('<title></title>', f'<title>{title}</title>')
    return header_html


def build_footer():
    return open("footer.template", "r").read().rstrip()


def build_about(title: str):
    about_html = open("about/index.html", "w")
    about_html.write(build_header(title))

    about_html.write(open("about/about.template", "r").read())

    about_html.write(build_footer())
    about_html.close()


def build_index_html(title: str):
    index_html = open("index.html", "w")

    index_html.write(build_header(title))

    # Create gallery view
    index_html.write('<div class="container" id="gallery">')

    index_html.write('  <div class="row no-gutter">')
    index_html.write('    <div class="col-xs-12 col-sm-6 left">')
    file = open("gallery_left.txt", "r")
    for line in file:
        name, img = line.split(',')
        index_html.write('<div class="art">')
        index_html.write(f'  <img class="img-responsive" src={img} alt={name} />')
        index_html.write(f'  <div class="caption">{name}</div>')
        index_html.write('</div>')
    file.close()
    index_html.write('    </div>')
    index_html.write('    <div class="col-xs-12 col-sm-6 right">')
    file = open("gallery_right.txt", "r")
    for line in file:
        name, img = line.split(',')
        index_html.write('<div class="art">')
        index_html.write(f'  <img class="img-responsive" src={img} alt={name} />')
        index_html.write(f'  <div class="caption">{name}</div>')
        index_html.write('</div>')
    file.close()
    index_html.write('    </div>')
    index_html.write('  </div>')
    index_html.write('</div>')

    index_html.write(build_footer())
    index_html.close()


def build():
    build_index_html('Alicia Beta')
    build_about('Alicia Beta - About')


if __name__ == "__main__":
    build()
