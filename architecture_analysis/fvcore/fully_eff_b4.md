| module                                   | #parameters or shape    | #flops     |
|:-----------------------------------------|:------------------------|:-----------|
| model                                    | 31.636M                 | 0.588T     |
|  eff_net                                 |  21.406M                |  23.469G   |
|   eff_net._conv_stem                     |   1.296K                |   5.436G   |
|    eff_net._conv_stem.weight             |    (48, 1, 3, 3, 3)     |            |
|   eff_net._bn0                           |   96                    |   1.007G   |
|    eff_net._bn0.weight                   |    (48,)                |            |
|    eff_net._bn0.bias                     |    (48,)                |            |
|   eff_net._blocks                        |   18.805M               |   17.027G  |
|    eff_net._blocks.0                     |    3.804K               |    1.472G  |
|    eff_net._blocks.1                     |    1.638K               |    0.768G  |
|    eff_net._blocks.2                     |    14.47K               |    2.804G  |
|    eff_net._blocks.3                     |    21.576K              |    1.281G  |
|    eff_net._blocks.4                     |    21.576K              |    1.281G  |
|    eff_net._blocks.5                     |    21.576K              |    1.281G  |
|    eff_net._blocks.6                     |    45.048K              |    0.76G   |
|    eff_net._blocks.7                     |    90.846K              |    0.682G  |
|    eff_net._blocks.8                     |    90.846K              |    0.682G  |
|    eff_net._blocks.9                     |    90.846K              |    0.682G  |
|    eff_net._blocks.10                    |    76.846K              |    0.218G  |
|    eff_net._blocks.11                    |    0.21M                |    0.18G   |
|    eff_net._blocks.12                    |    0.21M                |    0.18G   |
|    eff_net._blocks.13                    |    0.21M                |    0.18G   |
|    eff_net._blocks.14                    |    0.21M                |    0.18G   |
|    eff_net._blocks.15                    |    0.21M                |    0.18G   |
|    eff_net._blocks.16                    |    0.308M               |    0.281G  |
|    eff_net._blocks.17                    |    0.509M               |    0.448G  |
|    eff_net._blocks.18                    |    0.509M               |    0.448G  |
|    eff_net._blocks.19                    |    0.509M               |    0.448G  |
|    eff_net._blocks.20                    |    0.509M               |    0.448G  |
|    eff_net._blocks.21                    |    0.509M               |    0.448G  |
|    eff_net._blocks.22                    |    0.617M               |    0.212G  |
|    eff_net._blocks.23                    |    1.323M               |    0.142G  |
|    eff_net._blocks.24                    |    1.323M               |    0.142G  |
|    eff_net._blocks.25                    |    1.323M               |    0.142G  |
|    eff_net._blocks.26                    |    1.323M               |    0.142G  |
|    eff_net._blocks.27                    |    1.323M               |    0.142G  |
|    eff_net._blocks.28                    |    1.323M               |    0.142G  |
|    eff_net._blocks.29                    |    1.323M               |    0.142G  |
|    eff_net._blocks.30                    |    1.45M                |    0.159G  |
|    eff_net._blocks.31                    |    3.098M               |    0.323G  |
|   eff_net._conv_head                     |   0.803M                |            |
|    eff_net._conv_head.weight             |    (1792, 448, 1, 1, 1) |            |
|   eff_net._bn1                           |   3.584K                |            |
|    eff_net._bn1.weight                   |    (1792,)              |            |
|    eff_net._bn1.bias                     |    (1792,)              |            |
|   eff_net._fc                            |   1.793M                |            |
|    eff_net._fc.weight                    |    (1000, 1792)         |            |
|    eff_net._fc.bias                      |    (1000,)              |            |
|  conv_blocks_localization                |  8.081M                 |  0.548T    |
|   conv_blocks_localization.0             |   4.686M                |   3.805G   |
|    conv_blocks_localization.0.0          |    3.088M               |    2.471G  |
|    conv_blocks_localization.0.1          |    1.598M               |    1.333G  |
|   conv_blocks_localization.1             |   2.449M                |   16.208G  |
|    conv_blocks_localization.1.0          |    1.416M               |    9.289G  |
|    conv_blocks_localization.1.1          |    1.033M               |    6.919G  |
|   conv_blocks_localization.2             |   0.655M                |   35.279G  |
|    conv_blocks_localization.2.0          |    0.384M               |    20.489G |
|    conv_blocks_localization.2.1          |    0.271M               |    14.789G |
|   conv_blocks_localization.3             |   0.194M                |   85.874G  |
|    conv_blocks_localization.3.0          |    0.121M               |    52.488G |
|    conv_blocks_localization.3.1          |    73.872K              |    33.387G |
|   conv_blocks_localization.4             |   96.96K                |   0.407T   |
|    conv_blocks_localization.4.0.blocks.0 |    69.216K              |    0.291T  |
|    conv_blocks_localization.4.1.blocks.0 |    27.744K              |    0.117T  |
|  tu                                      |  2.146M                 |  15.85G    |
|   tu.0                                   |   1.147M                |   0.147G   |
|    tu.0.weight                           |    (448, 320, 2, 2, 2)  |            |
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