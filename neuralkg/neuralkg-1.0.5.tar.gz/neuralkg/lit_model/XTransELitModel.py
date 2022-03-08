from logging import debug
import pytorch_lightning as pl
import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import os
import json
from collections import defaultdict as ddict
from IPython import embed
from .BaseLitModel import BaseLitModel
from neuralkg.eval_task import *
from IPython import embed

from functools import partial

class XTransELitModel(BaseLitModel):
    def __init__(self, model, args):
        super().__init__(model, args)
        
    def forward(self, x):
        return self.model(x)
    
    def training_step(self, batch, batch_idx):

        triples  = batch["positive_sample"]
        neg      = batch["negative_sample"]
        neighbor = batch["neighbor"]
        mask     = batch['mask']
        mode     = batch['mode']
        pos_score = self.model(triples, neighbor, mask)
        neg_score = self.model(triples, neighbor, mask, neg, mode=mode)
        loss = self.loss(pos_score, neg_score)
        self.log("Train|loss", loss,  on_step=False, on_epoch=True)
        return loss
    
    def validation_step(self, batch, batch_idx):
        # pos_triple, tail_label, head_label = batch
        results = dict()
        ranks = XTransE_predict(batch, self.model, predicion='tail')
        results["count"] = torch.numel(ranks)
        results["Eval|mrr"] = torch.sum(1.0 / ranks).item()
        for k in [1, 3, 10]:
            results['Eval|hits@{}'.format(k)] = torch.numel(ranks[ranks <= k])
        return results
    
    def validation_epoch_end(self, results) -> None:
        outputs = self.get_results(results, "Eval|")
        # self.log("Eval|mrr", outputs["Eval|mrr"], on_epoch=True)
        self.log_dict(outputs, prog_bar=True, on_epoch=True)

    def test_step(self, batch, batch_idx):
        results = dict()
        ranks = XTransE_predict(batch, self.model, predicion='tail')
        results["count"] = torch.numel(ranks)
        results["Test|mrr"] = torch.sum(1.0 / ranks).item()
        for k in [1, 3, 10]:
            results['Test|hits@{}'.format(k)] = torch.numel(ranks[ranks <= k])
        return results
    
    def test_epoch_end(self, results) -> None:
        outputs = self.get_results(results, "Test|")
        self.log_dict(outputs, prog_bar=True, on_epoch=True)
    
    def get_results(self, results, mode):
        outputs = ddict(float)
        count = np.array([o["count"] for o in results]).sum().item()
        metrics = ["mrr", "hits@1", "hits@3", "hits@10"]
        metrics = [mode + metric for metric in metrics]
        for metric in metrics:
            number = np.array([o[metric] for \
             o in results]).sum().item() / count
            outputs[metric] = round(number, 2)
        return outputs

    '''这里设置优化器和lr_scheduler'''
    def configure_optimizers(self):
        milestones = int(self.args.max_epochs / 2)
        optimizer = self.optimizer_class(self.model.parameters(), lr=self.args.lr)
        StepLR = torch.optim.lr_scheduler.MultiStepLR(optimizer, milestones=[milestones], gamma=0.1)
        optim_dict = {'optimizer': optimizer, 'lr_scheduler': StepLR}
        return optim_dict
