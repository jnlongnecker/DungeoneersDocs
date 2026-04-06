from pathlib import Path

# Extract the topic from a header line
def extract_topic(line: str):
	val = line[line.find("# ") + 2:line.find("\n")]
	print("[extract_topic] Completed")
	return val

# Extract all explicit references in a line
def extract_references(line: str, existing_references: dict[str, int]):
	curr_token = ""
	i = 0
	while i < len(line):
		curr_char = line[i]
		i = i+1
		if curr_char == "`" and i < len(line):
			curr_char = line[i]
			while i < len(line) and curr_char != "`":
				curr_token += curr_char
				i = i+1
				curr_char = line[i]
			count = existing_references.get(curr_token, 0)
			count = count + 1
			existing_references[curr_token] = count
			curr_token = ""
			i = i+1
	print("[extract_references] Completed")

# Parse a file for topics & references
def parse(file, topics: dict[str, int], references: dict[str, int]):
	line = file.readline()
	while line:
		if line[0] == "#":
			topic = extract_topic(line)
			count = topics.get(topic, 0)
			count = count + 1
			topics[topic] = count
		else:
			extract_references(line, references)
		line = file.readline()
	print("[parse] Completed")

"""
	MAIN FUNCTIONALITY ===
"""
__dir = "e:\\Godot\\Projects\\Dungeoneers\\docs\\"
ruleDir = Path(__dir + "rulesLite")
topics: dict[str, int] = {}
references: dict[str, int] = {}

# Get just the .md files
mdFiles = list(ruleDir.glob('*.md'))
for file in mdFiles:
	with file.open("r") as f:
		# Open each file and parse out topics & references
		print("[main] Parsing " + file.name)
		parse(f, topics, references)

# Map topics -> references to the topic
print("[main] Mapping references")
mapping: dict[str, list[str]] = {}
unmapped: list[str] = []
ambiguous: list[str] = [] # Tracks references that could refer to multiple topics (bad)

for reference in references.keys():
	lower_ref = reference.lower()
	matched = False
	is_ambiguous = False

	# Check if this reference exactly matches a topic
	for topic in topics.keys():
		lower_topic = topic.lower()

		# If it's a match, add to the mapping
		if lower_ref == lower_topic:
			refs = mapping.get(topic, [])
			refs.append(reference)
			mapping[topic] = refs
			# If it had already been matched, its ambiguous
			if matched:
				is_ambiguous = True
			else:
				matched = True
	# If unmatched after all topics, it's unmapped
	if not matched:
		unmapped.append(reference)
print("[main] Mapping completed")

# Print to file the results of the mapping
mappingFile = __dir + "gen\\mapping.txt"
unmappedFile = __dir + "gen\\unmapped.txt"
ambiguousFile = __dir + "gen\\ambiguous.txt"

print("[main] Writing to mapping file")
with open(mappingFile, 'w') as file:
	for key in mapping:
		file.write(key)
		file.write(" -> ")
		file.write(", ".join(mapping[key]))
		file.write('\n')

print("[main] Writing to unmapped reference file")
with open(unmappedFile, 'w') as file:
	for val in unmapped:
		instances = references[val]
		file.write(val)
		file.write(" | ")
		file.write(str(instances))
		file.write(" instances")
		file.write('\n')

print("[main] Writing ambiguous references file")
with open(ambiguousFile, 'w') as file:
	for val in ambiguous:
		file.write(val)
		file.write('\n')

print("[main] Finished, exiting")