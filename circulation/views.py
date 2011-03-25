from django.contrib.auth.decorators import permission_required, login_required
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from listentome.circulation.models import *
from listentome.circulation.forms import *
from listentome.catalog.models import *

@permission_required("record.can_checkout")
def checkout(request, record_id):
    record = get_object_or_404(Record, pk = record_id)
if request.method == "GET":
        return render_to_response("circulation/checkout.html",
                context_instance = RequestContext(request,
                    {'record': record}))
    else:
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(record.get_absolute_url())
        else:
            return render_to_response("circulation/checkout.html",
                    context_instance = RequestContext(request,
                        {'record': record, 'form': form}))

@permission_required("record.can_checkin")
def checkin(request, record_id):
    pass

@login_required
def reserve(request, record_id):
    pass

@login_required
def dereserve(request, record_id):
    pass
