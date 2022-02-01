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


def build_bio(title: str):
    with open("bio/index.html", "w") as bio_html:
        bio_html.write(build_header(title))
        with open("bio/bio.template", "r") as template:
            bio_html.write(template.read())
        bio_html.write(build_footer())


def build_artwork(title: str):
    with open("artwork/index.html", "w") as artwork_html:
        artwork_html.write(build_header(title))
        with open("artwork/artwork.template", "r") as template:
            artwork_html.write(template.read())
        artwork_html.write(build_footer())


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
    website_name = "Alicia Beta Art"
    build_index_html(f"{website_name}")
    build_bio(f"{website_name} - Bio")
    build_artwork(f"{website_name} - Artwork")


if __name__ == "__main__":
    build()
