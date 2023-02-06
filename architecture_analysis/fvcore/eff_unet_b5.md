| module                                   | #parameters or shape    | #flops     |
|:-----------------------------------------|:------------------------|:-----------|
| model                                    | 47.829M                 | 0.701T     |
|  eff_net                                 |  33.097M                |  32.024G   |
|   eff_net._conv_stem                     |   1.296K                |   5.436G   |
|    eff_net._conv_stem.weight             |    (48, 1, 3, 3, 3)     |            |
|   eff_net._bn0                           |   96                    |   1.007G   |
|    eff_net._bn0.weight                   |    (48,)                |            |
|    eff_net._bn0.bias                     |    (48,)                |            |
|   eff_net._blocks                        |   29.994M               |   25.581G  |
|    eff_net._blocks.0                     |    3.804K               |    1.472G  |
|    eff_net._blocks.1                     |    1.638K               |    0.768G  |
|    eff_net._blocks.2                     |    1.638K               |    0.768G  |
|    eff_net._blocks.3                     |    15.638K              |    2.882G  |
|    eff_net._blocks.4                     |    31.77K               |    1.853G  |
|    eff_net._blocks.5                     |    31.77K               |    1.853G  |
|    eff_net._blocks.6                     |    31.77K               |    1.853G  |
|    eff_net._blocks.7                     |    31.77K               |    1.853G  |
|    eff_net._blocks.8                     |    61.098K              |    1.092G  |
|    eff_net._blocks.9                     |    0.112M               |    0.83G   |
|    eff_net._blocks.10                    |    0.112M               |    0.83G   |
|    eff_net._blocks.11                    |    0.112M               |    0.83G   |
|    eff_net._blocks.12                    |    0.112M               |    0.83G   |
|    eff_net._blocks.13                    |    98.576K              |    0.281G  |
|    eff_net._blocks.14                    |    0.271M               |    0.231G  |
|    eff_net._blocks.15                    |    0.271M               |    0.231G  |
|    eff_net._blocks.16                    |    0.271M               |    0.231G  |
|    eff_net._blocks.17                    |    0.271M               |    0.231G  |
|    eff_net._blocks.18                    |    0.271M               |    0.231G  |
|    eff_net._blocks.19                    |    0.271M               |    0.231G  |
|    eff_net._blocks.20                    |    0.383M               |    0.346G  |
|    eff_net._blocks.21                    |    0.602M               |    0.528G  |
|    eff_net._blocks.22                    |    0.602M               |    0.528G  |
|    eff_net._blocks.23                    |    0.602M               |    0.528G  |
|    eff_net._blocks.24                    |    0.602M               |    0.528G  |
|    eff_net._blocks.25                    |    0.602M               |    0.528G  |
|    eff_net._blocks.26                    |    0.602M               |    0.528G  |
|    eff_net._blocks.27                    |    0.738M               |    0.255G  |
|    eff_net._blocks.28                    |    1.624M               |    0.174G  |
|    eff_net._blocks.29                    |    1.624M               |    0.174G  |
|    eff_net._blocks.30                    |    1.624M               |    0.174G  |
|    eff_net._blocks.31                    |    1.624M               |    0.174G  |
|    eff_net._blocks.32                    |    1.624M               |    0.174G  |
|    eff_net._blocks.33                    |    1.624M               |    0.174G  |
|    eff_net._blocks.34                    |    1.624M               |    0.174G  |
|    eff_net._blocks.35                    |    1.624M               |    0.174G  |
|    eff_net._blocks.36                    |    1.825M               |    0.2G    |
|    eff_net._blocks.37                    |    4.032M               |    0.419G  |
|    eff_net._blocks.38                    |    4.032M               |    0.419G  |
|   eff_net._conv_head                     |   1.049M                |            |
|    eff_net._conv_head.weight             |    (2048, 512, 1, 1, 1) |            |
|   eff_net._bn1                           |   4.096K                |            |
|    eff_net._bn1.weight                   |    (2048,)              |            |
|    eff_net._bn1.bias                     |    (2048,)              |            |
|   eff_net._fc                            |   2.049M                |            |
|    eff_net._fc.weight                    |    (1000, 2048)         |            |
|    eff_net._fc.bias                      |    (1000,)              |            |
|  conv_blocks_localization                |  12.419M                |  0.652T    |
|   conv_blocks_localization.0             |   7.052M                |   7.223G   |
|    conv_blocks_localization.0.0.blocks.0 |    4.286M               |    4.39G   |
|    conv_blocks_localization.0.1.blocks.0 |    2.766M               |    2.833G  |
|   conv_blocks_localization.1             |   3.983M                |   32.636G  |
|    conv_blocks_localization.1.0.blocks.0 |    2.213M               |    18.13G  |
|    conv_blocks_localization.1.1.blocks.0 |    1.77M                |    14.506G |
|   conv_blocks_localization.2             |   1.024M                |   67.126G  |
|    conv_blocks_localization.2.0.blocks.0 |    0.581M               |    38.093G |
|    conv_blocks_localization.2.1.blocks.0 |    0.443M               |    29.033G |
|   conv_blocks_localization.3             |   0.263M                |   0.138T   |
|    conv_blocks_localization.3.0.blocks.0 |    0.152M               |    79.893G |
|    conv_blocks_localization.3.1.blocks.0 |    0.111M               |    58.15G  |
|   conv_blocks_localization.4             |   96.96K                |   0.407T   |
|    conv_blocks_localization.4.0.blocks.0 |    69.216K              |    0.291T  |
|    conv_blocks_localization.4.1.blocks.0 |    27.744K              |    0.117T  |
|  tu                                      |  2.31M                  |  15.871G   |
|   tu.0                                   |   1.311M                |   0.168G   |
|    tu.0.weight                           |    (512, 320, 2, 2, 2)  |            |
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