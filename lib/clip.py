import requests
from PIL import Image
from transformers import CLIPProcessor, CLIPModel


def clip_demo(image=None, desc=None, model="openai/clip-vit-base-patch32", processor="openai/clip-vit-base-patch32"):
    """
    This function uses the CLIP model to classify an image based on a given set of text descriptions.
    If no image is provided, it will download and use a default image from the COCO dataset.

    Parameters:
    - image (PIL.Image.Image, optional): The image to classify. If not provided, a default image will be downloaded.
    - model (str, optional): The name or path of the CLIP model to use. Defaults to "openai/clip-vit-base-patch32".
    - processor (str, optional): The name or path of the CLIP processor to use. Defaults to "openai/clip-vit-base-patch32".

    Returns:
    - probs (torch.Tensor): A tensor containing the probabilities of the image belonging to each text description.
    """
    model = CLIPModel.from_pretrained(model)
    processor = CLIPProcessor.from_pretrained(processor)

    url = "http://images.cocodataset.org/val2017/000000039769.jpg" # two cats
    images = image if image is not None else Image.open(requests.get(url, stream=True).raw)
    text = desc if desc is not None else ["a photo of a cat", "a photo of a dog"]
    print(f"Images: {images}")
    print(f"Text: {text}")
    inputs = processor(text=text, images=images, return_tensors="pt", padding=True)

    outputs = model(**inputs)
    logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
    probs = logits_per_image.softmax(dim=1)  # we can take the softmax to get the label probabilities
    print(f"Probs: {probs}")
