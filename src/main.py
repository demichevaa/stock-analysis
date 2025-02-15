import sources.alpha_vantage as av

res = av.get_time_series_monthly("IBM")
print(res)