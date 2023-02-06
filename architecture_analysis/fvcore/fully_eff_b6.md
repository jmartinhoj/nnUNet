| module                                   | #parameters or shape    | #flops     |
|:-----------------------------------------|:------------------------|:-----------|
| model                                    | 57.874M                 | 0.647T     |
|  eff_net                                 |  46.697M                |  42.989G   |
|   eff_net._conv_stem                     |   1.512K                |   6.342G   |
|    eff_net._conv_stem.weight             |    (56, 1, 3, 3, 3)     |            |
|   eff_net._bn0                           |   0.112K                |   1.174G   |
|    eff_net._bn0.weight                   |    (56,)                |            |
|    eff_net._bn0.bias                     |    (56,)                |            |
|   eff_net._blocks                        |   43.058M               |   35.473G  |
|    eff_net._blocks.0                     |    5.118K               |    1.963G  |
|    eff_net._blocks.1                     |    2.568K               |    1.158G  |
|    eff_net._blocks.2                     |    2.568K               |    1.158G  |
|    eff_net._blocks.3                     |    23.128K              |    4.644G  |
|    eff_net._blocks.4                     |    31.77K               |    1.853G  |
|    eff_net._blocks.5                     |    31.77K               |    1.853G  |
|    eff_net._blocks.6                     |    31.77K               |    1.853G  |
|    eff_net._blocks.7                     |    31.77K               |    1.853G  |
|    eff_net._blocks.8                     |    31.77K               |    1.853G  |
|    eff_net._blocks.9                     |    63.034K              |    1.108G  |
|    eff_net._blocks.10                    |    0.134M               |    0.99G   |
|    eff_net._blocks.11                    |    0.134M               |    0.99G   |
|    eff_net._blocks.12                    |    0.134M               |    0.99G   |
|    eff_net._blocks.13                    |    0.134M               |    0.99G   |
|    eff_net._blocks.14                    |    0.134M               |    0.99G   |
|    eff_net._blocks.15                    |    0.123M               |    0.351G  |
|    eff_net._blocks.16                    |    0.339M               |    0.288G  |
|    eff_net._blocks.17                    |    0.339M               |    0.288G  |
|    eff_net._blocks.18                    |    0.339M               |    0.288G  |
|    eff_net._blocks.19                    |    0.339M               |    0.288G  |
|    eff_net._blocks.20                    |    0.339M               |    0.288G  |
|    eff_net._blocks.21                    |    0.339M               |    0.288G  |
|    eff_net._blocks.22                    |    0.339M               |    0.288G  |
|    eff_net._blocks.23                    |    0.472M               |    0.425G  |
|    eff_net._blocks.24                    |    0.756M               |    0.659G  |
|    eff_net._blocks.25                    |    0.756M               |    0.659G  |
|    eff_net._blocks.26                    |    0.756M               |    0.659G  |
|    eff_net._blocks.27                    |    0.756M               |    0.659G  |
|    eff_net._blocks.28                    |    0.756M               |    0.659G  |
|    eff_net._blocks.29                    |    0.756M               |    0.659G  |
|    eff_net._blocks.30                    |    0.756M               |    0.659G  |
|    eff_net._blocks.31                    |    0.93M                |    0.325G  |
|    eff_net._blocks.32                    |    2.044M               |    0.218G  |
|    eff_net._blocks.33                    |    2.044M               |    0.218G  |
|    eff_net._blocks.34                    |    2.044M               |    0.218G  |
|    eff_net._blocks.35                    |    2.044M               |    0.218G  |
|    eff_net._blocks.36                    |    2.044M               |    0.218G  |
|    eff_net._blocks.37                    |    2.044M               |    0.218G  |
|    eff_net._blocks.38                    |    2.044M               |    0.218G  |
|    eff_net._blocks.39                    |    2.044M               |    0.218G  |
|    eff_net._blocks.40                    |    2.044M               |    0.218G  |
|    eff_net._blocks.41                    |    2.044M               |    0.218G  |
|    eff_net._blocks.42                    |    2.321M               |    0.254G  |
|    eff_net._blocks.43                    |    5.089M               |    0.528G  |
|    eff_net._blocks.44                    |    5.089M               |    0.528G  |
|   eff_net._conv_head                     |   1.327M                |            |
|    eff_net._conv_head.weight             |    (2304, 576, 1, 1, 1) |            |
|   eff_net._bn1                           |   4.608K                |            |
|    eff_net._bn1.weight                   |    (2304,)              |            |
|    eff_net._bn1.bias                     |    (2304,)              |            |
|   eff_net._fc                            |   2.305M                |            |
|    eff_net._fc.weight                    |    (1000, 2304)         |            |
|    eff_net._fc.bias                      |    (1000,)              |            |
|  conv_blocks_localization                |  8.702M                 |  0.587T    |
|   conv_blocks_localization.0             |   5.131M                |   4.138G   |
|    conv_blocks_localization.0.0          |    3.533M               |    2.805G  |
|    conv_blocks_localization.0.1          |    1.598M               |    1.333G  |
|   conv_blocks_localization.1             |   2.568M                |   16.942G  |
|    conv_blocks_localization.1.0          |    1.536M               |    10.023G |
|    conv_blocks_localization.1.1          |    1.033M               |    6.919G  |
|   conv_blocks_localization.2             |   0.686M                |   36.829G  |
|    conv_blocks_localization.2.0          |    0.416M               |    22.04G  |
|    conv_blocks_localization.2.1          |    0.271M               |    14.789G |
|   conv_blocks_localization.3             |   0.212M                |   93.047G  |
|    conv_blocks_localization.3.0          |    0.138M               |    59.66G  |
|    conv_blocks_localization.3.1          |    73.872K              |    33.387G |
|   conv_blocks_localization.4             |   0.104M                |   0.436T   |
|    conv_blocks_localization.4.0.blocks.0 |    76.128K              |    0.32T   |
|    conv_blocks_localization.4.1.blocks.0 |    27.744K              |    0.117T  |
|  tu                                      |  2.474M                 |  15.892G   |
|   tu.0                                   |   1.475M                |   0.189G   |
|    tu.0.weight                           |    (576, 320, 2, 2, 2)  |            |
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