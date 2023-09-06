from django import forms


class ExcelImportForm(forms.Form):
    excel_file = forms.FileField(label="Upload Excel File")