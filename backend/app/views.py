from app.models import GuestbookEntry
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    if request.POST:
        new_gb_entry = GuestbookEntry(
            name=request.POST["post_request_name"],
            email=request.POST["post_request_email"],
            comment=request.POST["post_request_comment"]
        )
        new_gb_entry.save()
    context["guestbook_entries"] = GuestbookEntry.objects.all()
    return render(request, "index.html", context)
