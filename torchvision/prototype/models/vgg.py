import warnings
from functools import partial
from typing import Any, Optional

from torchvision.transforms.functional import InterpolationMode

from ...models.vgg import VGG, make_layers, cfgs
from ..transforms.presets import ImageNetEval
from ._api import Weights, WeightEntry
from ._meta import _IMAGENET_CATEGORIES


__all__ = [
    "VGG",
    "VGG11Weights",
    "VGG11BNWeights",
    "VGG13Weights",
    "VGG13BNWeights",
    "VGG16Weights",
    "VGG16BNWeights",
    "VGG19Weights",
    "VGG19BNWeights",
    "vgg11",
    "vgg11_bn",
    "vgg13",
    "vgg13_bn",
    "vgg16",
    "vgg16_bn",
    "vgg19",
    "vgg19_bn",
]


def _vgg(arch: str, cfg: str, batch_norm: bool, weights: Optional[Weights], progress: bool, **kwargs: Any) -> VGG:
    if weights is not None:
        kwargs["num_classes"] = len(weights.meta["categories"])
    model = VGG(make_layers(cfgs[cfg], batch_norm=batch_norm), **kwargs)
    if weights is not None:
        model.load_state_dict(weights.state_dict(progress=progress))
    return model


_common_meta = {
    "size": (224, 224),
    "categories": _IMAGENET_CATEGORIES,
    "interpolation": InterpolationMode.BILINEAR,
    "recipe": "https://github.com/pytorch/vision/tree/main/references/classification#alexnet-and-vgg",
}


class VGG11Weights(Weights):
    ImageNet1K_RefV1 = WeightEntry(
        url="https://download.pytorch.org/models/vgg11-8a719046.pth",
        transforms=partial(ImageNetEval, crop_size=224),
        meta={
            **_common_meta,
            "acc@1": 69.020,
            "acc@5": 88.628,
        },
    )


class VGG11BNWeights(Weights):
    ImageNet1K_RefV1 = WeightEntry(
        url="https://download.pytorch.org/models/vgg11_bn-6002323d.pth",
        transforms=partial(ImageNetEval, crop_size=224),
        meta={
            **_common_meta,
            "acc@1": 70.370,
            "acc@5": 89.810,
        },
    )


class VGG13Weights(Weights):
    ImageNet1K_RefV1 = WeightEntry(
        url="https://download.pytorch.org/models/vgg13-19584684.pth",
        transforms=partial(ImageNetEval, crop_size=224),
        meta={
            **_common_meta,
            "acc@1": 69.928,
            "acc@5": 89.246,
        },
    )


class VGG13BNWeights(Weights):
    ImageNet1K_RefV1 = WeightEntry(
        url="https://download.pytorch.org/models/vgg13_bn-abd245e5.pth",
        transforms=partial(ImageNetEval, crop_size=224),
        meta={
            **_common_meta,
            "acc@1": 71.586,
            "acc@5": 90.374,
        },
    )


class VGG16Weights(Weights):
    ImageNet1K_RefV1 = WeightEntry(
        url="https://download.pytorch.org/models/vgg16-397923af.pth",
        transforms=partial(ImageNetEval, crop_size=224),
        meta={
            **_common_meta,
            "acc@1": 71.592,
            "acc@5": 90.382,
        },
    )


class VGG16BNWeights(Weights):
    ImageNet1K_RefV1 = WeightEntry(
        url="https://download.pytorch.org/models/vgg16_bn-6c64b313.pth",
        transforms=partial(ImageNetEval, crop_size=224),
        meta={
            **_common_meta,
            "acc@1": 73.360,
            "acc@5": 91.516,
        },
    )


class VGG19Weights(Weights):
    ImageNet1K_RefV1 = WeightEntry(
        url="https://download.pytorch.org/models/vgg19-dcbb9e9d.pth",
        transforms=partial(ImageNetEval, crop_size=224),
        meta={
            **_common_meta,
            "acc@1": 72.376,
            "acc@5": 90.876,
        },
    )


