library = {
    "books": [
        "Harry Potter",
        "The Hobbit",
        "Story Book",
        "Sherlock Holmes",
        "Fairy Tales"
    ]
}

print("===== LIBRARY ORGANIZER =====")


print("Books in Library:")
print(library["books"])


library["books"].append("Comic Book")
print("After Adding a Book:")
print(library["books"])


library["books"].remove("The Hobbit")
print("After Removing a Book:")
print(library["books"])


library["books"].sort()
print("Sorted Books:")
print(library["books"])


library["books"].sort(reverse=True)
print("Reverse Sorted Books:")
print(library["books"])


print("Book at Index 1:")
print(library["books"][1])


print("Books from Index 1 to 3:")
print(library["books"][1:4])