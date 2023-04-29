from django.shortcuts import render

from django.http import HttpResponseRedirect
from .forms import PDFUploadForm
from .models import Record,MyData
from .utils import parse_pdf

def pdf_parser(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.cleaned_data['pdf_file']
            parsed_data = parse_pdf(pdf_file)
            MyData.objects.all().delete()
            for i in parsed_data:
                if parsed_data[i]:
                    my_data=MyData(key1=i,value1=parsed_data[i])
                    my_data.save()



            #MyData=Record.objects.create(**parsed_data)
            #record=Record.objects.create(**parsed_data)
            #for data in parsed_data:
                #print(data)
                #record = Record.objects.create(**data)
            return HttpResponseRedirect('record_list/')
    else:
        form = PDFUploadForm()
        parsed_data = None
    return render(request, 'pdf_parser.html', {'form': form, 'parsed_data': parsed_data})

from django.shortcuts import render
from .models import Record

def record_list(request):
    records = MyData.objects.all()
    return render(request, 'record_list.html', {'records': records})

from rest_framework import generics
from .models import MyData
from .serializers import MyDataSerializer

class MyDataListCreate(generics.ListCreateAPIView):
    queryset = MyData.objects.all()
    
    serializer_class = MyDataSerializer

class MyDataRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyData.objects.all()
    serializer_class = MyDataSerializer


from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from .models import MyData

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.utils import simpleSplit

def download_pdf(request):
    # Get all records from the model
    mydata = MyData.objects.all()

    # Create a PDF file with a larger canvas size and smaller margins
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    pdf.leftMargin = 50
    pdf.bottomMargin = 50
    pdf.rightMargin = 50
    pdf.topMargin = 50

    # Write the records to the PDF
    y = 750
    for data in mydata:
        text = data.key1 + ': ' + data.value1
        lines = simpleSplit(text, pdf._fontname, pdf._fontsize, pdf._pagesize[0]-pdf.leftMargin-pdf.rightMargin)
        height = len(lines) * pdf._leading
        if y - height < 50:
            pdf.showPage()
            y = 750
        for line in lines:
            pdf.drawString(100, y, line)
            y -= pdf._leading

        y -= pdf._leading

    # Close the PDF file
    pdf.save()

    # Get the PDF content from the buffer
    buffer.seek(0)
    pdf_content = buffer.getvalue()

    # Create an HTTP response with the PDF content
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mydata.pdf"'

    return response
