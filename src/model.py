import tensorflow as tf
import numpy as np

class Model:

    piece_map = {
        "Pawn": 0, # white
        "Knight": 1, # white
        "Bishop": 2, # white
        "Rook": 3, # white
        "Queen": 4, # white
        "King": 5, # white
        "pawn": 6, # black
        "knight": 7, # black
        "bishop": 8, # black
        "rook": 9, # black
        "queen": 10, # black
        "king": 11 # black
    }
    
    def __init__(self, game) -> None:
        try:
            self.model = tf.keras.models.load_model("chess_model.h5") # load model
        except FileNotFoundError:
            # create model
            self.model = tf.keras.Sequential([
                tf.keras.layers.Flatten(input_shape=(8, 8, 12)), # 8x8, 12 fifures figures (6 white & 6 black)
                tf.keras.layers.Dense(128, activation="relu"),
                tf.keras.layers.Dense(64, activation="relu"),
                tf.keras.layers.Dense(1, activation="linear")
            ])

            self.model.compile(optimizer="adam", loss="mean_squared_error", metrics=["accuracy"]) # compile model
            X_train, y_train = None, None

            #self.model.fit(X_train, y_train, epochs=5) 
            #self.model.save("chess_model.h5") # save model