def recite(start_verse, end_verse):

    first_phrase = "On the {} day of Christmas my true love gave to me: "
    lyrics = [
        "a Partridge in a Pear Tree.",
        "two Turtle Doves, ",
        "three French Hens, ",
        "four Calling Birds, ",
        "five Gold Rings, ",
        "six Geese-a-Laying, ",
        "seven Swans-a-Swimming, ",
        "eight Maids-a-Milking, ",
        "nine Ladies Dancing, ",
        "ten Lords-a-Leaping, ",
        "eleven Pipers Piping, ",
        "twelve Drummers Drumming, ",
    ]
    ordinals = [
        "first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"
    ]

    def get_verse(n):
        verse = first_phrase.format(ordinals[n - 1])
        for i in range(n, 1, -1):
            verse += lyrics[i - 1]

        if n > 1:
            verse += "and "

        return verse + lyrics[0]

    song = [get_verse(n) for n in range(start_verse, end_verse + 1)]
    return song
