| module                                   | #parameters or shape    | #flops     |
|:-----------------------------------------|:------------------------|:-----------|
| model                                    | 19.408M                 | 0.608T     |
|  eff_net                                 |  5.969M                 |  9.658G    |
|   eff_net._conv_stem                     |   0.864K                |   3.624G   |
|    eff_net._conv_stem.weight             |    (32, 1, 3, 3, 3)     |            |
|   eff_net._bn0                           |   64                    |   0.671G   |
|    eff_net._bn0.weight                   |    (32,)                |            |
|    eff_net._bn0.bias                     |    (32,)                |            |
|   eff_net._blocks                        |   4.275M                |   5.363G   |
|    eff_net._blocks.0                     |    2.024K               |    0.847G  |
|    eff_net._blocks.1                     |    7.732K               |    1.417G  |
|    eff_net._blocks.2                     |    13.302K              |    0.81G   |
|    eff_net._blocks.3                     |    29.75K               |    0.476G  |
|    eff_net._blocks.4                     |    55.29K               |    0.424G  |
|    eff_net._blocks.5                     |    41.45K               |    0.116G  |
|    eff_net._blocks.6                     |    0.112M               |    97.277M |
|    eff_net._blocks.7                     |    0.112M               |    97.277M |
|    eff_net._blocks.8                     |    0.174M               |    0.161G  |
|    eff_net._blocks.9                     |    0.276M               |    0.248G  |
|    eff_net._blocks.10                    |    0.276M               |    0.248G  |
|    eff_net._blocks.11                    |    0.33M                |    0.108G  |
|    eff_net._blocks.12                    |    0.703M               |    76.874M |
|    eff_net._blocks.13                    |    0.703M               |    76.874M |
|    eff_net._blocks.14                    |    0.703M               |    76.874M |
|    eff_net._blocks.15                    |    0.738M               |    81.379M |
|   eff_net._conv_head                     |   0.41M                 |            |
|    eff_net._conv_head.weight             |    (1280, 320, 1, 1, 1) |            |
|   eff_net._bn1                           |   2.56K                 |            |
|    eff_net._bn1.weight                   |    (1280,)              |            |
|    eff_net._bn1.bias                     |    (1280,)              |            |
|   eff_net._fc                            |   1.281M                |            |
|    eff_net._fc.weight                    |    (1000, 1280)         |            |
|    eff_net._fc.bias                      |    (1000,)              |            |
|  conv_blocks_localization                |  11.617M                |  0.581T    |
|   conv_blocks_localization.0             |   6.499M                |   6.656G   |
|    conv_blocks_localization.0.0.blocks.0 |    3.733M               |    3.824G  |
|    conv_blocks_localization.0.1.blocks.0 |    2.766M               |    2.833G  |
|   conv_blocks_localization.1             |   3.817M                |   31.277G  |
|    conv_blocks_localization.1.0.blocks.0 |    2.047M               |    16.771G |
|    conv_blocks_localization.1.1.blocks.0 |    1.77M                |    14.506G |
|   conv_blocks_localization.2             |   0.968M                |   63.502G  |
|    conv_blocks_localization.2.0.blocks.0 |    0.526M               |    34.469G |
|    conv_blocks_localization.2.1.blocks.0 |    0.443M               |    29.033G |
|   conv_blocks_localization.3             |   0.249M                |   0.131T   |
|    conv_blocks_localization.3.0.blocks.0 |    0.138M               |    72.645G |
|    conv_blocks_localization.3.1.blocks.0 |    0.111M               |    58.15G  |
|   conv_blocks_localization.4             |   83.136K               |   0.349T   |
|    conv_blocks_localization.4.0.blocks.0 |    55.392K              |    0.233T  |
|    conv_blocks_localization.4.1.blocks.0 |    27.744K              |    0.117T  |
|  tu                                      |  1.819M                 |  15.808G   |
|   tu.0                                   |   0.819M                |   0.105G   |
|    tu.0.weight                           |    (320, 320, 2, 2, 2)  |            |
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