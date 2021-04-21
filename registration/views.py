from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm





# Create your views here.

def register(request):
    """Handle a registration request to create a new user account"""

    # process a registration form to create a new account
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            # redirect to the login page
            return redirect("/login")
        else:
            print(form.errors)
            context = {'form': form}
    # provide a registration form to the user
    else:
        # create a form and send it back to the user to fill in
        form = UserCreationForm()
        context = {'form': form}

    return render(request, 'registration/register.html', context)
