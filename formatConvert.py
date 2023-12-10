import pandas as pd
import json

# 读取CSV文件
csv_path = "20230929-jinshitan.csv"  # 替换为你的CSV文件路径
df = pd.read_csv(csv_path)

# 将数据转换为JSON格式
json_data = {"list": []}

for _, row in df.iterrows():
    entry = {"image": row["url"], "title": "", "description": ""}
    json_data["list"].append(entry)

# 将JSON数据写入文件
json_output_path = "output.json"  # 替换为你希望保存的JSON文件路径
with open(json_output_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"Conversion completed. JSON file saved at: {json_output_path}")
