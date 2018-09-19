
# ファイルパス一括取得ノート

import glob

parent_path = '/parent_path/**'

# ぜんぶ。
for path in glob.glob(parent_path, recursive=True):
    print(path)

# 直下のみ。
# for path in glob.glob(parent_path):
#     print(path)
