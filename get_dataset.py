import yadisk
import zipfile

# My token: fa54cb9253d9442ab52773987b7b4d79 or AQAAAAA3RRciAADLWxPBjTfUF0XImh04cN9dP4E
# Your token:
# Get there: https://ramziv.com/article/8

y = yadisk.YaDisk(
    id="fa54cb9253d9442ab52773987b7b4d79",
    secret="872a037c7d1a4c83b30f71442b18a40f",
    token="AQAAAAA3RRciAADLWxPBjTfUF0XImh04cN9dP4E",
)
# or
# y = yadisk.YaDisk("<id-app>", "<secret-app>", "<token>")

# Checks if the token is valid
y.check_token()

y.download(
    src_path="/gan-research/perfect.zip",
    path_or_file="/home/ubuntu/CycleGAN-PyTorch/perfect.zip",
)

with zipfile.ZipFile("/home/ubuntu/CycleGAN-PyTorch/perfect.zip", "r") as zip_ref:
    zip_ref.extractall("/home/ubuntu/CycleGAN-PyTorch/data/")
