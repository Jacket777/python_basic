# code02 从多个PDF中合并旋转的页面
import PyPDF2,os



def get_all_pdf():
    # Get all the PDF filenames
    pdfFiles = []
    for filename in os.listdir(''):
        if filename.endswith('.pdf'):
            # print(filename)
            pdfFiles.append(filename)
    pdfFiles.remove('encrypted.pdf')
    pdfFiles.remove('encryptedminutes.pdf')
    pdfFiles.sort()
    pdf_writer = PyPDF2.PdfFileWriter()
    print(pdfFiles)
    # TODO  loop through al the PDF files
    for filename in pdfFiles:
        pdf_file = open(filename, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        # loop through all the pages (except the first) and add them
        total_num = pdf_reader.numPages
        for pageNum in range(1, total_num):
            page = pdf_reader.getPage(pageNum)
            pdf_writer.addPage(page)

    # TODO: Save the resulting PDF to a file
    result = open('allminutes.pdf', 'wb')
    pdf_writer.write(result)
    result.close()


if __name__ == '__main__':
    get_all_pdf()



