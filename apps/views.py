from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from django.shortcuts import render, redirect
from django.core.mail import send_mail  # elekton pochtaga habar yuborish
from apps.forms import ModelForm
from apps.models import Meet


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        msg = f"""
                From: {name}
                Email: {email}
                Massage: {message}
                """
        send_mail(
            subject=subject,
            message=msg,
            from_email=email,
            recipient_list=['muhammadbilol40@gmail.com'],
            fail_silently=True
        )
        return redirect('/')
    return render(request, 'index.html')


class Home(CreateView):
    template_name = 'index.html'
    model = Meet
    form_class = ModelForm
    success_url = reverse_lazy('index')


# meetings list.
class Create(ListView):
    model = Meet
    template_name = 'meetings.html'
    paginate_by = 1


# paginate_by = None


# view  edd meeting
class Edit(CreateView):
    model = Meet
    form_class = ModelForm
    template_name = 'addMeeting.html'
    success_url = reverse_lazy('index')


class MeetingDetailView(DetailView):
    template_name = 'meeting-details.html'
    model = Meet
    context_object_name = 'meeting'


class Update(UpdateView):
    template_name = 'update.html'
    model = Meet
    context_object_name = 'meeting'
    form_class = ModelForm
    success_url = reverse_lazy('add')


class MeetDeleteView(DeleteView):
    model = Meet
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

def search(request):
    query = request.GET.get('search')
    meetings = Meet.objects.filter(name__icontains=query)
    return render(request, 'meetings.html', {'meetings': meetings})

# =================================================================


# from django.views import generic
#
#
# class HomeView(generic.View, generic.base.ContextMixin):
#     template_name = 'home.html'
#     form_class = forms.ContactModelForm
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data()
#
#         search = request.GET.get('search')
#         if search:
#             context = models.Meeting.objects.filter(name__icontains=search)
#
#         return render(request, self.template_name, context)
#
#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#
#         msg = f"""
#                 From: {name}
#                 Email: {email}
#                 Massage: {message}
#                 """
#         send_mail(
#             subject=subject,
#             message=msg,
#             from_email=email,
#             recipient_list=['muhammadbilol40@gmail.com'],
#             fail_silently=True
#         )
#         return redirect('/')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["meetings"] = models.Meet.objects.all()[:4]
#         return context
#
#
# class MeetingCreateRetrieveUpdateDelete(generic.View):
#     template_name = 'meeting.html'
#     form_class = forms.MeetModelForm
#     success_url = _('')
#
#     def post(self, request, *args, **kwargs):
#         pass
#
#     def get(self, request, *args, **kwargs):
#         pass
#
#     def put(self, request, *args, **kwargs):
#         pass
#
#     def delete(self, request, *args, **kwargs):
#         pass
