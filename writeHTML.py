import webbrowser

f = open('helloworld.html','w')

message = """<html>
<head></head>
<body><p>Hello World from Python!</p></body>
</html>"""

f.write(message)
f.close()

filename = 'https://www.kristynl.com/Exploration2/CS4830-Exploration2/helloworld.html'
webbrowser.get("C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s").open(filename, new=2)