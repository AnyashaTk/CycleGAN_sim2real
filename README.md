# CycleGAN-PyTorch sim3real task

<img src="https://github.com/AnyashaTk/-CycleGAN_sim2real/blob/main/assets/example_in.png" width="400" /> <img src="https://github.com/AnyashaTk/-CycleGAN_sim2real/blob/main/assets/example_out.png" width="400" />

### Installation

#### Clone and install requirements

```bash
$ git clone https://github.com/AnyashaTk/CycleGAN_sim2real_task.git
$ cd  CycleGAN_sim2real_task/
$ pip3 install -r requirements.txt
```

#### Download dataset

```bash
# example: perfect
$ python3 get_dataset.py
```

### Test

The following commands can be used to test the whole test.

```bash
# Example: perfect
$ python3 test.py --dataset perfect --cuda
```

For single image processing, use the following command.

```bash
$ python3 test_image.py --file test_photo.png --model-name weights/perfect/netG_A2B.pth --cuda
```

### Train

```text
usage: train.py [-h] [--dataroot DATAROOT] [--dataset DATASET] [--epochs N]
                [--decay_epochs DECAY_EPOCHS] [-b N] [--lr LR] [-p N] [--cuda]
                [--netG_A2B NETG_A2B] [--netG_B2A NETG_B2A] [--netD_A NETD_A]
                [--netD_B NETD_B] [--image-size IMAGE_SIZE] [--outf OUTF]
                [--manualSeed MANUALSEED]


optional arguments:
  -h, --help            show this help message and exit
  --dataroot DATAROOT   path to datasets. (default:./data)
  --dataset DATASET     dataset name. (default:`horse2zebra`)Option:
                        [apple2orange, summer2winter_yosemite, horse2zebra,
                        monet2photo, cezanne2photo, ukiyoe2photo,
                        vangogh2photo, maps, facades, selfie2anime,
                        iphone2dslr_flower, ae_photos, ]
  --epochs N            number of total epochs to run
  --decay_epochs DECAY_EPOCHS
                        epoch to start linearly decaying the learning rate to
                        0. (default:100)
  -b N, --batch-size N  mini-batch size (default: 1), this is the total batch
                        size of all GPUs on the current node when using Data
                        Parallel or Distributed Data Parallel
  --lr LR               learning rate. (default:0.0002)
  -p N, --print-freq N  print frequency. (default:100)
  --cuda                Enables cuda
  --netG_A2B NETG_A2B   path to netG_A2B (to continue training)
  --netG_B2A NETG_B2A   path to netG_B2A (to continue training)
  --netD_A NETD_A       path to netD_A (to continue training)
  --netD_B NETD_B       path to netD_B (to continue training)
  --image-size IMAGE_SIZE
                        size of the data crop (squared assumed). (default:256)
  --outf OUTF           folder to output images. (default:`./outputs`).
  --manualSeed MANUALSEED
                        Seed for initializing training. (default:none)

```

#### Example


```bash
# Example: perfect
$ python3 train.py --dataset perfect --cuda
```

#### Results
Train losses:

![https://myoctocat.com/assets/images/base-octocat.svg](https://github.com/AnyashaTk/-CycleGAN_sim2real/blob/main/assets/errD_B_train.svg)

Inference result:

<img src="https://github.com/AnyashaTk/-CycleGAN_sim2real/blob/main/assets/example_in.png" width="400" /> <img src="https://github.com/AnyashaTk/-CycleGAN_sim2real/blob/main/assets/example_out.png" width="400" />
