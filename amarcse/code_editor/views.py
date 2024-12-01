import subprocess
from .forms import SnippetForm
from .models import Snippet
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


def code_editor(request):
    output = None
    error = None
    saved_snippet = None

    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            title = form.cleaned_data['title']


            try:
                result = subprocess.run(
                    ['python', '-c', code],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                output = result.stdout
                error = result.stderr
            except subprocess.TimeoutExpired:
                error = "Code execution timed out."
            except Exception as e:
                error = str(e)


            if request.user.is_authenticated:
                saved_snippet = Snippet.objects.create(
                    user=request.user,
                    title=title,
                    code=code,
                    output=output,
                    error=error,
                )
        else:
            error = "Invalid form submission."
    else:
        form = SnippetForm()


    snippets = Snippet.objects.filter(user=request.user).order_by('-created_at') if request.user.is_authenticated else None

    return render(request, 'editor/code_editor.html', {
        'form': form,
        'output': output,
        'error': error,
        'saved_snippet': saved_snippet,
        'snippets': snippets,
    })



from django.shortcuts import render, redirect
from .models import Snippet

def view_snippets(request):
    if request.user.is_authenticated:
        snippets = Snippet.objects.filter(user=request.user).order_by('-created_at')
        return render(request, 'editor/view_snippets.html', {'snippets': snippets})
    else:

        return redirect('login')


def delete_snippet(request, snippet_id):
    if request.user.is_authenticated:
        snippet = get_object_or_404(Snippet, id=snippet_id, user=request.user)
        snippet.delete()
        return redirect('view_snippets')
    else:
        return redirect('login')

