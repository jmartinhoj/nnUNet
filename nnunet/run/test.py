



from nnunet.network_architecture.efficient_Unet import Efficient_UNet
from nnunet.network_architecture.initialization import InitWeights_He
from torch import nn


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


print(Efficient_UNet(num_input_channels, base_num_features, num_classes,
                        len(net_num_pool_op_kernel_sizes),
                        conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                        dropout_op_kwargs,
                        net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                        net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True, efficient_model="efficientnet-b0"))