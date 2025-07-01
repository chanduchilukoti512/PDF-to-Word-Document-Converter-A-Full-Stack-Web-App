from django.db import models

class UploadedPDF(models.Model):
    pdf_file = models.FileField(upload_to='pdfs/')
    converted_file = models.FileField(upload_to='docs/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)