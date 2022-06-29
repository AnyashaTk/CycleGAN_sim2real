import glob
import random

import cv2
import torch


class ReplayBuffer:
    """."""

    def __init__(self, max_size=50):
        """."""
        assert (
            max_size > 0
        ), "Empty buffer or trying to create a black hole. Be careful."
        self.max_size = max_size
        self.data = []

    def push_and_pop(self, data):
        """."""
        to_return = []
        for element in data.data:
            element = torch.unsqueeze(element, 0)
            if len(self.data) < self.max_size:
                self.data.append(element)
                to_return.append(element)
            else:
                if random.uniform(0, 1) > 0.5:
                    i = random.randint(0, self.max_size - 1)
                    to_return.append(self.data[i].clone())
                    self.data[i] = element
                else:
                    to_return.append(element)
        return torch.cat(to_return)


# custom weights initialization called on netG and netD
def weights_init(m):
    """."""
    classname = m.__class__.__name__
    if classname.find("Conv") != -1:
        torch.nn.init.normal_(m.weight, 0.0, 0.02)
    elif classname.find("BatchNorm") != -1:
        torch.nn.init.normal_(m.weight, 1.0, 0.02)
        torch.nn.init.zeros_(m.bias)


# changing directories
def order_dataset():
    """."""
    folders = glob.glob(
        "/media/vlad/20127138-1a35-451b-85c0-a84dbc12ae79/storage/gta5_2_real/cityscapes_images/val/*"
    )
    paths = []
    for folder in folders:
        paths += glob.glob(folder + "/*")

    print(len(paths))
    for path in paths:
        img = cv2.imread(path)
        cv2.imwrite(
            path.replace("frankfurt", "new")
            .replace("lindau", "new")
            .replace("munster", "new"),
            img,
        )
