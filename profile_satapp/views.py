from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView

from plancoach.decorators import is_teacher
from profile_satapp.decorators import profile_sat_ownership_required
from profile_satapp.forms import Profile_satCreateForm
from profile_satapp.models import Profile_sat
from profileapp.models import Profile


class Profile_satCreateView(CreateView):
    model = Profile_sat
    form_class = Profile_satCreateForm
    template_name = 'profile_satapp/create.html'


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        target_profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        kwargs['target_profile'] = target_profile
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        target_profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        context['target_profile'] = target_profile
        return context

    def form_valid(self, form):
        target_profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        form.instance.profile = target_profile
        form.instance.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profileapp:detail', kwargs={'pk': self.kwargs['pk']})


class Profile_satDeleteView(DeleteView):
    model = Profile_sat
    context_object_name = 'target_profile_sat'
    template_name = 'profile_satapp/delete.html'
    def get_success_url(self):
        return reverse_lazy('profileapp:detail', kwargs={'pk': self.object.profile.pk})


class Profile_satUpdateView(UpdateView):
    model = Profile_sat
    form_class = Profile_satCreateForm
    context_object_name = 'target_profile_sat'
    template_name = 'profile_satapp/update.html'
    def get_success_url(self):
        return reverse_lazy('profileapp:detail', kwargs={'pk': self.object.profile.pk})



