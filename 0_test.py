full_names = ['Rachel Raccoon', 'Joe Plumber']

#WRONG - TRYING TO APPEND THE EXISTING FULL_NAMES LIST while LOOPING
    #ON THE FULL_NAMES LIST

# for full_name in full_names:
#   first_last = full_name.split()
#   initials = first_last[0][0] + first_last[1][0]
#   full_names.append(initials)  # MISTAKE!


#BETTER SOLUTION:

# def slice_initials_list_from_full_names(full_names):
#   initials_list = []
#   for full_name in full_names:
#     first_last = full_name.split()
#     initials = first_last[0][0] + first_last[1][0]
#     initials_list.append(initials)
#   return initials_list


def slice_initials_from_full_name(full_name):
  first_last = full_name.split()
  return first_last[0][0] + first_last[1][0]

def slice_initials_list_from_full_names(full_names):
  initials_list = []
  for full_name in full_names:
    initials = slice_initials_from_full_name(full_name)
    initials_list.append(initials)
  return initials_list

slice_initials_list_from_full_names(full_names)

initials = slice_initials_list_from_full_names(full_names)

print(initials)