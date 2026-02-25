from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from studentorg.models import Organization, Student, College, Program, OrgMember 
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy
from django.db.models import Q

# --- HOME ---
class HomePageView(ListView):  
    model = Organization  
    context_object_name = 'home'  
    template_name = "home.html"

# --- ORGANIZATION ---
class OrganizationList(ListView):  
    model = Organization  
    context_object_name = 'object_list' 
    template_name = 'org_list.html'  
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs


class OrganizationCreateView(CreateView): 
    model = Organization 
    form_class = OrganizationForm 
    template_name = 'org_form.html' 
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView): 
    model = Organization 
    form_class = OrganizationForm 
    template_name = 'org_form.html' 
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView): 
    model = Organization 
    template_name = 'org_del.html' 
    success_url = reverse_lazy('organization-list')

# --- STUDENT ---
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(
                Q(lastname__icontains=query) | 
                Q(firstname__icontains=query) | 
                Q(student_id__icontains=query)
            )
        return Student.objects.all()

class StudentCreateView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

# --- COLLEGE ---
class CollegeListView(ListView):
    model = College
    template_name = 'college_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return College.objects.filter(
                Q(college_name__icontains=query)
            )
        return College.objects.all()

class CollegeCreateView(CreateView):
    model = College
    fields = '__all__'
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    fields = '__all__'
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

# --- PROGRAM ---
class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Program.objects.filter(
                Q(prog_name__icontains=query) | 
                Q(college__college_name__icontains=query)
            )
        return Program.objects.all()

class ProgramCreateView(CreateView):
    model = Program
    fields = '__all__'
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    fields = '__all__'
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

# --- ORGMEMBER ---
class OrgMemberListView(ListView):
    model = OrgMember
    template_name = 'orgmember_list.html'
    context_object_name = 'object_list'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return OrgMember.objects.filter(
                Q(student__lastname__icontains=query) | 
                Q(student__firstname__icontains=query) |
                Q(organization__name__icontains=query)
            )
        return OrgMember.objects.all()

class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = '__all__'
    template_name = 'orgmember_form.html'
    success_url = reverse_lazy('orgmember-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')