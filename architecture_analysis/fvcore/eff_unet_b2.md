| module                                   | #parameters or shape    | #flops     |
|:-----------------------------------------|:------------------------|:-----------|
| model                                    | 23.768M                 | 0.611T     |
|  eff_net                                 |  10.124M                |  12.503G   |
|   eff_net._conv_stem                     |   0.864K                |   3.624G   |
|    eff_net._conv_stem.weight             |    (32, 1, 3, 3, 3)     |            |
|   eff_net._bn0                           |   64                    |   0.671G   |
|    eff_net._bn0.weight                   |    (32,)                |            |
|    eff_net._bn0.bias                     |    (32,)                |            |
|   eff_net._blocks                        |   8.216M                |   8.208G   |
|    eff_net._blocks.0                     |    2.024K               |    0.847G  |
|    eff_net._blocks.1                     |    0.9K                 |    0.445G  |
|    eff_net._blocks.2                     |    7.732K               |    1.417G  |
|    eff_net._blocks.3                     |    13.302K              |    0.81G   |
|    eff_net._blocks.4                     |    13.302K              |    0.81G   |
|    eff_net._blocks.5                     |    30.918K              |    0.486G  |
|    eff_net._blocks.6                     |    72.108K              |    0.547G  |
|    eff_net._blocks.7                     |    72.108K              |    0.547G  |
|    eff_net._blocks.8                     |    55.484K              |    0.161G  |
|    eff_net._blocks.9                     |    0.133M               |    0.116G  |
|    eff_net._blocks.10                    |    0.133M               |    0.116G  |
|    eff_net._blocks.11                    |    0.133M               |    0.116G  |
|    eff_net._blocks.12                    |    0.202M               |    0.186G  |
|    eff_net._blocks.13                    |    0.31M                |    0.277G  |
|    eff_net._blocks.14                    |    0.31M                |    0.277G  |
|    eff_net._blocks.15                    |    0.31M                |    0.277G  |
|    eff_net._blocks.16                    |    0.373M               |    0.124G  |
|    eff_net._blocks.17                    |    0.812M               |    88.412M |
|    eff_net._blocks.18                    |    0.812M               |    88.412M |
|    eff_net._blocks.19                    |    0.812M               |    88.412M |
|    eff_net._blocks.20                    |    0.812M               |    88.412M |
|    eff_net._blocks.21                    |    0.869M               |    95.852M |
|    eff_net._blocks.22                    |    1.927M               |    0.201G  |
|   eff_net._conv_head                     |   0.496M                |            |
|    eff_net._conv_head.weight             |    (1408, 352, 1, 1, 1) |            |
|   eff_net._bn1                           |   2.816K                |            |
|    eff_net._bn1.weight                   |    (1408,)              |            |
|    eff_net._bn1.bias                     |    (1408,)              |            |
|   eff_net._fc                            |   1.409M                |            |
|    eff_net._fc.weight                    |    (1000, 1408)         |            |
|    eff_net._fc.bias                      |    (1000,)              |            |
|  conv_blocks_localization                |  11.741M                |  0.582T    |
|   conv_blocks_localization.0             |   6.568M                |   6.727G   |
|    conv_blocks_localization.0.0.blocks.0 |    3.803M               |    3.894G  |
|    conv_blocks_localization.0.1.blocks.0 |    2.766M               |    2.833G  |
|   conv_blocks_localization.1             |   3.872M                |   31.73G   |
|    conv_blocks_localization.1.0.blocks.0 |    2.102M               |    17.224G |
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
|  tu                                      |  1.901M                 |  15.819G   |
|   tu.0                                   |   0.901M                |   0.115G   |
|    tu.0.weight                           |    (352, 320, 2, 2, 2)  |            |
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