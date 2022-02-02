from page import CommonPage
from gallery import create_gallery


def build():
    website_name = "Alicia Beta Art"

    create_gallery("gallery", "artwork", website_name)

    bio = CommonPage(f"{website_name} - Bio", "bio/bio.template")
    bio.write("bio/index.html")
    index = CommonPage(f"{website_name}", "index.template")
    index.write("index.html")


if __name__ == "__main__":
    build()
