from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import get_object_or_404, render_to_response
from listentome.circulation.models import *
from listentome.catalog.models import *

@permission_required("record.can_checkout")
def checkout(request, record_id):
    if request.method == "GET":
        record = get_object_or_404(Record, pk = record_id)
        return render_to_response("circulation/checkout.html",
                context_instance = RequestContext(request,
                    {'record': record}))
    else:
        pass

@permission_required("record.can_checkin")
def checkin(request, record_id):
    pass

@login_required
def reserve(request, record_id):
    pass

@login_required
def dereserve(request, record_id):
    pass
