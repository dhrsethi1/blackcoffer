DRIVER_PATH = "~/Documents/chromedriver_mac64"
INPUT_FILENAME = 'Input.xlsx'
OPTIONS_ARGUMENT = "--windows-size=1920,1200"
COUNTERS = {"positive_score": 0,
            "negative_score":0,
            "polarity_score":0,
            "subjectivity_score":0,
            "sentence_count":0,
            "percentage_of_complex_words":0,
            "fog_index":0,
            "average_sentence_length":0,
            "average_words_per_sentence":0, #Same as above
            "complex_word_count":0,
            "word_count":0,
            "personal_pronouns":0,
            "avg_word_length":0,
            "total_characters":0,
            "paragraph_count":0,
            "total_syllables_in_article":0,
            "syllables_per_word":0}

POSITIVE_LIST = []
NEGATIVE_LIST = []

SMALL_NUMBER = 0.000001