""" using module to print and finish printing """
import printing_functions as pf
unprinted_designs = ["casita", "gundam", "tower", "base", "clip"]
finished_printing = []

pf.print_models(unprinted_designs, finished_printing)
pf.show_completed_models(finished_printing)
