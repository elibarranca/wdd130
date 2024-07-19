#establish variables
max_chapters = 0

#Open the file, read through it line by line, separate the line into the appropriate pieces and display each book in this format:

with open("books_and_chapters.txt") as reading_file:
    for line in reading_file:
        clean_line = line.strip()
        words = clean_line.split(":")
        name = words[0]
        chapters = int(words[1])
        book = words[2]
        print(f"Scrptires: {book}, Book: {name}, Chapters: {chapters}")

        if chapters

        parts = line.split(":")
        book = parts[0].strip()
        chapters = int(parts[1])
        scripture = parts[2].strip()

        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")


#Find the largest number of chapters in the scriptures.
#Find the book that has the largest number of chapters in the scriptures.
        #set loop
        if chapters > max_chapters:

            max_chapters = chapters
            book_with_max = book

            print(f"The largest number of chapters in the scriptures is {book_max}.")
            print(f"In the book of {max_chapters}.")
