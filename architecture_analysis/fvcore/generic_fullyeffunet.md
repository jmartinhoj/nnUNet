| module                                   | #parameters or shape   | #flops     |
|:-----------------------------------------|:-----------------------|:-----------|
| model                                    | 28.246M                | 0.861T     |
|  conv_blocks_localization                |  12.399M               |  0.565T    |
|   conv_blocks_localization.0             |   6.637M               |   5.258G   |
|    conv_blocks_localization.0.0          |    5.039M              |    3.924G  |
|    conv_blocks_localization.0.1          |    1.598M              |    1.333G  |
|   conv_blocks_localization.1             |   4.277M               |   27.189G  |
|    conv_blocks_localization.1.0          |    3.245M              |    20.271G |
|    conv_blocks_localization.1.1          |    1.033M              |    6.919G  |
|   conv_blocks_localization.2             |   1.107M               |   57.211G  |
|    conv_blocks_localization.2.0          |    0.836M              |    42.422G |
|    conv_blocks_localization.2.1          |    0.271M              |    14.789G |
|   conv_blocks_localization.3             |   0.295M               |   0.126T   |
|    conv_blocks_localization.3.0          |    0.221M              |    92.375G |
|    conv_blocks_localization.3.1          |    73.872K             |    33.387G |
|   conv_blocks_localization.4             |   83.136K              |   0.349T   |
|    conv_blocks_localization.4.0.blocks.0 |    55.392K             |    0.233T  |
|    conv_blocks_localization.4.1.blocks.0 |    27.744K             |    0.117T  |
|  conv_blocks_context                     |  14.025M               |  0.279T    |
|   conv_blocks_context.0.blocks           |   28.704K              |   0.121T   |
|    conv_blocks_context.0.blocks.0        |    0.96K               |    4.295G  |
|    conv_blocks_context.0.blocks.1        |    27.744K             |    0.117T  |
|   conv_blocks_context.1.blocks           |   0.166M               |   87.309G  |
|    conv_blocks_context.1.blocks.0        |    55.488K             |    29.159G |
|    conv_blocks_context.1.blocks.1        |    0.111M              |    58.15G  |
|   conv_blocks_context.2.blocks           |   0.664M               |   43.57G   |
|    conv_blocks_context.2.blocks.0        |    0.222M              |    14.537G |
|    conv_blocks_context.2.blocks.1        |    0.443M              |    29.033G |
|   conv_blocks_context.3.blocks           |   2.656M               |   21.764G  |
|    conv_blocks_context.3.blocks.0        |    0.886M              |    7.258G  |
|    conv_blocks_context.3.blocks.1        |    1.77M               |    14.506G |
|   conv_blocks_context.4.blocks           |   4.979M               |   5.099G   |
|    conv_blocks_context.4.blocks.0        |    2.213M              |    2.267G  |
|    conv_blocks_context.4.blocks.1        |    2.766M              |    2.833G  |
|   conv_blocks_context.5                  |   5.532M               |   0.708G   |
|    conv_blocks_context.5.0.blocks.0      |    2.766M              |    0.354G  |
|    conv_blocks_context.5.1.blocks.0      |    2.766M              |    0.354G  |
|  tu                                      |  1.819M                |  15.808G   |
|   tu.0                                   |   0.819M               |   0.105G   |
|    tu.0.weight                           |    (320, 320, 2, 2, 2) |            |
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