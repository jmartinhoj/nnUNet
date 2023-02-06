| module                                   | #parameters or shape    | #flops     |
|:-----------------------------------------|:------------------------|:-----------|
| model                                    | 27.509M                 | 0.655T     |
|  eff_net                                 |  13.595M                |  17.916G   |
|   eff_net._conv_stem                     |   1.08K                 |   4.53G    |
|    eff_net._conv_stem.weight             |    (40, 1, 3, 3, 3)     |            |
|   eff_net._bn0                           |   80                    |   0.839G   |
|    eff_net._bn0.weight                   |    (40,)                |            |
|    eff_net._bn0.bias                     |    (40,)                |            |
|   eff_net._blocks                        |   11.464M               |   12.547G  |
|    eff_net._blocks.0                     |    3.018K               |    1.237G  |
|    eff_net._blocks.1                     |    1.638K               |    0.768G  |
|    eff_net._blocks.2                     |    14.47K               |    2.804G  |
|    eff_net._blocks.3                     |    21.576K              |    1.281G  |
|    eff_net._blocks.4                     |    21.576K              |    1.281G  |
|    eff_net._blocks.5                     |    43.496K              |    0.748G  |
|    eff_net._blocks.6                     |    72.108K              |    0.547G  |
|    eff_net._blocks.7                     |    72.108K              |    0.547G  |
|    eff_net._blocks.8                     |    57.804K              |    0.163G  |
|    eff_net._blocks.9                     |    0.157M               |    0.136G  |
|    eff_net._blocks.10                    |    0.157M               |    0.136G  |
|    eff_net._blocks.11                    |    0.157M               |    0.136G  |
|    eff_net._blocks.12                    |    0.157M               |    0.136G  |
|    eff_net._blocks.13                    |    0.236M               |    0.217G  |
|    eff_net._blocks.14                    |    0.384M               |    0.341G  |
|    eff_net._blocks.15                    |    0.384M               |    0.341G  |
|    eff_net._blocks.16                    |    0.384M               |    0.341G  |
|    eff_net._blocks.17                    |    0.384M               |    0.341G  |
|    eff_net._blocks.18                    |    0.462M               |    0.156G  |
|    eff_net._blocks.19                    |    0.989M               |    0.107G  |
|    eff_net._blocks.20                    |    0.989M               |    0.107G  |
|    eff_net._blocks.21                    |    0.989M               |    0.107G  |
|    eff_net._blocks.22                    |    0.989M               |    0.107G  |
|    eff_net._blocks.23                    |    0.989M               |    0.107G  |
|    eff_net._blocks.24                    |    1.064M               |    0.117G  |
|    eff_net._blocks.25                    |    2.286M               |    0.239G  |
|   eff_net._conv_head                     |   0.59M                 |            |
|    eff_net._conv_head.weight             |    (1536, 384, 1, 1, 1) |            |
|   eff_net._bn1                           |   3.072K                |            |
|    eff_net._bn1.weight                   |    (1536,)              |            |
|    eff_net._bn1.bias                     |    (1536,)              |            |
|   eff_net._fc                            |   1.537M                |            |
|    eff_net._fc.weight                    |    (1000, 1536)         |            |
|    eff_net._fc.bias                      |    (1000,)              |            |
|  conv_blocks_localization                |  11.928M                |  0.62T     |
|   conv_blocks_localization.0             |   6.707M                |   6.869G   |
|    conv_blocks_localization.0.0.blocks.0 |    3.941M               |    4.036G  |
|    conv_blocks_localization.0.1.blocks.0 |    2.766M               |    2.833G  |
|   conv_blocks_localization.1             |   3.872M                |   31.73G   |
|    conv_blocks_localization.1.0.blocks.0 |    2.102M               |    17.224G |
|    conv_blocks_localization.1.1.blocks.0 |    1.77M                |    14.506G |
|   conv_blocks_localization.2             |   0.996M                |   65.314G  |
|    conv_blocks_localization.2.0.blocks.0 |    0.553M               |    36.281G |
|    conv_blocks_localization.2.1.blocks.0 |    0.443M               |    29.033G |
|   conv_blocks_localization.3             |   0.263M                |   0.138T   |
|    conv_blocks_localization.3.0.blocks.0 |    0.152M               |    79.893G |
|    conv_blocks_localization.3.1.blocks.0 |    0.111M               |    58.15G  |
|   conv_blocks_localization.4             |   90.048K               |   0.378T   |
|    conv_blocks_localization.4.0.blocks.0 |    62.304K              |    0.262T  |
|    conv_blocks_localization.4.1.blocks.0 |    27.744K              |    0.117T  |
|  tu                                      |  1.982M                 |  15.829G   |
|   tu.0                                   |   0.983M                |   0.126G   |
|    tu.0.weight                           |    (384, 320, 2, 2, 2)  |            |
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