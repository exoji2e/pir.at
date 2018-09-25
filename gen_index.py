partys = [
        ["https://piratpartiet.se", "&#x1F1F8;&#x1F1EA; Piratpartiet"],
        [ "https://piratar.is/", "&#x1F1EE;&#x1F1F8; Píratapartýið"],
        ["https://www.piratenpartei.de/","&#x1F1E9;&#x1F1EA; Piratenpartei"],
        ["https://www.pirati.cz/", "&#x1F1E8;&#x1F1FF Pirátská Strana"]
        ]
header = """---
layout: base
title: Home
---
<style>
.box {
  background-color: #512483;
  color: white;
  margin: 1em 1em;
  padding: 1em 1em;
  text-decoration: none;
  font-size: 24px;
  width: 250px;
  border-radius: 25px;
}
</style>"""
t1 = '''<div class="col-xs-8 col-sm-6 col-md-3">
  <a href="'''
t2 = '''">
    <div class="box">'''
t3 = '''</div>
  </a>
</div>'''

print(header)
for url, s in partys:
    print(t1 + url + t2 + s + t3)
