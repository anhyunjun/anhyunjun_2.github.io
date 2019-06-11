from django.shortcuts import render
import cgi, cgitb

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def count(request):
#     full_text = request.GET['fulltext']
#     return render(request, 'wordcount/count.html', {'fulltext': full_text})

# def count(request):
#     full_text = request.GET['fulltext']

#     word_list = full_text.split()

#     return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list)})

def count(request):
    full_text = request.GET['fulltext']
    
    word_list = full_text.split()

    word_dictionary = {}
    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})
