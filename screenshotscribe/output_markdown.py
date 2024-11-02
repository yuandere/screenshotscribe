import re
from screenshotscribe.utils import open_file


def escape_special_characters(input_string):
    if '`' in input_string:
        return input_string
    
    patterns = [r"<", r">", r"\$\$", r"\&\&", r"\%\%", r"\*", r"\*\*", r"\*\*\*", r"\[", r"\]"]
    combined_pattern = '|'.join(patterns)

    def escape_match(match):
        return ''.join(f'\\{char}' for char in match.group(0))

    escaped_string = re.sub(combined_pattern, escape_match, input_string)

    return escaped_string


def output_markdown(generated_data):
    errors = 0
    markdown_content = ''

    for item in generated_data:
        escaped = escape_special_characters(item["text"])
        markdown_content += f'{escaped}\n'
        if item['success'] != True:
            errors += 1
            markdown_content += f'File: *{item["filename"]
                                          }* Date created: *{item["date_created"]}*\n'
        markdown_content += '- - -\n'

    status = f'**{len(generated_data)} images successfully transcribed**\n\n' if errors == 0 else f'**{errors}/{len(
        generated_data)} images not able to be transcribed. Review each corresponding finish reason for more information.**\n\n'

    filename = 'transcribed.md'
    with open(filename, 'w', encoding='utf-8', errors='ignore') as md_file:
        md_file.write(status + markdown_content)

    print(f'Markdown file generated at {filename}')

    open_file(filename)
