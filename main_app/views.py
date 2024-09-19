from django.shortcuts import render

# Create your views here.


def add_to_file(word1: str, word2: str):
    with open("file.txt", "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")


def read_from_file():
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    return words1, words2


def home(request):
    return render(request, 'home.html')


def words_list(request):
    words1, words2 = read_from_file()
    
    words = zip(words1, words2)
    return render(request, 'words_list.html', context={'words': words})


def add_word(request):
    if request.method == 'POST':
        word1 = request.POST['word1']
        word2 = request.POST['word2']
        add_to_file(word1, word2)
    return render(request, 'add_word.html')