from PIL import Image


def max_resize(max_size: int, input_file: str, output_file: str):
    with Image.open(input_file) as input_img:
        width, height = input_img.size

        if width < max_size:
            raise ValueError(f'width ({width}) of image ({input_file}) is less than max ({max_size})')
        if height < max_size:
            raise ValueError(f'height ({height}) of image ({input_file}) is less than max ({max_size})')
        if width > height:
            # width / height = max / x
            # x = max * height / width
            new_width = max_size
            new_height = max_size * height / width
        else:
            # width / height = x / max
            new_height = max_size
            new_width = max_size * width / height

        input_img.resize((int(new_width), int(new_height)))
        input_img.save(output_file)
