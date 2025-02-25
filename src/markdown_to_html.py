# std libs
import os

# 3rd party libs
import mistune

# constants
PATH_TO_CURRENT_FOLDER: str = os.getcwd()
PATH_TO_HTML_INPUT: str = os.path.join(PATH_TO_CURRENT_FOLDER,"html_template.html")
PATH_TO_HTML_OUTPUT: str = os.path.join(PATH_TO_CURRENT_FOLDER,"html_report.html")
PATH_TO_MARKDOWN_INPUT: str = os.path.join(PATH_TO_CURRENT_FOLDER,"lab4.md")
REPORT_TITLE: str = "Network Lab 4"

# functions
def getFile(path_to_file: str) -> str:
    with open(path_to_file,"r") as input_file:
        result: str = input_file.read()
    return result

def buildReport(html_report: str, markdown_report: str) -> str:
    markdown_to_html: str = mistune.html(markdown_report)
    result: str = (
        html_report
        .replace("{{placeholder_title}}",REPORT_TITLE)
        .replace("{{placeholder_html}}",markdown_to_html)
        .replace("<p><img ",'<br><p><img class="resized-images" ')
        .replace('title="Image" /></p>','title="Image" /></p><br>')
        .replace("<table>",'<br><div class="table-centered"><table>')
        .replace("</table>","</table></div><br><br>")
    )
    return result

def saveReport(path_to_file: str, html_report: str) -> None:
    with open(path_to_file,"w") as output_file:
        output_file.write(html_report)

def runAll() -> None:
    html_input: str = getFile(PATH_TO_HTML_INPUT)
    markdown_input: str = getFile(PATH_TO_MARKDOWN_INPUT)
    parsed_report: str = buildReport(html_input,markdown_input)
    saveReport(PATH_TO_HTML_OUTPUT,parsed_report)

if __name__ == "__main__":
    runAll()