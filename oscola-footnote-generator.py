def main():
    welcome()
    instructions()
    footnote()
    
def welcome():  
    print("Welcome to OSCOLA generator (Secondary Sources - Footnotes).")
    
def instructions():
    print("1. Type in all caps.")
    """
    print("2. All elements that need to be italicized will generate like this. <i> italicized word here </i>. This is because I'm still looking for a way to italicize words in the Python terminal (not sure if this is possible), or otherwise turning this into a graphic-based program instead of a text-based one. I'll keep you up once I'm done!")
    """

def footnote():
    source = input("What are you citing? Possible answers are BOOK, CHAPTER, ENCYCLOPEDIA, JOURNAL ARTICLE, ONLINE JOURNAL, WEBSITE, NEWSPAPER ARTICLE: ")
    if source == "BOOK":
        book()
    elif source == "CHAPTER":
        chapter()
    elif source == "ENCYCLOPEDIA":
        encyclopedia()
    elif source == "JOURNAL ARTICLE":
        journal_article()
    elif source == "ONLINE JOURNAL":
        online_journal()
    elif source == "WEBSITE": 
        website()
    elif source == "NEWSPAPER ARTICLE":
        newspaper_article()
    else: 
        print("Sorry! At this moment, only footnotes citing a BOOK, ENCYCLOPEDIA, CHAPTER, JOURNAL ARTICLE, ONLINE JOURNAL, WEBSITE, CHAPTER, and NEWSPAPER ARTICLE could be generated! We're looking to expand this generator over time.")
    print("Here is your footnote!")

def book():
    author_name = ask_author_name()
    title = ask_title()
    editors = ask_editors()
    # translator = ask_translator()
    edition = ask_edition()
    publisher = ask_publisher()
    year = ask_year()
    
    print(author_name + "," , "'" + title + "'" , "in", editors , "(eds)" + "," , title, "(" + "tr" + "," , publisher + "," , str(year) +")")
          
def encyclopedia():
    title = ask_title()
    edition = ask_edition()
    year = ask_year()
    volume = ask_volume()
    paragraph = int(input("Paragraph number:"))

    print(title, "(" + edition, "edn" + "," , str(year) + ")" , "vol" , str(volume) + "," , "para" , paragraph)

def chapter():
    author_name = ask_author_name()
    title = ask_title()
    editors = ask_editors()
    publisher = ask_publisher()
    year = ask_year()

    print(author_name, "'" + title + "'" , "in" , editors , "(eds)" + "," , title , "(" + publisher , str(year) + ")")

def journal_article():
    author_name = ask_author_name()
    title = ask_title()
    year = ask_year()
    journal =  str(input("Journal:"))
    volume = ask_volume()
    issue = ask_issue()
    starting_page = int(input("First page of article:"))
    cited_page = int(input("Cited page of article:"))
    
    print(author_name + ",",title,"("+str(year)+")", str(volume) + "(" + str(issue) + ")" , journal,  str(starting_page)+ ",", str(cited_page)+".")

def online_journal():
    author_name = ask_author_name()
    author_name = ask_author_name
    title = ask_title()
    year = ask_year()
    journal = ask_journal
    volume = ask_volume()
    issue = ask_issue()
    link = ask_link()
    date_accessed = ask_date_accessed()

    print(author_name + "," , "'" + title + "'" , "(" + year + ")" , str(volume) ,"(" + issue + ")" , journal + "<"+link+">" , "accessed" , date_accessed )

def website():
    author_name = ask_author_name()    
    title = str(input("Website or blog title:"))
    date = str(input("Date of publication:"))
    publisher = str(input("Publisher:"))
    link = str(input("Link:"))
    date_accessed = str(input("Date accessed:"))

    print(author_name + ",", "'" + title + "'" ,"("+ publisher +","+ date_published +")","<"+link+">", "accessed", date_accessed+".")

def newspaper_article():
    author_name = ask_author_name()
    title = ask_title()
    publisher = ask_publisher()
    place_published = ask_place_published()
    date_published = ask_date_published()
    page_cited = int(input("Page cited:"))

    print(author_name + "," , "'" + title + "'" , publisher , "(" + place_published + "," , date_published + ")" ,  page_cited)

#Asking functions below:
def ask_author_name():
    author_name = str(input("Author name (If two authors, separate with and. If multiple, use first author and place et al.):"))
    return author_name

def ask_editors():
    editors = str(input("Editors:"))
    return editors
 
def ask_title():
    title = str(input("Title:"))
    return title

def ask_journal():
    journal =  str(input("Journal:"))

def ask_volume():
    volume = int(input("Volume:"))
    return volume

def ask_issue():
    issue = int(input("Issue:"))
    return issue

def ask_translator_name():
    translator_needed = bool(input("Is this book translated? If so, type TRUE:"))
    if translator_needed == True:
        translator_name = str(input("Translator name:"))
        return translator_name
    else:
        pass

def ask_edition():
    edition = str(input("Edition (e.g 1st, 2nd, 3rd, etc.): "))
    return edition

def ask_publisher():
    publisher = str(input("Publisher:"))
    return publisher

def ask_year():
    year = int(input("Year:"))
    return year

def ask_link():
    link = str(input("Link:"))
    return link

def ask_date_accessed():
    date_accessed = str(input("Date accessed:"))
    return date_accessed

def ask_place_published():
    place_publised = str(input("Place published:"))
    return place_publised

def ask_date_published():
    date_published = str(input("Date of publication (e.g 1 Jan 2023)"))
    return date_published

if __name__ == '__main__':
    main()
