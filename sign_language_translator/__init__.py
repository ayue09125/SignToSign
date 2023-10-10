"""
sign_language_translator
========================
Code: https://github.com/sign-language-translator/sign-language-translator
Help: https://sign-language-translator.readthedocs.io

This project is an effort to bridge the communication gap between the hearing and the hearing-impaired community using Artificial Intelligence.
The goal is to provide a user friendly API to novel Sign Language Translation solutions that can easily adapt to any regional sign language.

Usage
-----

.. code-block:: python

    import sign_language_translator as slt

    # download dataset or models (if you need them for personal use)
    # (by default, resources are auto-downloaded within the install directory)
    # slt.set_resource_dir("path/to/folder")  # Helps preventing duplication across environments or using cloud synced data
    # slt.utils.download_resource(".*.json")  # downloads into resource_dir
    # print(slt.Settings.FILE_TO_URL.keys())  # All downloadable resources

    print("All available models:")
    print(list(slt.ModelCodes))  # slt.ModelCodeGroups
    # print(list(slt.TextLanguageCodes))
    # print(list(slt.SignLanguageCodes))
    # print(list(slt.SignFormatCodes))

    # -------------------------- TRANSLATE: text to sign --------------------------

    import sign_language_translator as slt

    # Load text-to-sign model
    # deep_t2s_model = slt.get_model("t2s-flan-T5-base-01.pt") # pytorch

    # rule-based model (concatenates clips of each word)
    t2s_model = slt.models.ConcatenativeSynthesis(
        text_language = "urdu", # or object of any child of slt.languages.text.text_language.TextLanguage class
        sign_language = "pakistan-sign-language", # or object of any child of slt.languages.sign.sign_language.SignLanguage class
        sign_format = "video", # or object of any child of slt.vision.sign.Sign class
    )

    text = "HELLO دنیا!" # HELLO treated as an acronym
    sign_language_sentence = t2s_model(text)

    # slt_video_object.show() # class: slt.vision.sign.Sign
    # slt_video_object.save(f"sentences/{text}.mp4")

    # -------------------------- TRANSLATE: sign to text --------------------------

    import sign_language_translator as slt

    # load sign
    video = slt.Video("video.mp4")
    # features = slt.extract_features(video, "mediapipe_pose_v2_hand_v1")

    # Load sign-to-text model
    # deep_s2t_model = slt.get_model(slt.ModelCodes.TRANSFORMER_S2T) # pytorch
    deep_s2t_model = slt.get_model("gesture_mp_base-01") # pytorch

    # translate via single call to pipeline
    # text = deep_s2t_model.translate(video)

    # translate via individual steps
    features = deep_s2t_model.extract_features(video.iter_frames())
    encoding = deep_s2t_model.encoder(features)
    # logits = deep_s2t_model.decoder(encoding, token_ids = [0])
    # logits = deep_s2t_model.decoder(encoding, token_ids = [0, logits.argmax(dim=-1)])
    # ...
    tokens = deep_s2t_model.decode(encoding) # uses beam search to generate a token sequence
    text = "".join(tokens) # deep_s2t_model.detokenize(tokens)

    print(features.shape)
    print(logits.shape)
    print(text)
"""

from sign_language_translator import (
    config,
    data_collection,
    languages,
    models,
    text,
    utils,
    vision,
)
from sign_language_translator.config import enums
from sign_language_translator.config.enums import ModelCodeGroups, ModelCodes
from sign_language_translator.config.enums import SignFormats as SignFormatCodes
from sign_language_translator.config.enums import SignLanguages as SignLanguageCodes
from sign_language_translator.config.enums import TextLanguages as TextLanguageCodes
from sign_language_translator.config.settings import Settings, set_resources_dir
from sign_language_translator.languages import get_sign_language, get_text_language
from sign_language_translator.models import get_model

__version__ = config.helpers.get_package_version()

__all__ = [
    # config
    "set_resources_dir",
    "Settings",
    "__version__",
    # modules
    "vision",
    "text",
    "data_collection",
    "models",
    "languages",
    "utils",
    "config",
    "enums",
    # classes (enum)
    "ModelCodes",
    "TextLanguageCodes",
    "SignLanguageCodes",
    "SignFormatCodes",
    "ModelCodeGroups",
    # object loaders
    "get_sign_language",
    "get_text_language",
    "get_model",
]
