__all__ = ("find_shortest_longest_word",)


def find_shortest_longest_word(text: str) -> tuple[str, str] | tuple[None, None]:
    """Находит самое короткое и самое длинное слово.

    Returns:
        (<самое короткое слово>, <самое длинное слово>) – если text содержит слова,
        (None, None) – иначе

    Example:
        >> find_shortest_longest_word("а бб ввв")
        ("а", "ввв")
        >> find_shortest_longest_word(" \n\t ")
        (None, None)
    """
    if text == '' or text.strip() == "":
        return (None, None)

    words = text.replace(',', ' ').split()
    smallest = words[0]
    longest = words[0]

    for word in words[1:]:
        if len(word) < len(smallest):
            smallest = word
        if len(word) > len(longest):
            longest = word

    return (smallest, longest) 

print(find_shortest_longest_word("hello\n\n\tsir"))