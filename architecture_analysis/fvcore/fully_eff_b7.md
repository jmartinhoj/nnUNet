| module                                   | #parameters or shape    | #flops     |
|:-----------------------------------------|:------------------------|:-----------|
| model                                    | 83.044M                 | 0.695T     |
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
|  conv_blocks_localization                |  9.083M                 |  0.618T    |
|   conv_blocks_localization.0             |   5.411M                |   4.348G   |
|    conv_blocks_localization.0.0          |    3.813M               |    3.015G  |
|    conv_blocks_localization.0.1          |    1.598M               |    1.333G  |
|   conv_blocks_localization.1             |   2.63M                 |   17.318G  |
|    conv_blocks_localization.1.0          |    1.597M               |    10.399G |
|    conv_blocks_localization.1.1          |    1.033M               |    6.919G  |
|   conv_blocks_localization.2             |   0.719M                |   38.431G  |
|    conv_blocks_localization.2.0          |    0.448M               |    23.641G |
|    conv_blocks_localization.2.1          |    0.271M               |    14.789G |
|   conv_blocks_localization.3             |   0.212M                |   93.047G  |
|    conv_blocks_localization.3.0          |    0.138M               |    59.66G  |
|    conv_blocks_localization.3.1          |    73.872K              |    33.387G |
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
|  seg_outputs                             |  3.2K                   |  0.714G    |
|   seg_outputs.0                          |   1.28K                 |   1.311M   |
|    seg_outputs.0.weight                  |    (4, 320, 1, 1, 1)    |            |
|   seg_outputs.1                          |   1.024K                |   8.389M   |
|    seg_outputs.1.weight                  |    (4, 256, 1, 1, 1)    |            |
|   seg_outputs.2                          |   0.512K                |   33.554M  |
|    seg_outputs.2.weight                  |    (4, 128, 1, 1, 1)    |            |
|   seg_outputs.3                          |   0.256K                |   0.134G   |
|    seg_outputs.3.weight                  |    (4, 64, 1, 1, 1)     |            |
|   seg_outputs.4                          |   0.128K                |   0.537G   |
|    seg_outputs.4.weight                  |    (4, 32, 1, 1, 1)     |            |