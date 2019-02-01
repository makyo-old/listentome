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
    if record.status == 'a' or record.status = 'r':
        if request.method == "GET":
            return render_to_response("circulation/checkout.html",
                    context_instance = RequestContext(request,
                        {'record': record}))
        else:
            form = CheckoutForm(request.POST)
            if form.is_valid():
                can_check_out = False
                if record.status == 'a':
                    can_check_out = True
                elif record.status == 'r':
                    for reservation in record.reserverecord_set.all():
                        if reservation.reserved_for == form.user:
                            can_check_out = True
                            break
                if can_check_out:
                    form.save()
                    return HttpResponseRedirect(record.get_absolute_url())
            else:
                return render_to_response("circulation/checkout.html",
                        context_instance = RequestContext(request,
                            {'record': record, 'form': form}))
    # Return message saying unable to check out

@permission_required("record.can_checkin")
def checkin(request, record_id):
    record = get_object_or_404(Record, pk = record_id)

@login_required
def reserve(request, record_id):
    pass

@login_required
def dereserve(request, record_id):
    pass
