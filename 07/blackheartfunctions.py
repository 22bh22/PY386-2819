def int_or_float_no_error(s):
	try:
		float(s)
	except ValueError:
		return None
	else:
		s = float(s)
	if s % 1 == 0:
		s = int(s)
	return s

def int_or_float(s):
	s = float(s)
	if s % 1 == 0:
		s = int(s)
	return s