class VGG19BNWeights(Weights):
    ImageNet1K_RefV1 = WeightEntry(
        url="https://download.pytorch.org/models/vgg19_bn-c79401a0.pth",
        transforms=partial(ImageNetEval, crop_size=224),
        meta={
            **_common_meta,
            "acc@1": 74.218,
            "acc@5": 91.842,
        },
    )


def vgg11(weights: Optional[VGG11Weights] = None, progress: bool = True, **kwargs: Any) -> VGG:
    if "pretrained" in kwargs:
        warnings.warn("The argument pretrained is deprecated, please use weights instead.")
        weights = VGG11Weights.ImageNet1K_RefV1 if kwargs.pop("pretrained") else None
    weights = VGG11Weights.verify(weights)

    return _vgg("vgg11", "A", False, weights, progress, **kwargs)


def vgg11_bn(weights: Optional[VGG11BNWeights] = None, progress: bool = True, **kwargs: Any) -> VGG:
    if "pretrained" in kwargs:
        warnings.warn("The argument pretrained is deprecated, please use weights instead.")
        weights = VGG11BNWeights.ImageNet1K_RefV1 if kwargs.pop("pretrained") else None
    weights = VGG11BNWeights.verify(weights)

    return _vgg("vgg11_bn", "A", True, weights, progress, **kwargs)


def vgg13(weights: Optional[VGG13Weights] = None, progress: bool = True, **kwargs: Any) -> VGG:
    if "pretrained" in kwargs:
        warnings.warn("The argument pretrained is deprecated, please use weights instead.")
        weights = VGG13Weights.ImageNet1K_RefV1 if kwargs.pop("pretrained") else None
    weights = VGG13Weights.verify(weights)

    return _vgg("vgg13", "B", False, weights, progress, **kwargs)


def vgg13_bn(weights: Optional[VGG13BNWeights] = None, progress: bool = True, **kwargs: Any) -> VGG:
    if "pretrained" in kwargs:
        warnings.warn("The argument pretrained is deprecated, please use weights instead.")
        weights = VGG13BNWeights.ImageNet1K_RefV1 if kwargs.pop("pretrained") else None
    weights = VGG13BNWeights.verify(weights)

    return _vgg("vgg13_bn", "B", True, weights, progress, **kwargs)


def vgg16(weights: Optional[VGG16Weights] = None, progress: bool = True, **kwargs: Any) -> VGG:
    if "pretrained" in kwargs:
        warnings.warn("The argument pretrained is deprecated, please use weights instead.")
        weights = VGG16Weights.ImageNet1K_RefV1 if kwargs.pop("pretrained") else None
    weights = VGG16Weights.verify(weights)

    return _vgg("vgg16", "D", False, weights, progress, **kwargs)


def vgg16_bn(weights: Optional[VGG16BNWeights] = None, progress: bool = True, **kwargs: Any) -> VGG:
    if "pretrained" in kwargs:
        warnings.warn("The argument pretrained is deprecated, please use weights instead.")
        weights = VGG16BNWeights.ImageNet1K_RefV1 if kwargs.pop("pretrained") else None
    weights = VGG16BNWeights.verify(weights)

    return _vgg("vgg16_bn", "D", True, weights, progress, **kwargs)


def vgg19(weights: Optional[VGG19Weights] = None, progress: bool = True, **kwargs: Any) -> VGG:
    if "pretrained" in kwargs:
        warnings.warn("The argument pretrained is deprecated, please use weights instead.")
        weights = VGG19Weights.ImageNet1K_RefV1 if kwargs.pop("pretrained") else None
    weights = VGG19Weights.verify(weights)

    return _vgg("vgg19", "E", False, weights, progress, **kwargs)


def vgg19_bn(weights: Optional[VGG19BNWeights] = None, progress: bool = True, **kwargs: Any) -> VGG:
    if "pretrained" in kwargs:
        warnings.warn("The argument pretrained is deprecated, please use weights instead.")
        weights = VGG19BNWeights.ImageNet1K_RefV1 if kwargs.pop("pretrained") else None
    weights = VGG19BNWeights.verify(weights)

    return _vgg("vgg19_bn", "E", True, weights, progress, **kwargs)
