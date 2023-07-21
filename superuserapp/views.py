from datetime import datetime

from django.db.models.functions import Cast
from django.db.models import IntegerField
from django.views.generic import TemplateView
from accountapp.models import CustomUser
from documentapp.models import Document
from profileapp.models import Profile
from refundapp.models import Refund
from salaryapp.models import Salary
from teacherapplyapp.models import Teacherapply
from plancoach.updaters import *
from django.utils.decorators import method_decorator

#1 로그인  3슈퍼유저
class SuperuserDashboardView(TemplateView):
    model = CustomUser
    template_name = 'superuserapp/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profiles = Profile.objects.annotate(username_as_int=Cast('teacher__username', IntegerField())).order_by('username_as_int')
        context['profiles'] = profiles
        context['salarys'] = Salary.objects.filter(is_given=False, salaryday__lte=datetime.now().date())
        context['refunds'] = Refund.objects.filter(is_given=False)
        context['teacherapplys'] = Teacherapply.objects.filter(is_done=True)
        context['document'] = Document.objects.all().first()
        return context

