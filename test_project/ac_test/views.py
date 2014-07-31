from django.forms.models import modelformset_factory, formset_factory
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext

from forms import FormulaRow

# Create your views here.

def test_view(request):
    page_title = "Test View"

    FormulaFormSet = formset_factory(FormulaRow, extra=5, can_delete=True)

    if request.method == 'POST':
        formset = FormulaFormSet(request.POST)
        if formset.is_valid():
            HttpResponseRedirect('/foobar')

    else:
        formset = FormulaFormSet()

    return render_to_response('ac_test/test_view.html',
                      {'page_title': page_title,
                       'formset': formset.forms,
                       'management_form': formset.management_form,
                       },
                       context_instance=RequestContext(request))