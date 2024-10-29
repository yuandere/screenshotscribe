from docx import Document
from docx.enum.text import WD_COLOR_INDEX

from screenshotscribe.utils import open_file


def output_document(generated_data):
    document = Document()
    font = document.styles['Normal'].font
    font.name = 'Arial'
    
    status = document.add_paragraph()
    errors = 0

    for item in generated_data:
        bullet = document.add_paragraph()
        run = bullet.add_run(item['text'], style='List Bullet')
        if item['success'] != True:
            errors += 1
            run2 = bullet.add_run(' ' + item['filename'] + ' ' +
                                 item['date_created'])
            run.bold, run2.bold = True
            run.font.highlight_color, run2.font.highlight_color = WD_COLOR_INDEX.YELLOW
            continue

    if errors == 0:
        run = status.add_run(f'{len(generated_data)} images successfully transcribed')
    else:
        run = status.add_run(f'{errors}/{len(generated_data)} images not able to be transcribed. Review each corresponding finish reason for more information')
        run.font.highlight_color = WD_COLOR_INDEX.YELLOW
    run.bold = True

    filename = 'transcribed.docx'
    document.save(filename)
    print(f'Document generated at {filename}')

    open_file(filename)
