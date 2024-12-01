import wikipedia


def main():
    search_input = input("Enter a page title: ")
    while search_input != "":
        try:
            page = wikipedia.page(search_input)
            print(f"{page.title}\n{page.summary}\n{page.url}\n")

        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_input}" does not match any pages. Try another id!\n')

        search_input = input("Enter a page title: ")

    print("Thank you.")


# Start the program
main()
