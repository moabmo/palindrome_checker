from django.shortcuts import render
from django.http import HttpResponse

def is_palindrome(request):
    input_string = request.GET.get('input_string', '')
    result = "It is a palindrome." if input_string == input_string[::-1] else "The string is not a palindrome."
    return render(request, 'is_palindrome.html', {'result': result})
