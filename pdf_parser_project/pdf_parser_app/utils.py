import PyPDF2


import pdfplumber   # pip install pdfplumber
from operator import itemgetter
import json
# function to extract navlog information from PDF
def parse_pdf(file, navlog_type="MAIN"):
    #  Read PDF file
    with pdfplumber.open(file) as pdf:
        # find page count
        total_no_of_pages = len(pdf.pages)

        # declate empty list to store text content and table content
        pdf_content = []
        pdf_tables = []

        #  loop pdf pages
        for i in range(0, total_no_of_pages):
            # select pdf page
            pdf_page = pdf.pages[i]

            # extract text content & append it to pdf_content list
            extracted_data = pdf_page.extract_words(x_tolerance=3, y_tolerance=3, keep_blank_chars=True, use_text_flow=True, horizontal_ltr=True, vertical_ttb=True, extra_attrs=[], split_at_punctuation=False)
            pdf_content.extend(extracted_data)

            # extract table contents
            # find tables in selected pdf page
            tables = pdf_page.find_tables()
            for j in range(0, len(tables)):
                table = tables[j]

                # get table box bound values - x0,x1, top, bottom
                x0,  x1, top, bottom = 0, pdf_page.width, table.bbox[1], table.bbox[3],

                # if table width is less than half of the page change its width
                if table.bbox[0] > pdf_page.width / 2 :
                    x0 = pdf_page.width / 2

                # if table staring position (x0) is greater than half of the page change its x0 value
                if table.bbox[2] < pdf_page.width / 2 :
                    x1 = pdf_page.width / 2

                #  crop image using box bound value
                croppage = pdf_page.crop((x0, top, x1, bottom))
                edge_left = sorted(croppage.horizontal_edges, key=itemgetter("x0"))[0]
                edge_right = sorted(croppage.horizontal_edges, key=itemgetter("x1"))[-1]
                # extract table value and append it in pdf_table list
                extracted_tables =  croppage.extract_table({"vertical_strategy": "lines", "explicit_vertical_lines": [edge_left["x0"], edge_right["x1"]]})
                pdf_tables.append(extracted_tables)
                for i in pdf_tables:
                    for j in i:
                        if j==['', None]:
                            del i[i.index(j)]

                dic={}
                for i in pdf_tables:
                    for j in i:
                        for k in j:
                            r=j.index(k)
                            if k==None:
                                break
                            elif k =='':
                                o=j.index(k)
                                dic.update({head:dic[head]+', '+j[0+1]})
                                break
                            else:
                                dic.update({j[r]: j[r+1]})
                                head=j[r]
                                break
                        

        # print(pdf_content)
        # print(pdf_tables)

        

	
        # return json_output
        # print('-----------')
        # print(json_output)
        # print('-----------')
        return dic