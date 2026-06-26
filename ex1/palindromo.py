def is_palindromo(text): 
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]