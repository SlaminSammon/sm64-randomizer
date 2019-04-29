def hexlify(l):
  if type(l) == list or type(l) == tuple:
    return [(hexlify(v)) for v in l]
  else:
    if l == None:
      return 'None'
    else:
      return hex(l)

def format_binary(bin_data):
  if bin_data is None:
    return 'NO DATA'

  return ' '.join(hex(b)[2:].upper().rjust(2, '0') for b in bin_data)

def pretty_print_table(title, data):
  print(title.center(73, "-"))
  longest_line = max([len(label) for label in data.keys()])

  for (label, value ) in data.items():
    print(f' {str(label).ljust(longest_line + 2, " ")} {str(value).ljust(longest_line + 2, " ")}')
    
  print("-" * 73)
  print()