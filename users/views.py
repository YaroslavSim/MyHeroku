from django.shortcuts import render

from users.forms import SignUpForm

from django.contrib.sites.shortcuts import get_current_site

from django.utils.http import urlsafe_base64_encode

from django.template.loader import render_to_string

from users.token import account_activation_token

from django.utils.encoding import force_bytes, force_str


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            token = account_activation_token.make_token(user)
            user_id = urlsafe_base64_encode(force_bytes(user.pk))
            message = render_to_string('users/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'user_id': user_id,
                'token': token
            })
            user.email_user(subject, message)
            return render(request, 'users/account_activation_sent.html')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def activate(request, user_id, token):
    try:
        user_id = force_text(urlsafe_base64_decode(user_id))
        user = User.objects.get(pk=user_id)
    except (TypeError, ValueError, ObjectDoesNotExist):
        user = None

    if user and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/students/')

    return render(request, 'users/account_activation_invalid.html')
