import numpy as np

# image = np.zeros((224,224,3), dtype = np.uint8)
# print(image.shape)

# image_batch = np.random.randint(
#     0,256,
#     size=(32,224,224,3),
#     dtype= np.uint8
# )

# print(image_batch.shape)

numbers = np.random.rand(1_000_000)

result = numbers * 2 + 10
print(result[:5])