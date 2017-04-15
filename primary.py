from note_handling import *
from variables import paths

contexts = read_contexts()
write_date_to_contexts(contexts, paths)
rename_all_files(paths)
contexts = daily_retrieve(contexts, paths)
write_contexts(contexts)
#write_to_context_files(c_dict, paths)