def htmlId3Decisions(decisions, f):
    '''
    Analyzes a single node in the decision tree and creates part of the HTML page based on it
    '''
    f.write("<table><tr><th>{}</th></tr>\n".format(decisions[0][0]))
    for d in decisions:
        f.write("<tr><td>{}</td>\n".format(d[1]))
        if type(d[2]) == type(''):
            f.write("<td>{}</td></tr>\n".format(d[2]))
        else:
            f.write("<td>")
            htmlId3Decisions(d[2], f)
            f.write("</td></tr>")
    f.write("</table>")

def html(decisions, fileName):
    '''
    Outputs an HTML page as a visualization of the ID3 decision tree, where decisions is the decision tree and fileName will be the filename of the output file
    '''
    with open(fileName, "w") as f:
        f.write('''<!DOCTYPE html>
            <html>
            <style>
            td,th { vertical-align: top; border: 1px solid grey }
            </style>
            <body>''')
        htmlId3Decisions(decisions, f)
        f.write("</body>\n</html>\n")
