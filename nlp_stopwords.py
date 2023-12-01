#The currency file was converted to UTF-8 format from ANSI
STOPWORDS_FILES=["StopWords_Auditor.txt", "StopWords_Currencies.txt", "StopWords_DatesandNumbers.txt",
                 "StopWords_Generic.txt", "StopWords_GenericLong.txt", "StopWords_Geographic.txt",
                 "StopWords_Names.txt"]


def removeAll(list, item):
    # remove the item for all its occurrences
    c = list.count(item)
    for i in range(c):
        list.remove(item)
    return list

def ReplaceStopwordInParagraph(stopword, local_paragraph):
    if isinstance(local_paragraph, str):
        paragraph_words = local_paragraph.split()
    else:
        paragraph_words = local_paragraph.text.split()
    paragraph_words_lower = [x.lower() for x in paragraph_words]
    #clean_paragraph = paragraph_words
    if stopword in paragraph_words_lower:
       # paragraph_words.lower()
        removeAll(paragraph_words_lower, stopword)
    rejoined_paragraph = " ".join(paragraph_words_lower)

    return rejoined_paragraph


def remove_stopwords(filename, paragraph):
    lines_of_stopword_file = []
    local_paragraph = paragraph
    f = open('StopWords/'+filename, 'r')
    lines_of_stopword_file = f.readlines()

    for stopword in lines_of_stopword_file:
        stopword = stopword.strip('\n').lower()
        clean_paragraph = ReplaceStopwordInParagraph(stopword, local_paragraph) #local paragraph need's to change
        local_paragraph = clean_paragraph

    return local_paragraph

def process_stopword_files(article):
    print("3. In process_stopword_files")
    clean_article =  []
    counter = 0
    for paragraph in article:
        counter += 1
        for stopword_file in STOPWORDS_FILES:
            output_paragraph = remove_stopwords(stopword_file, paragraph) 
            clean_article.append(output_paragraph)
    return clean_article

