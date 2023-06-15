from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):
    """View for home page."""
    return render(
        request, 'home.html', {'user': request.user}
    )