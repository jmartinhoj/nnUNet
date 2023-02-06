

from turtle import forward
from torch import nn
from nnunet.network_architecture.nvnet.metrics import CustomKLLoss


class CombinedLoss(nn.Module):
    def __init__(self, multiple_loss, k1 = 0.1, k2 = 0.1):
        """
        use this if you have several outputs and ground truth (both list of same len) and the loss should be computed
        between them (x[0] and y[0], x[1] and y[1] etc)
        :param loss:
        :param weight_factors:
        """
        super(CombinedLoss, self).__init__()
        self.k1 = k1
        self.k2 = k2
        self.multiple_loss = multiple_loss
        self.l2loss = nn.MSELoss()
        self.klloss = CustomKLLoss()

    def forward(self, seg_out, seg_gt, vae_out, data, dist_out):
        num_features = dist_out.shape[1]//2
        est_mean, est_std = (dist_out[:, :num_features], dist_out[:, num_features:])
        dloss = self.multiple_loss(seg_out, seg_gt)
        l2loss = self.l2loss(vae_out, data)
        klloss = self.klloss(est_mean, est_std)


        print("l2", l2loss * self.k1)
        print("kl", klloss * self.k2)

        return dloss + self.k1 * l2loss + self.k2 * klloss



class CombinedLoss_L2(nn.Module):
    def __init__(self, multiple_loss, k1 = 0.01):
        """
        use this if you have several outputs and ground truth (both list of same len) and the loss should be computed
        between them (x[0] and y[0], x[1] and y[1] etc)
        :param loss:
        :param weight_factors:
        """
        super(CombinedLoss_L2, self).__init__()
        self.k1 = k1
        self.multiple_loss = multiple_loss
        self.l2loss = nn.MSELoss()
        # self.klloss = CustomKLLoss()

    def forward(self, seg_out, seg_gt, vae_out, data, dist_out):
        num_features = dist_out.shape[1]//2
        est_mean, est_std = (dist_out[:, :num_features], dist_out[:, num_features:])
        dloss = self.multiple_loss(seg_out, seg_gt)
        l2loss = self.l2loss(vae_out, data)
        # klloss = self.klloss(est_mean, est_std)


        # print("l2", l2loss * self.k1)
        # print("kl", klloss * self.k2)

        return dloss + self.k1 * l2loss
