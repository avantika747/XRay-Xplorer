from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

''' This code is used to generate pdfs of the reports that the doctors make. Once the doctor enters the 
patient's details in the report, the xhtml2pdf converts the html form of the report to pdf for easy download.'''

def generate_report_as_pdf(report_html, filename):
    # Generate PDF from HTML content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{filename}_report.pdf"'
    pisa_status = pisa.CreatePDF(
        report_html, dest=response
    )
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + report_html + '</pre>')
    return response