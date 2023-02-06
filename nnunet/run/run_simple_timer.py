from nnunet.network_architecture.custom_modules.effnetv2_3d import effnetv2_l3d, effnetv2_m3d, effnetv2_s3d
from nnunet.network_architecture.efficient_Unet import Efficient_UNet
from nnunet.network_architecture.efficient_Unet_v2 import Efficient_UNet_v2
from nnunet.network_architecture.generic_FulllyEffUNet import Generic_FullyEffUNet
from nnunet.network_architecture.generic_UNet import Generic_UNet
from nnunet.network_architecture.fully_efficient_Unet import Fully_Efficient_UNet
from nnunet.network_architecture.fullyefficient_Unet_v2 import Fullyefficient_UNet_v2
from torch import nn
from nnunet.network_architecture.initialization import InitWeights_He
import torch
import torch.nn.functional as F
import numpy as np
from tqdm import tqdm
import time

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


effnets = ["efficientnet-b0", "efficientnet-b1", "efficientnet-b2", "efficientnet-b3", "efficientnet-b4", "efficientnet-b5", "efficientnet-b6", "efficientnet-b7"]
effnetsv2 = [effnetv2_s3d, effnetv2_m3d, effnetv2_l3d]

inputs = torch.randn(2, 1,128,128,128)

networks = []

networks.append(Generic_UNet(num_input_channels, base_num_features, num_classes,
                            len(net_num_pool_op_kernel_sizes),
                            conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                            dropout_op_kwargs,
                            net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                            net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True))

networks.append(Generic_FullyEffUNet(num_input_channels, base_num_features, num_classes,
                            len(net_num_pool_op_kernel_sizes),
                            conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                            dropout_op_kwargs,
                            net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                            net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True))

for eff in effnets:

    networks.append(Efficient_UNet(num_input_channels, base_num_features, num_classes,
                                    len(net_num_pool_op_kernel_sizes),
                                    conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True, efficient_model=eff))
    
    networks.append(Fully_Efficient_UNet(num_input_channels, base_num_features, num_classes,
                                    len(net_num_pool_op_kernel_sizes),
                                    conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True, efficient_model=eff))

for effv2 in effnetsv2:

    networks.append(Efficient_UNet_v2(num_input_channels, base_num_features, num_classes,
                        len(net_num_pool_op_kernel_sizes),
                        conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                        dropout_op_kwargs,
                        net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                        net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True, eff_netv2=effv2()))

    networks.append(Fullyefficient_UNet_v2(num_input_channels, base_num_features, num_classes,
                        len(net_num_pool_op_kernel_sizes),
                        conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                        dropout_op_kwargs,
                        net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                        net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True, eff_netv2=effv2()))


repetitions = 500

for network in tqdm(networks):
    with open("times.txt", "a") as f:
        f.write(network.__repr__())
        f.write("\n")
        f.close()

    # if torch.cuda.is_available():
    #     self.network.cuda()



    network.inference_apply_nonlin = softmax_helper
    network.eval()
    network.training = False
    # starter, ender = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)
    timings=np.zeros((repetitions,1))
    for _ in range(10):
        _ = network(inputs)

    with torch.no_grad():
        for rep in range(repetitions):
            # starter.record()
            start = time.perf_counter()
            _ = network(inputs)
            # ender.record()
            # WAIT FOR GPU SYNC
            # torch.cuda.synchronize()

            # curr_time = starter.elapsed_time(ender)
            # print(curr_time)
            timings[rep] = time.perf_counter()-start
        mean_syn = np.sum(timings) / repetitions
        std_syn = np.std(timings)
        with open("times.txt", "a") as f:
            f.write(str(mean_syn) + "\n")
            f.close()
        # flops = FlopCountAnalysis(self.network, inputs)
        # print(flop_count_table(flops))
print("finish")










# if torch.cuda.is_available():
#     network.cuda()
# network.inference_apply_nonlin = softmax_helper
# flops = FlopCountAnalysis(network, inputs)
# with open("fullyeff_v2_m.md", "w") as f:
#     f.write(flop_count_table(flops)) 
#     f.close()
# print(eff + " completed!")


# print("done")