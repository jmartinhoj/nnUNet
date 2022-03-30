Variables from nnUNetTrainer
```python
num_input_channels = plans['num_modalities']
base_num_features =  plans['base_num_features']
num_classes = plans['num_classes'] + 1  #(background is no longer in num_classes)
net_num_pool_op_kernel_sizes = plans['plans_per_stage'][stage]['pool_op_kernel_sizes']
conv_per_stage = plans['conv_per_stage']
net_conv_kernel_sizes = plans['plans_per_stage'][stage]['conv_kernel_sizes']
```

For Kits2021:
```python
Generic_UNet(self.num_input_channels, self.base_num_features, self.num_classes,
                                    len(self.net_num_pool_op_kernel_sizes),
                                    self.conv_per_stage, 2, conv_op, norm_op, norm_op_kwargs, dropout_op,
                                    dropout_op_kwargs,
                                    net_nonlin, net_nonlin_kwargs, True, False, lambda x: x, InitWeights_He(1e-2),
                                    self.net_num_pool_op_kernel_sizes, self.net_conv_kernel_sizes, False, True, True)
```
is equivalent to:
```python
Generic_UNet(1, 32, 4, 5, 2, 2, nn.Conv3d, nn.InstanceNorm3d, {'eps': 1e-5, 'affine': True}, nn.Dropout3d, {'p': 0, 'inplace': True}, nn.LeakyReLU, {'negative_slope': 1e-2, 'inplace': True}, True, False, lambda x: x, InitWeights_He(1e-2), [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]], [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]], False, True, True)
```