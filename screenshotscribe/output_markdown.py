from screenshotscribe.utils import open_file

def output_markdown(generated_data):
    errors = 0
    markdown_content = ''

    for item in generated_data:
        markdown_content += f'- {item["text"]}\n'
        if item['success'] != True:
            errors += 1
            markdown_content += f'File: *{item["filename"]}* Date created: *{item["date_created"]}*\n'
        markdown_content += '- - -\n'

    status = f'**{len(generated_data)} images successfully transcribed**\n\n' if errors == 0 else f'**{errors}/{len(generated_data)} images not able to be transcribed. Review each corresponding finish reason for more information.**\n\n'

    filename = 'transcribed.md'
    with open(filename, 'w') as md_file:
        md_file.write(status + markdown_content)

    print(f'Markdown file generated at {filename}')

    open_file(filename)