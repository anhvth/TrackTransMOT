task = 'mot'
dataset = 'jde'
exp_id = 'all_dla34'
test = False
load_model = '../models/ctdet_coco_dla_2x.pth'
resume = False
gpus = [0, 1]
num_workers = 8
not_cuda_benchmark = False
seed = 317
print_iter = 0
hide_data_time = False
save_all = False
metric = 'loss'
vis_thresh = 0.5
arch = 'dla_34'
head_conv = 256
down_ratio = 4
input_res = -1
input_h = -1
input_w = -1
lr = 0.0001
lr_step = [20, 27]
num_epochs = 30
batch_size = 12
master_batch_size = 6
num_iters = -1
val_intervals = 5
trainval = False
K = 128
not_prefetch_test = False
fix_res = True
keep_res = False
test_mot16 = False
val_mot15 = False
test_mot15 = False
val_mot16 = False
test_mot17 = False
val_mot17 = False
val_mot20 = False
test_mot20 = False
conf_thres = 0.6
det_thres = 0.3
nms_thres = 0.4
track_buffer = 30
min_box_area = 200
input_video = '../videos/MOT16-03.mp4'
output_format = 'video'
output_root = '../results'
data_cfg = 'lib/cfg/data.py'
data_dir = './data'
mse_loss = False
reg_loss = 'l1'
hm_weight = 1
off_weight = 1
wh_weight = 0.1
id_loss = 'ce'
id_weight = 1
reid_dim = 512
norm_wh = False
dense_wh = False
cat_spec_wh = False
not_reg_offset = False
gpus_str = '0,1'
reg_offset = True
pad = 31
num_stacks = 1
chunk_sizes = [6, 6]
root_dir = '/home/bi/gitprojects/TrackTransMOT/src/lib/../..'
exp_dir = '/home/bi/gitprojects/TrackTransMOT/src/lib/../../exp/mot'
save_dir = '/home/bi/gitprojects/TrackTransMOT/src/lib/../../exp/mot/all_dla34'
debug_dir = '/home/bi/gitprojects/TrackTransMOT/src/lib/../../exp/mot/all_dla34/debug'