# Pinterest practice:

# Your company runs a social networking website, and you are working on the user profiles.

# When registering on your website, users provided their full name, which is composed of one first name (mandatory), zero or more middle names, and one last name (mandatory). Some possible full names are:

# John Smith
# Anna Maria Simpson
# Bob Alan Faria Stewart
# Implement the function answer, which returns an abbreviated version of the full name. In the abbreviated version, all names except for the first and the last should be abbreviated to one letter. For example, the full names above should be abbreviated as:

# John Smith
# Anna M. Simpson
# Bob A. F. Stewart
# Your answer may assume the input is always valid.
# Save your code in /home/candidate/candidate_files/py/answer.py

# Please refer to the Debug tab for the instructions on how to test your answer.


def answer(self, name):
	"""
	input type: str
	return type: str
	"""
	if not name:
		return ""

	pname = name.split()

	if len(pname) < 2:
		return "Please provide both your first and last names!"

	if len(pname) == 2:
		return name

	res = pname[0]
	if len(pname) > 2:
		c = []
		for i, v in enumrate(pname[1:-1]):
			c.append(v[0]+".")

	res += " " + ' '.join(c) + " " + pname[-1]
	return res  


















