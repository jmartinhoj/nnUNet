| module                                   | #parameters or shape    | #flops     |
|:-----------------------------------------|:------------------------|:-----------|
| model                                    | 86.96M                  | 0.797T     |
|  eff_net                                 |  71.32M                 |  59.897G   |
|   eff_net._conv_stem                     |   1.728K                |   7.248G   |
|    eff_net._conv_stem.weight             |    (64, 1, 3, 3, 3)     |            |
|   eff_net._bn0                           |   0.128K                |   1.342G   |
|    eff_net._bn0.weight                   |    (64,)                |            |
|    eff_net._bn0.bias                     |    (64,)                |            |
|   eff_net._blocks                        |   67.114M               |   51.307G  |
|    eff_net._blocks.0                     |    6.096K               |    2.231G  |
|    eff_net._blocks.1                     |    2.568K               |    1.158G  |
|    eff_net._blocks.2                     |    2.568K               |    1.158G  |
|    eff_net._blocks.3                     |    2.568K               |    1.158G  |
|    eff_net._blocks.4                     |    24.68K               |    4.747G  |
|    eff_net._blocks.5                     |    43.884K              |    2.526G  |
|    eff_net._blocks.6                     |    43.884K              |    2.526G  |
|    eff_net._blocks.7                     |    43.884K              |    2.526G  |
|    eff_net._blocks.8                     |    43.884K              |    2.526G  |
|    eff_net._blocks.9                     |    43.884K              |    2.526G  |
|    eff_net._blocks.10                    |    43.884K              |    2.526G  |
|    eff_net._blocks.11                    |    81.388K              |    1.499G  |
|    eff_net._blocks.12                    |    0.159M               |    1.163G  |
|    eff_net._blocks.13                    |    0.159M               |    1.163G  |
|    eff_net._blocks.14                    |    0.159M               |    1.163G  |
|    eff_net._blocks.15                    |    0.159M               |    1.163G  |
|    eff_net._blocks.16                    |    0.159M               |    1.163G  |
|    eff_net._blocks.17                    |    0.159M               |    1.163G  |
|    eff_net._blocks.18                    |    0.15M                |    0.429G  |
|    eff_net._blocks.19                    |    0.415M               |    0.352G  |
|    eff_net._blocks.20                    |    0.415M               |    0.352G  |
|    eff_net._blocks.21                    |    0.415M               |    0.352G  |
|    eff_net._blocks.22                    |    0.415M               |    0.352G  |
|    eff_net._blocks.23                    |    0.415M               |    0.352G  |
|    eff_net._blocks.24                    |    0.415M               |    0.352G  |
|    eff_net._blocks.25                    |    0.415M               |    0.352G  |
|    eff_net._blocks.26                    |    0.415M               |    0.352G  |
|    eff_net._blocks.27                    |    0.415M               |    0.352G  |
|    eff_net._blocks.28                    |    0.571M               |    0.511G  |
|    eff_net._blocks.29                    |    0.928M               |    0.804G  |
|    eff_net._blocks.30                    |    0.928M               |    0.804G  |
|    eff_net._blocks.31                    |    0.928M               |    0.804G  |
|    eff_net._blocks.32                    |    0.928M               |    0.804G  |
|    eff_net._blocks.33                    |    0.928M               |    0.804G  |
|    eff_net._blocks.34                    |    0.928M               |    0.804G  |
|    eff_net._blocks.35                    |    0.928M               |    0.804G  |
|    eff_net._blocks.36                    |    0.928M               |    0.804G  |
|    eff_net._blocks.37                    |    0.928M               |    0.804G  |
|    eff_net._blocks.38                    |    1.143M               |    0.404G  |
|    eff_net._blocks.39                    |    2.512M               |    0.267G  |
|    eff_net._blocks.40                    |    2.512M               |    0.267G  |
|    eff_net._blocks.41                    |    2.512M               |    0.267G  |
|    eff_net._blocks.42                    |    2.512M               |    0.267G  |
|    eff_net._blocks.43                    |    2.512M               |    0.267G  |
|    eff_net._blocks.44                    |    2.512M               |    0.267G  |
|    eff_net._blocks.45                    |    2.512M               |    0.267G  |
|    eff_net._blocks.46                    |    2.512M               |    0.267G  |
|    eff_net._blocks.47                    |    2.512M               |    0.267G  |
|    eff_net._blocks.48                    |    2.512M               |    0.267G  |
|    eff_net._blocks.49                    |    2.512M               |    0.267G  |
|    eff_net._blocks.50                    |    2.512M               |    0.267G  |
|    eff_net._blocks.51                    |    2.877M               |    0.314G  |
|    eff_net._blocks.52                    |    6.268M               |    0.65G   |
|    eff_net._blocks.53                    |    6.268M               |    0.65G   |
|    eff_net._blocks.54                    |    6.268M               |    0.65G   |
|   eff_net._conv_head                     |   1.638M                |            |
|    eff_net._conv_head.weight             |    (2560, 640, 1, 1, 1) |            |
|   eff_net._bn1                           |   5.12K                 |            |
|    eff_net._bn1.weight                   |    (2560,)              |            |
|    eff_net._bn1.bias                     |    (2560,)              |            |
|   eff_net._fc                            |   2.561M                |            |
|    eff_net._fc.weight                    |    (1000, 2560)         |            |
|    eff_net._fc.bias                      |    (1000,)              |            |
|  conv_blocks_localization                |  12.999M                |  0.721T    |
|   conv_blocks_localization.0             |   7.467M                |   7.647G   |
|    conv_blocks_localization.0.0.blocks.0 |    4.701M               |    4.815G  |
|    conv_blocks_localization.0.1.blocks.0 |    2.766M               |    2.833G  |
|   conv_blocks_localization.1             |   4.093M                |   33.542G  |
|    conv_blocks_localization.1.0.blocks.0 |    2.323M               |    19.036G |
|    conv_blocks_localization.1.1.blocks.0 |    1.77M                |    14.506G |
|   conv_blocks_localization.2             |   1.051M                |   68.938G  |
|    conv_blocks_localization.2.0.blocks.0 |    0.609M               |    39.905G |
|    conv_blocks_localization.2.1.blocks.0 |    0.443M               |    29.033G |
|   conv_blocks_localization.3             |   0.277M                |   0.145T   |
|    conv_blocks_localization.3.0.blocks.0 |    0.166M               |    87.141G |
|    conv_blocks_localization.3.1.blocks.0 |    0.111M               |    58.15G  |
|   conv_blocks_localization.4             |   0.111M                |   0.465T   |
|    conv_blocks_localization.4.0.blocks.0 |    83.04K               |    0.349T  |
|    conv_blocks_localization.4.1.blocks.0 |    27.744K              |    0.117T  |
|  tu                                      |  2.638M                 |  15.913G   |
|   tu.0                                   |   1.638M                |   0.21G    |
|    tu.0.weight                           |    (640, 320, 2, 2, 2)  |            |
|   tu.1                                   |   0.655M                |   0.671G   |
|    tu.1.weight                           |    (320, 256, 2, 2, 2)  |            |
|   tu.2                                   |   0.262M                |   2.147G   |
|    tu.2.weight                           |    (256, 128, 2, 2, 2)  |            |
|   tu.3                                   |   65.536K               |   4.295G   |
|    tu.3.weight                           |    (128, 64, 2, 2, 2)   |            |
|   tu.4                                   |   16.384K               |   8.59G    |
|    tu.4.weight                           |    (64, 32, 2, 2, 2)    |            |
|  seg_outputs                             |  2.4K                   |  0.536G    |
|   seg_outputs.0                          |   0.96K                 |   0.983M   |
|    seg_outputs.0.weight                  |    (3, 320, 1, 1, 1)    |            |
|   seg_outputs.1                          |   0.768K                |   6.291M   |
|    seg_outputs.1.weight                  |    (3, 256, 1, 1, 1)    |            |
|   seg_outputs.2                          |   0.384K                |   25.166M  |
|    seg_outputs.2.weight                  |    (3, 128, 1, 1, 1)    |            |
|   seg_outputs.3                          |   0.192K                |   0.101G   |
|    seg_outputs.3.weight                  |    (3, 64, 1, 1, 1)     |            |
|   seg_outputs.4                          |   96                    |   0.403G   |
|    seg_outputs.4.weight                  |    (3, 32, 1, 1, 1)     |            |