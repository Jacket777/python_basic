import PyPDF2

def get_pdf():
    # 二进制模式打开
    with open('meetingminutes.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        print("num page", str(pdf_reader.numPages))
        page = pdf_reader.getPage(0)
        content = page.extractText()
        print(content)


def decrypt_pdf():
    with open('encrypted.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        if pdf_reader.isEncrypted:
            print("加密文档......")
            # 解密
            pdf_reader.decrypt('rosebud')
        page = pdf_reader.getPage(0)
        content = page.extractText()
        print(content)


# 不能用with 方式打开
def copy_pdf():
    pdf_writer = PyPDF2.PdfFileWriter()
    file01 = open('meetingminutes.pdf', 'rb')
    pdf1_reader = PyPDF2.PdfFileReader(file01)
    total_pageNum = pdf1_reader.numPages
    print("total_pageNum", str(total_pageNum))
    for pageNum in range(total_pageNum):
        page = pdf1_reader.getPage(pageNum)
        pdf_writer.addPage(page)

    file02 = open('meetingminutes2.pdf', 'rb')
    pdf2_reader = PyPDF2.PdfFileReader(file02)
    total_pageNum = pdf2_reader.numPages
    for pageNum in range(total_pageNum):
        page = pdf2_reader.getPage(pageNum)
        pdf_writer.addPage(page)



    # 写入文件
    file03 = open('combinedminutes.pdf', 'wb')
    pdf_writer.write(file03)
    file03.close()



# 旋转页面并保存
def rotate_pdf():
    with open('meetingminutes.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        page = pdf_reader.getPage(0)

        # 无旋转API



# 无加水印


# 加密 无效---加密后为文档为空白
def encrypt_pdf():
    pdf_writer = PyPDF2.PdfFileWriter()
    with open('meetingminutes.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        for pagNum in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(pagNum))
    pdf_writer.encrypt('swordfish')
    with open('encryptedminutes.pdf', 'wb') as f:
        pdf_writer.write(f)




if __name__ == '__main__':
    # get_pdf()
    # decrypt_pdf()
    copy_pdf()
    # encrypt_pdf()