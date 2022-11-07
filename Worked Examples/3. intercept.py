
def Hactober():
    bookmarks_final = ''
    email_final = ''

    count_email = 0
    count_bmk = 0

    with open('bookmarks.txt') as bmk:
        bookmarks = bmk.readlines()
        for j in bookmarks:
            bookmarks_final.join(bookmarks[count_bmk])
            count_bmk += 1

    with open('email.txt') as eml:
        email = eml.readlines()
        for i in email:
            email_final.join(email[count_email])
            count_email += 1
            

    return 'Joseph is doing it'
    
