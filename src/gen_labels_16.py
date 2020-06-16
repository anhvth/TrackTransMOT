from glob import glob
import os.path as osp
import os
import numpy as np


def mkdirs(d):
    if not osp.exists(d):
        os.makedirs(d)


seq_root = '/data/JDE/MOT16/'
label_root = '/data/JDE/MOT16/labels_with_ids/'
mkdirs(label_root)
#seqs = [s for s in os.listdir(seq_root)]
seqs = ['ADL-Rundle-6', 'ETH-Bahnhof', 'KITTI-13', 'PETS09-S2L1', 'TUD-Stadtmitte', 'ADL-Rundle-8', 'KITTI-17',
        'ETH-Pedcross2', 'ETH-Sunnyday', 'TUD-Campus', 'Venice-2']

tid_curr = 0
tid_last = -1

path_seqs = glob(f"{seq_root}/**/*.ini", recursive=True)
path_gts = glob(f"{seq_root}/**/*gt.txt", recursive=True)

img_paths = glob(f"{seq_root}/**/*.jpg", recursive=True)
def get_txt_output_path_from_fid(fid):
    fname = "{:06d}.jpg".format(fid)
    for path in img_paths:
        if fname in path:
            return path.replace("images", "labels_with_ids").replace(".jpg", ".txt")

    raise Exception("Not found images")

for path_seq in path_seqs:
    seq_info = open(path_seq).read()
    seq_width = int(seq_info[seq_info.find('imWidth=') + 8:seq_info.find('\nimHeight')])
    seq_height = int(seq_info[seq_info.find('imHeight=') + 9:seq_info.find('\nimExt')])

    #gt_txt = osp.join(seq_root, seq, 'gt', 'gt.txt').replace("seqinfo","train")
    gt_txt = path_seq.replace("seqinfo.ini", "gt/gt.txt" )
    if not  osp.exists(gt_txt): continue

    gt = np.loadtxt(gt_txt, dtype=np.float64, delimiter=',')

    idx = np.lexsort(gt.T[:2, :])
    gt = gt[idx, :]

    #seq_label_root = osp.join(label_root, seq, 'img1')
    seq_label_root = osp.dirname(path_seq).replace("images", "labels_with_ids")
    seq_label_root = osp.join(seq_label_root, "img1")
    mkdirs(seq_label_root)

    for fid, tid, x, y, w, h, mark in gt[:,:7]:
        if mark == 0:
            continue
        fid = int(fid)
        tid = int(tid)
        if not tid == tid_last:
            tid_curr += 1
            tid_last = tid
        x += w / 2
        y += h / 2
        label_fpath = osp.join(seq_label_root, '{:06d}.txt'.format(fid))
        label_str = '0 {:d} {:.6f} {:.6f} {:.6f} {:.6f}\n'.format(
            tid_curr, x / seq_width, y / seq_height, w / seq_width, h / seq_height)

        os.makedirs(os.path.basename(label_fpath), exist_ok=True)
        with open(label_fpath, 'w') as f:
            f.write(label_str)
        print(label_fpath)
