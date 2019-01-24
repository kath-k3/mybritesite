from django.urls import reverse_lazy
from .models import Client, FeatureRequest, ProductArea
from .forms import FeatureRequestForm
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


class FeatureRequestCreateView(CreateView):

    model = FeatureRequest
    form_class = FeatureRequestForm
    success_msg = "Feature Request created!"
    template_name = 'featurereq/featurerequest_create.html'
    success_url = reverse_lazy('featurereq:index')

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super().form_valid(form)


class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    #fields = '__all__'
    success_msg = "Feature Request updated!"
    context_object_name = 'feature_request'
    template_name = 'featurereq/featurerequest_update.html'



class FeatureRequestDetailView(DetailView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    context_object_name = 'feature_request'
    template_name = 'featurereq/featurerequest_detail.html'



class FeatureRequestListView(ListView):
    model = FeatureRequest
    slug_field = 'title'
    slug_url_kwarg = 'title'
    context_object_name = 'feature_requests'
    template_name = 'featurereq/featurerequest_list.html'
    success_url = reverse_lazy('featurereq:index')



class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    template_name = 'featurereq/featurerequest_delete.html'
    context_object_name = 'feature_request'
    success_url = reverse_lazy('featurereq:index')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Your feature request was deleted!')
        return super(FeatureRequestDeleteView, self).delete(request, *args, **kwargs)
