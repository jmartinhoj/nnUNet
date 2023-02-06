from nnunet.network_architecture.generic_FulllyEffUNet import Generic_FullyEffUNet
from nnunet.training.network_training.nnUNetTrainerV2 import nnUNetTrainerV2
from torch import nn
from nnunet.network_architecture.efficient_Unet import Efficient_UNet
from nnunet.network_architecture.generic_UNet import Generic_UNet
from nnunet.network_architecture.fully_efficient_Unet import Fully_Efficient_UNet
from nnunet.network_architecture.efficient_Unet_v2 import Efficient_UNet_v2
from nnunet.network_architecture.fullyefficient_Unet_v2 import Fullyefficient_UNet_v2
from nnunet.network_architecture.initialization import InitWeights_He
import torch
from nnunet.utilities.nd_softmax import softmax_helper
from fvcore.nn import FlopCountAnalysis, flop_count_table
from nnunet.network_architecture.custom_modules.effnetv2_3d import effnetv2_l3d, effnetv2_m3d
import numpy as np


class nnUNetTrainer_efficient_inftime(nnUNetTrainerV2):

    def __init__(self, plans_file, fold, output_folder=None, dataset_directory=None, batch_dice=True, stage=None,
                 unpack_data=True, deterministic=True, fp16=False):
        super().__init__(plans_file, fold, output_folder, dataset_directory, batch_dice, stage,
                 unpack_data, deterministic, fp16)

        self.max_num_epochs = 1500
    
    def initialize_network(self, training=True):
        """
        - momentum 0.99
        - SGD instead of Adam
        - self.lr_scheduler = None because we do poly_lr
        - deep supervision = True
        - i am sure I forgot something here

        Known issue: forgot to set neg_slope=0 in InitWeights_He; should not make a difference though
        :return:
        """
        if self.threeD:
            conv_op = nn.Conv3d
            dropout_op = nn.Dropout3d
            norm_op = nn.InstanceNorm3d

        else:
            conv_op = nn.Conv2d
            dropout_op = nn.Dropout2d
            norm_op = nn.InstanceNorm2d

        norm_op_kwargs = {'eps': 1e-5, 'affine': True}
        dropout_op_kwargs = {'p': 0, 'inplace': True}
        net_nonlin = nn.LeakyReLU
        net_nonlin_kwargs = {'negative_slope': 1e-2, 'inplace': True}
        print("vamos lá ver")
        net_num_pool_op_kernel_sizes = [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]]
        net_conv_kernel_sizes = [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]
        # self.network = Generic_UNet(1, 32, 3,
        #                     len(net_num_pool_op_kernel_sizes),
        #                     2, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
        #                     dropout_op_kwargs,
        #                     net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
        #                     net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True)
        
        self.num_input_channels = 1
        self.base_num_features = 32
        self.num_classes: 3
        self.net_num_pool_op_kernel_sizes = [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.conv_per_stage= 2
        self.net_conv_kernel_sizes = [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]]
        networks = []


        networks.append(Generic_UNet(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True))

        networks.append(Generic_FullyEffUNet(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True))

        networks.append(Efficient_UNet_v2(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True))
        networks.append(Efficient_UNet_v2(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True, eff_netv2=effnetv2_m3d()))

        networks.append(Efficient_UNet_v2(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True, eff_netv2=effnetv2_l3d()))

        networks.append(Efficient_UNet(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True))


        networks.append(Fully_Efficient_UNet(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True))


        networks.append(Fully_Efficient_UNet(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True, efficient_model="efficientnet-b4"))


        networks.append(Fully_Efficient_UNet(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True, efficient_model="efficientnet-b7"))



        networks.append(Fullyefficient_UNet_v2(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True))

        networks.append(Fullyefficient_UNet_v2(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True, eff_netv2=effnetv2_l3d()))
      



        # self.network = Efficient_UNet_v2(1, 32, 3,
        #                     len(net_num_pool_op_kernel_sizes),
        #                     2, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
        #                     dropout_op_kwargs,
        #                     net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
        #                     net_num_pool_op_kernel_sizes, net_conv_kernel_sizes, False, True, True, eff_netv2=effnetv2_l3d())

        # 

        # self.network = Efficient_UNet(self.num_input_channels, self.base_num_features, self.num_classes,
        #                             len(self.net_num_pool_op_kernel_sizes),
        #                             self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
        #                             dropout_op_kwargs,
        #                             net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
        #                             self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True, efficient_model="efficientnet-b7")


        # self.network = Fullyefficient_UNet_v2(self.num_input_channels, self.base_num_features, self.num_classes,
        #                     len(self.net_num_pool_op_kernel_sizes),
        #                     self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
        #                     dropout_op_kwargs,
        #                     net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
        #                     self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True, eff_netv2=effnetv2_l3d())
        

        # macs, params = get_model_complexity_info(self.network, (1, 128, 128, 128), as_strings=True,print_per_layer_stat=True, verbose=True)

        # print('{:<30}  {:<8}'.format('Computational complexity: ', macs))
        # print('{:<30}  {:<8}'.format('Number of parameters: ', params))
        
        for i in networks:
            print(type(i).__name__)
            self.network = i
        
            if torch.cuda.is_available():
                self.network.cuda()


        
            self.network.inference_apply_nonlin = softmax_helper
            self.network.eval()
            self.network.training = False
            starter, ender = torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True)
            repetitions = 500
            timings=np.zeros((repetitions,1))

            inputs = torch.randn((1,1,128,128,128)).cuda()
            
            for _ in range(10):
                _ = self.network(inputs)

            with torch.no_grad():
                for rep in range(repetitions):
                    starter.record()
                    # print("first")
                    _ = self.network(inputs)
                    # _ = self.network.predict3D(inputs, False, None, use_sliding_window=False)
                    ender.record()
                    # WAIT FOR GPU SYNC
                    torch.cuda.synchronize()
                    curr_time = starter.elapsed_time(ender)
                    # print(curr_time)
                    timings[rep] = curr_time
                mean_syn = np.sum(timings) / repetitions
                std_syn = np.std(timings)
                print(mean_syn)
                # flops = FlopCountAnalysis(self.network, inputs)
                # print(flop_count_table(flops))
        print("finish")

        quit()