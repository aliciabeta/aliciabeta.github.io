from page import CommonPage
from gallery import Gallery


def build():
    website_name = "Alicia Beta Art"

    index = Gallery(f"{website_name}")
    index.write("index.html")
    bio = CommonPage(f"{website_name} - Bio", "bio/bio.template")
    bio.write("bio/index.html")
    artwork = CommonPage(f"{website_name} - Artwork", "artwork/artwork.template")
    artwork.write("artwork/index.html")


if __name__ == "__main__":
    build()
