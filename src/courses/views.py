# from django.http import Http404
# from django.urls import reverse

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from .models import Course
from .forms import CourseModelForm

from django.views import View

# Create your views here.

# An example of Raw Class method based on Views
#
#

# service class that contains the get_object Method in one place
# to be used in other classes
# Could be just defined in other classes
class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        context = {}
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj


class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *kargs, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)



# example of filtered list view
class CourseListViewFiltered(CourseListView):
    queryset = Course.objects.all().filter(id=1)



class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *kargs, **kwargs):
        # Uncomment if not using the CourseObjectMixin
        #
        # context = {}
        # if id is not None:
        #     obj = get_object_or_404(Course, id=id)
        # else:
        #     obj = ''
        # context['object'] = obj
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)



class CourseCreateView(View):
    template_name = 'courses/course_update.html'

    # GET method
    def get(self, request, *kargs, **kwargs):
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *kargs, **kwargs):
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)




class CourseUpdateView(CourseObjectMixin, View):
    template_name = 'courses/course_update.html'

    # Uncomment if not using the CourseObjectMixin
    #
    # def get_object(self):
    #     context = {}
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id is not None:
    #         obj = get_object_or_404(Course, id=id)
    #     return obj

    # GET method
    def get(self, request, id=None, *kargs, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    # POST method
    def post(self, request, id=None, *kargs, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)



class CourseDeleteView(CourseObjectMixin, View):
    template_name = 'courses/course_delete.html'

    # Uncomment if not using the CourseObjectMixin
    #
    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id is not None:
    #         obj = get_object_or_404(Course, id=id)
    #     return obj

    # GET method
    def get(self, request, id=None, *kargs, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    # POST method
    def post(self, request, id=None, *kargs, **kwargs):
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)



# # HTTP Method
# def my_fbv(request, *kargs, **kwargs):
#     return render(request, 'about.html', {})
