from Image_Parsing import image_ocr

"""
Get ingredients from image by passing image path to parse_ingredients()
"""


def parse_ingredients_url(image_url):
    """
    param: image - url to image
    returns result of parse_string function - python object list of ingredients
    """
    text = image_ocr.read_url(image_url)

    return parse_string(text)


def parse_ingredients_path(image_path):

    text = image_ocr.read_path(image_path)

    return parse_string(text)




def parse_string(text):
    """
    param: text from ocr
    returns list of fixed ingredients
    """

    text = text.split("INGREDIENTS: ")
    if len(text) == 1:
        text = text[0]
        text = text.split("Ingredients: ")
    text = text[1]
    text = text.replace('(', ',')
    text = text.replace(')', '')
    text = text.replace('[', ',')
    text = text.replace(']', '')
    text = text.split('      ')
    text = text[0]
    text = text.split(',')

    formatted_text = []
    for i in text:
        word = ""
        w = i.split()
        for z in range(len(w) - 1):
            w[z] = w[z].replace('/n', '')
            word += w[z].lower()
            word += ' '
        w[len(w) - 1] = w[len(w) - 1].replace('/n', '')
        word += w[len(w) - 1]
        formatted_text.append(word)

    formatted_text[len(formatted_text)-1] = formatted_text[len(formatted_text)-1].split('. ')[0]

    return formatted_text


if __name__ == "__main__":
    print(parse_ingredients_path("cheese.jpg"))