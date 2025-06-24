from keras.models import load_model

# Load your .h5 model
model = load_model("model/efficientnetb3-Chicken Disease-98.27.h5")

# Save in new Keras format
model.save("model/chicken_model.keras")

print("✅ Model converted to .keras format successfully.")
