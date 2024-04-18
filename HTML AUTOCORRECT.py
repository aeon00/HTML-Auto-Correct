import tidylib

# HTML code to be corrected
html = """
<html>
    <head>
        <title>Test Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a test page.</p>
    </body>
</html>
"""

# Use pytidy to correct the HTML code
tidy_html, errors = tidylib.tidy_document(html)

# Print the corrected HTML code
print(errors)