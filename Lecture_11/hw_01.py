def csv_open(path):
	with open(path, "r", encoding = "utf_8_sig") as f:
		ret = [list(map(float, row.replace("\n", "").split(","))) for row in f]
	return ret

def cmap(temp, _min, _max):
	middle = (_min + _max) / 2
	if temp < middle:
		return "#" + format(int(255 * (temp - _min) / (middle - _min)), 'X').zfill(2) * 2 + "FF"
	else:
		return "#FF" + format(255 - int(255 * (temp - middle) / (_max - middle)), 'X').zfill(2) * 2

def write_html(path, data):
	with open(path, "w", encoding = "utf_8_sig") as f:
		f.write(data)

records = csv_open("tokyo.csv")
_min = min([min(r[1:]) for r in records])
_max = max([max(r[1:]) for r in records])

output = """<!DOCTYPE html>
  <style>
    table {
      border-top: 1px solid;
      border-bottom: 1px solid;
    }
  </style>
<h1>Temperatures in Tokyo</h1>
<table>
<tr>
<th> - 
"""
for i in range(1, 13): output += " <th> " + str(i)
output += " </tr>\n"
for r in records:
	output += "<tr>\n<td>" + str(int(r[0]))
	for x in r[1:]:
		output += "<td style=\"background-color: {}\"> {}\n".format(cmap(x, _min, _max), x)
	output += "</tr>"
output += "</table>\n</html>"

write_html("tokyo.html", output)
