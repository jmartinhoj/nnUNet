| module                                   | #parameters or shape    | #flops     |
|:-----------------------------------------|:------------------------|:-----------|
| model                                    | 23.344M                 | 0.553T     |
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
|  conv_blocks_localization                |  7.763M                 |  0.519T    |
|   conv_blocks_localization.0             |   4.433M                |   3.614G   |
|    conv_blocks_localization.0.0          |    2.835M               |    2.281G  |
|    conv_blocks_localization.0.1          |    1.598M               |    1.333G  |
|   conv_blocks_localization.1             |   2.39M                 |   15.85G   |
|    conv_blocks_localization.1.0          |    1.358M               |    8.932G  |
|    conv_blocks_localization.1.1          |    1.033M               |    6.919G  |
|   conv_blocks_localization.2             |   0.655M                |   35.279G  |
|    conv_blocks_localization.2.0          |    0.384M               |    20.489G |
|    conv_blocks_localization.2.1          |    0.271M               |    14.789G |
|   conv_blocks_localization.3             |   0.194M                |   85.874G  |
|    conv_blocks_localization.3.0          |    0.121M               |    52.488G |
|    conv_blocks_localization.3.1          |    73.872K              |    33.387G |
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