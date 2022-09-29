# 20220919 - Python Advanced - Python
# Conversion from number seconds to time in the format (hh:mm:ss) with trimming of the amount above 24 hrs

def convert_seconds_to_hh_mm_ss(seconds):
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'result: {hours:02d}:{minutes:02d}:{seconds:02d}')


data_in = float(input('\nEnter a integer (seconds) to convert to "hh:mm:ss" 24 hr timeframe. Count starts from 00:00:00\n'
                      'If amount entered exceeds 24 hr period, result is trimmed to [00:00:00 <= result <= 23:59:59]\n'
                      'If amount entered is a float. Portion after decimal point is ignored.\n'
                      '\nenter seconds >>> : '))

data_to_convert_to_hh_mm_ss = int(data_in)

convert_seconds_to_hh_mm_ss(data_to_convert_to_hh_mm_ss)

# - input value of seconds is given in the function

# - result after "seconds %= 86400" is a number under 86400.
#       - If seconds >= 86400, portions sized 86400 are subtracted until result comes under 86400
#       - If seconds < 86400, no change in the result

# - result after "seconds %= 3600" is a number under 3600.
#       - If seconds >= 3600, portions sized 3600 are subtracted until result comes under 3600
#       - If seconds < 3600, no change in the result

# - result after "seconds %= 60" is a number under 60.
#       - If seconds >= 60, portions sized 60 are subtracted until result comes under 60
#       - If seconds < 60, no change in the result
