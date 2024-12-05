data = []

data_min = min(data)
data_max = max(data)
scaled_data = []

for k in data:
    scaled_value = (k - data_min) / (data_max - data_min)
    scaled_data.append(scaled_value)

print(sorted(scaled_data))