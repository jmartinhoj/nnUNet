from nnunet.network_architecture.custom_modules.effnetv2_3d import effnetv2_m3d
from nnunet.network_architecture.generic_UNet import Generic_UNet
from fvcore.nn import FlopCountAnalysis, flop_count_table
from nnunet.network_architecture.fully_efficient_Unet import Fully_Efficient_UNet
from nnunet.network_architecture.fullyefficient_Unet_v2 import Fullyefficient_UNet_v2
from torch import nn
from nnunet.network_architecture.initialization import InitWeights_He
import torch
import torch.nn.functional as F


softmax_helper = lambda x: F.softmax(x, 1)



conv_op = nn.Conv3d
dropout_op = nn.Dropout3d
norm_op = nn.InstanceNorm3d

norm_op_kwargs = {'eps': 1e-5, 'affine': True}
dropout_op_kwargs = {'p': 0, 'inplace': True}
net_nonlin = nn.LeakyReLU
net_nonlin_kwargs = {'negative_slope': 1e-2, 'inplace': True}

num_input_channels = 1
base_num_features = 32
num_classes = 3
net_num_pool_op_kernel_sizes = [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]]
conv_per_stage= 2
net_conv_kernel_sizes = [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]


effnets = [effnetv2_m3d()]

inputs = torch.randn(2, 1,128,128,128)

for eff in effnets:
    # network = Fully_Efficient_UNet(num_input_channels, base_num_features, num_classes,
    #                     len(net_num_pool_op_kernel_sizes),
    #                     conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
    #                     dropout_op_kwargs,
    #                     net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
    #                     net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True, efficient_model=eff)

    network = Fullyefficient_UNet_v2(num_input_channels, base_num_features, num_classes,
                        len(net_num_pool_op_kernel_sizes),
                        conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                        dropout_op_kwargs,
                        net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                        net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True, eff_netv2=eff)

    # if torch.cuda.is_available():
    #     network.cuda()
    network.inference_apply_nonlin = softmax_helper
    flops = FlopCountAnalysis(network, inputs)
    with open("fullyeff_v2_m.md", "w") as f:
        f.write(flop_count_table(flops)) 
        f.close()
    print(eff + " completed!")



print("done")