from atlassian import Confluence

confluence = Confluence(
    url='https://ivand.atlassian.net',
    username='ivanskyd@gmail.com',
    password='09PKKHn00tuJNCKbYvuT1FB5')

status = confluence.create_page(
    space='MYSTUFF',
    title='This is a test page created by my Python script',
    body='This is the body. You can use <strong>HTML tags</strong>!')

print(status)