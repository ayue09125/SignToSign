import sign_language_translator as slt

# The core model of the project (rule-based text-to-sign translator)
# which enables us to generate synthetic training datasets
model = slt.models.ConcatenativeSynthesis(
   text_language="english", sign_language="pk-sl", sign_format="video" )

# text = "یہ بہت اچھا ہے۔" # "this-very-good-is"
# sign = model.translate(text) # tokenize, map, download & concatenate
# sign.show()

model.sign_format = slt.SignFormatCodes.LANDMARKS
model.sign_embedding_model = "mediapipe-world"

# ==== English ==== #
model.text_language = slt.languages.text.English()
sign_2 = model.translate("This is an apple.")
sign_2.show()

# # ==== Hindi ==== #
# model.text_language = slt.TextLanguageCodes.HINDI
# sign_3 = model.translate("कैसे हैं आप?") # "how-are-you"
# sign_3.save_animation("how-are-you.gif", overwrite=True)