from functions import export_postcodes, postcode_ranges, make_included_list

# enter path of input file
CSV_INPUT= 'postcodes_no_service.csv'

# enter filename for excluded areas file
FILENAME_EXCLUDED = 'excluded_areas.csv'   

# enter filename for included area file
FILENAME_INCLUDED = 'included_areas.csv'

# generate csv file with excluded delivery areas
export_postcodes(postcode_ranges(CSV_INPUT), FILENAME_EXCLUDED)

# generatie csv file with included delivery areas based in the excluded range
export_postcodes(make_included_list(FILENAME_EXCLUDED), FILENAME_INCLUDED)