from typing import Optional
from abc import abstractmethod


class Page:
    def __init__(self, title: str):
        self.title = title
        self.header = self.build_header(title)
        self.footer = self.build_footer()

    @staticmethod
    def build_header(title: str) -> str:
        with open("header.template", "r") as file:
            header_html = file.read().rstrip()
        if title is not None:
            header_html = header_html.replace('<title></title>', f'<title>{title}</title>')
        return header_html

    @staticmethod
    def build_footer() -> str:
        with open("footer.template", "r") as file:
            footer_html = file.read().rstrip()
        return footer_html

    @property
    @abstractmethod
    def body(self) -> Optional[str]:
        return None

    def write(self, output_file: str):
        with open(output_file, "w") as html:
            html.write(self.header)
            html.write(self.body)
            html.write(self.footer)


class CommonPage(Page):
    def __init__(self, title: str, body_template: str):
        super().__init__(title)
        self.body_template = body_template

    @property
    def body(self) -> Optional[str]:
        with open(self.body_template, "r") as file:
            return file.read()
