import csv
from django.http import HttpResponse

def lottosPurchased(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date', 'HowMany'])
    writer.writerow(['2014-02-13', '2'])

    return response