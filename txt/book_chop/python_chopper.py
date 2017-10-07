import re

with open("new_magick.txt") as f:
	full_text = f.readlines()
full_text = [x.strip() for x in full_text]

current_iteration = "Iteration 1";
diversity = '0.24';

divs = {'0.24' : open("div_24", "a"),
		'0.42' : open("div_42", "a"),
		'0.5' : open("div_5", "a"),
		'0.6' : open("div_6", "a"),
		'0.666' : open("div_666", "a"),
		'0.7' : open("div_7", "a"),
		'0.777' : open("div_777", "a"),
		'0.8' : open("div_8", "a"),
		'0.9' : open("div_9", "a"),
		'1.0' : open("div_1", "a")}

def write_diversity():
	for num, div in divs.iteritems():
		div.write("Diversity " + num + "\n\n")

def write_iteration(iteration):
	for num, div in divs.iteritems():
		div.write("\n" + iteration + "\n\n")

write_diversity()
write_iteration(current_iteration)
for line in full_text[:]:
	if line[35:44] == "Iteration":
		current_iteration = "Iteration " + str(line[45:])
		write_iteration(current_iteration)
	elif line[6:16] == "diversity:":
		diversity = re.search('----- (.*)----- Generating with seed:', line)
		diversity = diversity.group(1)[10:]
	else:
		divs[diversity].write(line + "\n")
