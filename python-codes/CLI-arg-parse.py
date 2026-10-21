import argparse

parser = argparse.ArgumentParser(
    description= " Deep learning model settings"
)

parser.add_argument(
"--epochs",
type = int,
default= 10,
help = "Number of training epochs"
)

parser.add_argument(
    "--batch_size",
    type = int,
    default = 32,
    help = "Training batch size"
)

parser.add_argument(
    "--learning_rate",
    type = float,
    default = 0.001,
    help = "Laening rate"
)

args = parser.parse_args()

# 4. Use the values
print("Epochs:", args.epochs)
print("Batch Size:", args.batch_size)
print("Learning Rate:", args.learning_rate)