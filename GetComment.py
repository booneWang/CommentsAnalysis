import urllib.request as urlrequest
import json
import re
import time
import pandas as pd
import random
from pandas.io.json import json_normalize

# ITEM_ID = "546408734932"
ITEM_ID = "558185566672"
ITEM_ID = "558517626411" #Vapromax
ITEM_ID = "39356129215" #关门神器


# Read Tmall Rate Comment
# item_id : Tmall product D
# page : the page # of rate comment
def read_url(item_id, page, try_times=2):
    # Check try times
    if try_times == 0:
        return ""

    # set up delay
    time.sleep(random.randint(5, 10) / 10)

    # Tmall Rate Comment Link Template
    url_template = "https://rate.tmall.com/list_detail_rate.htm?itemId={0}&spuId=520897750&sellerId=890482188&order=3&currentPage={1}"
    url = url_template.format(item_id, page)
    content = urlrequest.urlopen(url).read()
    content = content.decode("gbk")

    # Tmall is in json format with additional disturbing information
    # using regular to remove the additional info
    cleaned_content = re.findall("\\{.*?\\}$", content)

    if cleaned_content.__len__() > 0:
        return json.loads(cleaned_content[0])
    else:
        # In case failed by Taobao Security Matrix, then try within try times limitation
        time.sleep(random.randint(15, 25) / 10)
        return read_url(item_id, page, try_times - 1)


# First Read
json_content = read_url(ITEM_ID, 1)
pages = int(json_content["paginator"]["lastPage"])
df_rate = pd.DataFrame()
print("*** Total {} Pages ***".format(pages))

# read page from second page
for i in range(1, pages + 1):
    json_content = read_url(ITEM_ID, i)
    if json_content != "":
        df = json_normalize(json_content["rateList"])
        df_rate = df_rate.append(df, True)

        print('---Page {:0>2} read---'.format(i))
    else:
        print('---Page {:0>2} failed---'.format(i))

file_name = "{}.csv".format(ITEM_ID)
# df_rate.to_csv(file_name, encoding="utf16")
df_rate.to_csv(file_name)
