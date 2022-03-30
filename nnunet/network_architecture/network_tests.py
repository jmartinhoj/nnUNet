# nnUNet_predict -i /media/jomstorage/datasets/nnUNet_raw_data/Task001_KiTS2021/imagesTr -o ~/out_test -t 1 -m 3d_fullres

from efficient_Unet import Efficient_UNet
from nnunet.network_architecture.initialization import InitWeights_He
from torch import nn
from nnunet.training.dataloading.dataset_loading import load_dataset, DataLoader3D, DataLoader2D, unpack_dataset
import numpy as np
from nnunet.training.dataloading.dataset_loading import load_dataset
from nnunet.paths import network_training_output_dir, preprocessing_output_dir, default_plans_identifier
from batchgenerators.utilities.file_and_folder_operations import *
from nnunet.utilities.task_name_id_conversion import convert_id_to_task_name
from collections import OrderedDict



dataset = load_dataset(join(join(preprocessing_output_dir, convert_id_to_task_name(1)), "nnUNetData_plans_v2.1" + "_stage%d" % 1))

rnd = np.random.RandomState(seed=12345 + 0)
keys = np.sort(list(dataset.keys()))
idx_tr = rnd.choice(len(keys), int(len(keys) * 0.8), replace=False)
idx_val = [i for i in range(len(keys)) if i not in idx_tr]
tr_keys = [keys[i] for i in idx_tr]
val_keys = [keys[i] for i in idx_val]
tr_keys.sort()
dataset_tr = OrderedDict()
for i in tr_keys:
    dataset_tr[i] = dataset[i]

dl_tr = DataLoader3D(dataset_tr, 1, self.patch_size, self.batch_size,
                        False, oversample_foreground_percent=self.oversample_foreground_percent,
                        pad_mode="constant", pad_sides=self.pad_all_sides, memmap_mode='r')

print(next(dl_tr))

# network = Efficient_UNet(1, 32, 4, 5, 2, 2, nn.Conv3d, nn.InstanceNorm3d, {'eps': 1e-5, 'affine': True}, nn.Dropout3d, {'p': 0, 'inplace': True}, nn.LeakyReLU, {'negative_slope': 1e-2, 'inplace': True}, True, False, lambda x: x, InitWeights_He(1e-2), [[2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]], [[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]], False, True, True)