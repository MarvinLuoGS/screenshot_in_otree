import pandas as pd
import base64
import os

# 输入和输出配置
csv_file = 'shot_2025-02-24.csv'  # CSV 文件路径
output_dir = 'output_images'  # 保存图片的目录

# 创建输出目录（如果不存在）
os.makedirs(output_dir, exist_ok=True)

# 读取 CSV 文件
df = pd.read_csv(csv_file)

# 遍历每一行，转换 Base64 数据为图片
for index, row in df.iterrows():
    # 获取 session、participant、timestamp 和 Base64 数据
    session = row['session']
    participant = row['participant']
    timestamp = row['timestamp']
    image_data = row['image_data']

    # 如果 Base64 数据包含 "data:image/png;base64," 前缀，去掉前缀
    if image_data.startswith('data:image'):
        base64_string = image_data.split(',')[1]
    else:
        base64_string = image_data  # 假设没有前缀

    try:
        # 解码 Base64 数据为二进制
        image_bytes = base64.b64decode(base64_string)

        # 用 session、participant 和 timestamp 生成文件名
        # 替换 timestamp 中的特殊字符，避免文件路径问题
        safe_timestamp = timestamp.replace(':', '-').replace('.', '-')
        file_name = f'{session}-{participant}-{safe_timestamp}.png'
        file_path = os.path.join(output_dir, file_name)

        # 保存为 PNG 文件
        with open(file_path, 'wb') as f:
            f.write(image_bytes)
        print(f'已保存图片: {file_path}')

    except Exception as e:
        print(f'转换失败（行 {index}）: {e}')

print('所有图片转换完成！')