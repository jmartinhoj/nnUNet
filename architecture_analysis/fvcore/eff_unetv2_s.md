| module                                   | #parameters or shape   | #flops     |
|:-----------------------------------------|:-----------------------|:-----------|
| model                                    | 38.267M                | 0.678T     |
|  eff_netv2                               |  24.321M               |  94.991G   |
|   eff_netv2.features                     |   22.066M              |   94.991G  |
|    eff_netv2.features.0                  |    0.696K              |    3.221G  |
|    eff_netv2.features.1.conv             |    16.224K             |    8.582G  |
|    eff_netv2.features.2.conv             |    16.224K             |    8.582G  |
|    eff_netv2.features.3.conv             |    67.104K             |    4.426G  |
|    eff_netv2.features.4.conv             |    0.259M              |    16.99G  |
|    eff_netv2.features.5.conv             |    0.259M              |    16.99G  |
|    eff_netv2.features.6.conv             |    0.259M              |    16.99G  |
|    eff_netv2.features.7.conv             |    0.262M              |    2.15G   |
|    eff_netv2.features.8.conv             |    0.459M              |    3.771G  |
|    eff_netv2.features.9.conv             |    0.459M              |    3.771G  |
|    eff_netv2.features.10.conv            |    0.459M              |    3.771G  |
|    eff_netv2.features.11.conv            |    65.808K             |    0.187G  |
|    eff_netv2.features.12.conv            |    0.181M              |    0.154G  |
|    eff_netv2.features.13.conv            |    0.181M              |    0.154G  |
|    eff_netv2.features.14.conv            |    0.181M              |    0.154G  |
|    eff_netv2.features.15.conv            |    0.181M              |    0.154G  |
|    eff_netv2.features.16.conv            |    0.181M              |    0.154G  |
|    eff_netv2.features.17.conv            |    0.295M              |    0.257G  |
|    eff_netv2.features.18.conv            |    0.415M              |    0.352G  |
|    eff_netv2.features.19.conv            |    0.415M              |    0.352G  |
|    eff_netv2.features.20.conv            |    0.415M              |    0.352G  |
|    eff_netv2.features.21.conv            |    0.415M              |    0.352G  |
|    eff_netv2.features.22.conv            |    0.415M              |    0.352G  |
|    eff_netv2.features.23.conv            |    0.415M              |    0.352G  |
|    eff_netv2.features.24.conv            |    0.415M              |    0.352G  |
|    eff_netv2.features.25.conv            |    0.415M              |    0.352G  |
|    eff_netv2.features.26.conv            |    0.507M              |    0.198G  |
|    eff_netv2.features.27.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.28.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.29.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.30.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.31.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.32.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.33.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.34.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.35.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.36.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.37.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.38.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.39.conv            |    1.033M              |    0.108G  |
|    eff_netv2.features.40.conv            |    1.033M              |    0.108G  |
|   eff_netv2.conv                         |   0.462M               |            |
|    eff_netv2.conv.0                      |    0.459M              |            |
|    eff_netv2.conv.1                      |    3.584K              |            |
|   eff_netv2.classifier                   |   1.793M               |            |
|    eff_netv2.classifier.weight           |    (1000, 1792)        |            |
|    eff_netv2.classifier.bias             |    (1000,)             |            |
|  conv_blocks_localization                |  12.287M               |  0.567T    |
|   conv_blocks_localization.0             |   6.914M               |   7.081G   |
|    conv_blocks_localization.0.0.blocks.0 |    4.148M              |    4.248G  |
|    conv_blocks_localization.0.1.blocks.0 |    2.766M              |    2.833G  |
|   conv_blocks_localization.1             |   3.983M               |   32.636G  |
|    conv_blocks_localization.1.0.blocks.0 |    2.213M              |    18.13G  |
|    conv_blocks_localization.1.1.blocks.0 |    1.77M               |    14.506G |
|   conv_blocks_localization.2             |   1.051M               |   68.938G  |
|    conv_blocks_localization.2.0.blocks.0 |    0.609M              |    39.905G |
|    conv_blocks_localization.2.1.blocks.0 |    0.443M              |    29.033G |
|   conv_blocks_localization.3             |   0.263M               |   0.138T   |
|    conv_blocks_localization.3.0.blocks.0 |    0.152M              |    79.893G |
|    conv_blocks_localization.3.1.blocks.0 |    0.111M              |    58.15G  |
|   conv_blocks_localization.4             |   76.224K              |   0.32T    |
|    conv_blocks_localization.4.0.blocks.0 |    48.48K              |    0.204T  |
|    conv_blocks_localization.4.1.blocks.0 |    27.744K             |    0.117T  |
|  tu                                      |  1.655M                |  15.787G   |
|   tu.0                                   |   0.655M               |   83.886M  |
|    tu.0.weight                           |    (256, 320, 2, 2, 2) |            |
|   tu.1                                   |   0.655M               |   0.671G   |
|    tu.1.weight                           |    (320, 256, 2, 2, 2) |            |
|   tu.2                                   |   0.262M               |   2.147G   |
|    tu.2.weight                           |    (256, 128, 2, 2, 2) |            |
|   tu.3                                   |   65.536K              |   4.295G   |
|    tu.3.weight                           |    (128, 64, 2, 2, 2)  |            |
|   tu.4                                   |   16.384K              |   8.59G    |
|    tu.4.weight                           |    (64, 32, 2, 2, 2)   |            |
|  seg_outputs                             |  3.2K                  |  0.714G    |
|   seg_outputs.0                          |   1.28K                |   1.311M   |
|    seg_outputs.0.weight                  |    (4, 320, 1, 1, 1)   |            |
|   seg_outputs.1                          |   1.024K               |   8.389M   |
|    seg_outputs.1.weight                  |    (4, 256, 1, 1, 1)   |            |
|   seg_outputs.2                          |   0.512K               |   33.554M  |
|    seg_outputs.2.weight                  |    (4, 128, 1, 1, 1)   |            |
|   seg_outputs.3                          |   0.256K               |   0.134G   |
|    seg_outputs.3.weight                  |    (4, 64, 1, 1, 1)    |            |
|   seg_outputs.4                          |   0.128K               |   0.537G   |
|    seg_outputs.4.weight                  |    (4, 32, 1, 1, 1)    |            |