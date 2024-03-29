"""
MIT License

Copyright (c) 2020 Mahdi S. Hosseini

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import torch

from models.vgg import VGG
from models.dpn import DPN92
# from .lenet import *
from models.senet import SENet18
# from .pnasnet import *
from models.densenet import densenet_cifar
from models.googlenet import GoogLeNet
from models.shufflenet import ShuffleNetG2
from models.shufflenetv2 import ShuffleNetV2
from models.resnet import ResNet34
from models.resnext import ResNeXt29_2x64d
from models.preact_resnet import PreActResNet18
from models.mobilenet import MobileNet
from models.mobilenetv2 import MobileNetV2
from models.efficientnet import EfficientNetB0
from models.SqueezeNet import SqueezeNet
from models.own_network import DASNet34, DASNet50

def get_net(network: str, num_classes,init_adapt_conv_size=None) -> torch.nn.Module:
    return VGG('VGG16', num_classes=num_classes) if network == 'VGG16' else \
        ResNet34(num_classes=num_classes) if network == 'ResNet34' else \
        PreActResNet18(num_classes=num_classes) if network == 'PreActResNet18' else \
        GoogLeNet(num_classes=num_classes) if network == 'GoogLeNet' else \
        densenet_cifar(num_classes=num_classes) if network == 'densenet_cifar' else \
        ResNeXt29_2x64d(num_classes=num_classes) if network == 'ResNeXt29_2x64d' else \
        MobileNet(num_classes=num_classes) if network == 'MobileNet' else \
        MobileNetV2(num_classes=num_classes) if network == 'MobileNetV2' else \
        DPN92(num_classes=num_classes) if network == 'DPN92' else \
        ShuffleNetG2(num_classes=num_classes) if network == 'ShuffleNetG2' else \
        SENet18(num_classes=num_classes) if network == 'SENet18' else \
        ShuffleNetV2(1, num_classes=num_classes) if network == 'ShuffleNetV2' else \
        SqueezeNet(num_classes=num_classes) if network == 'SqueezeNet' else \
        EfficientNetB0(
            num_classes=num_classes) if network == 'EfficientNetB0' else \
        DASNet34(num_classes=num_classes) if network == 'DASNet34' else \
        DASNet50(num_classes=num_classes) if network == 'DASNet50' else None
