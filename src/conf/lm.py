import time as _time
from src.lm_networks import LandmarkExpNetwork as _net
from src.lm_networks import LandmarkBranchUpsample as _lm_branch
from src.utils import LandmarkEvaluator as _evaluator

_name = 'lm'
_time = _time.strftime('%m-%d %H:%M:%S', _time.localtime())

# Dataset
gaussian_R = 8
DATASET_PROC_METHOD_TRAIN = 'BBOXRESIZE'
DATASET_PROC_METHOD_VAL = 'BBOXRESIZE'
########

# Network
USE_NET = _net
LM_SELECT_VGG = 'conv4_3'
LM_SELECT_VGG_SIZE = 28
LM_SELECT_VGG_CHANNEL = 512
LM_BRANCH = _lm_branch
EVALUATOR = _evaluator
#################

# Learning Scheme
LEARNING_RATE_DECAY = 0.8
WEIGHT_LOSS_LM_POS = 10
#################

# auto
TRAIN_DIR = 'runs/%s/' % _name #+ _time
VAL_DIR = 'runs/%s/' % _name #+ _time

MODEL_NAME = '%s.pkl' % _name
#############
