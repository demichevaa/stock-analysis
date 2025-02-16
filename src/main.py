import sources.alpha_vantage_api as av
from common.project_context import ProjectContext
from storage.local import local_write

DATA_PATH = ProjectContext().local_file_storage_path
res = av.get_time_series_monthly("IBM")

print(res)

local_write(res, DATA_PATH + "ibm__alpha_vantage__time_series_monthly.parquet")

#from sources.eodhd_api import api as eodhd

