```python
import PyPDF2

def extract_titles_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        num_pages = pdf_reader.numPages

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            title = text.split('\n')[0]  # فرض بر این است که تایتل در خط اول هر صفحه قرار دارد
            print(title)