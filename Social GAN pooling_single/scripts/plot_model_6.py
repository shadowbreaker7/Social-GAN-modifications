import argparse
import os
import torch
import numpy as np
import random

from attrdict import AttrDict
import matplotlib.pyplot as plt
from matplotlib import animation

from sgan.data.loader import data_loader
from sgan.models import TrajectoryGenerator
from sgan.losses import displacement_error, final_displacement_error
from sgan.utils import relative_to_abs, get_dset_path

parser = argparse.ArgumentParser()
parser.add_argument('--model_path', default='../models/c0',type=str)
parser.add_argument('--num_samples', default=20, type=int)
parser.add_argument('--dset_type', default='test', type=str)

os.environ['KMP_DUPLICATE_LIB_OK']='True'

total_aa,total_bb=[],[]

xdata0, ydata0 = [], []
xdata1, ydata1 = [], []
xdata2, ydata2 = [], []
xdata3, ydata3 = [], []
xdata4, ydata4 = [], []
xdata5, ydata5 = [], []
xdata6, ydata6 = [], []
xdata7, ydata7 = [], []
xdata8, ydata8 = [], []
xdata9, ydata9 = [], []
xdata10, ydata10 = [], []
xdata11, ydata11 = [], []

x11,y11,x12,y12,x13,y13,x14,y14=[],[],[],[],[],[],[],[]
x15,y15,x16,y16 = [],[],[],[]

x01,y01,x02,y02,x03,y03,x04,y04=[],[],[],[],[],[],[],[]
x05,y05,x06,y06 = [],[],[],[]

aa, bb = [], []

num_t=0
fig, ax = plt.subplots()
ln11, = ax.plot([], [], 'b--',label = 'defender 1')
ln12, = ax.plot([], [], 'g--',label = 'defender 2')
ln21, = ax.plot([], [], 'r--',label = 'defender 3')
ln22, = ax.plot([], [], 'c--',label = 'attacker 1')
ln51, = ax.plot([], [], 'k--',label = 'attacker 2')
ln52, = ax.plot([], [], 'm--',label = 'attacker 3')
ln31, = ax.plot([], [], 'b:')
ln32, = ax.plot([], [], 'g:')
ln41, = ax.plot([], [], 'r:')
ln42, = ax.plot([], [], 'c:')
ln61, = ax.plot([], [], 'k:')
ln62, = ax.plot([], [], 'm:')

def init():
    ax.set_xlim(10, 300)
    ax.set_ylim(10, 300)

def gen_dot():
    for i in range(0,len(x01)):
        newdot = [x01[i], y01[i]]
        yield newdot

def update_dot(newd):
    global num_t
    if(num_t<len(x01)):
        xdata0.append(newd[0])# x01
        ydata0.append(newd[1])# y01

        xdata1.append(x02[num_t])
        ydata1.append(y02[num_t])

        xdata2.append(x03[num_t])
        ydata2.append(y03[num_t])

        xdata3.append(x04[num_t])
        ydata3.append(y04[num_t])

        xdata4.append(x11[num_t])
        ydata4.append(y11[num_t])

        xdata5.append(x12[num_t])
        ydata5.append(y12[num_t])

        xdata6.append(x13[num_t])
        ydata6.append(y13[num_t])

        xdata7.append(x14[num_t])
        ydata7.append(y14[num_t])

        xdata8.append(x05[num_t])
        ydata8.append(y05[num_t])

        xdata9.append(x06[num_t])
        ydata9.append(y06[num_t])

        xdata10.append(x15[num_t])
        ydata10.append(y15[num_t])

        xdata11.append(x16[num_t])
        ydata11.append(y16[num_t])

        num_t = num_t +1

        ln11.set_data(xdata0, ydata0)
        ln12.set_data(xdata1, ydata1)

        ln21.set_data(xdata2, ydata2)
        ln22.set_data(xdata3, ydata3)

        ln31.set_data(xdata4, ydata4)
        ln32.set_data(xdata5, ydata5)

        ln41.set_data(xdata6, ydata6)
        ln42.set_data(xdata7, ydata7)

        ln51.set_data(xdata8,ydata8)
        ln52.set_data(xdata9,ydata9)

        ln61.set_data(xdata10,ydata10)
        ln62.set_data(xdata11,ydata11)

        return ln11,ln12,ln21,ln22,ln31,ln32,ln41,ln42

def ploot():
    global x01,x02,x03,x04,y01,y02,y03,y04,x05,y05,x06,y06,x11,x12,x13,x14,y11,y12,y13,y14,x15,y15,x16,y16

    x01=total_aa[0][:,0]
    y01=total_aa[0][:,1]

    x02=total_aa[1][:,0]
    y02=total_aa[1][:,1]

    x03=total_aa[2][:,0]
    y03=total_aa[2][:,1]

    x04=total_aa[3][:,0]
    y04=total_aa[3][:,1]

    x05=total_aa[4][:,0]
    y05=total_aa[4][:,1]

    x06=total_aa[5][:,0]
    y06=total_aa[5][:,1]

    x11=total_bb[0][:,0]
    y11=total_bb[0][:,1]

    x12=total_bb[1][:,0]
    y12=total_bb[1][:,1]

    x13=total_bb[2][:,0]
    y13=total_bb[2][:,1]

    x14=total_bb[3][:,0]
    y14=total_bb[3][:,1]

    x15=total_bb[4][:, 0]
    y15=total_bb[4][:, 1]

    x16=total_bb[5][:, 0]
    y16=total_bb[5][:, 1]

    ani = animation.FuncAnimation(fig, update_dot, frames = gen_dot, interval = 500, init_func=init)
    plt.legend()
    plt.show()
    plt.close()

def get_generator(checkpoint):
    args = AttrDict(checkpoint['args'])
    generator = TrajectoryGenerator(
        obs_len=args.obs_len,
        pred_len=args.pred_len,
        embedding_dim=args.embedding_dim,
        encoder_h_dim=args.encoder_h_dim_g,
        decoder_h_dim=args.decoder_h_dim_g,
        mlp_dim=args.mlp_dim,
        num_layers=args.num_layers,
        noise_dim=args.noise_dim,
        noise_type=args.noise_type,
        noise_mix_type=args.noise_mix_type,
        pooling_type=args.pooling_type,
        pool_every_timestep=args.pool_every_timestep,
        dropout=args.dropout,
        bottleneck_dim=args.bottleneck_dim,
        neighborhood_size=args.neighborhood_size,
        grid_size=args.grid_size,
        batch_norm=args.batch_norm)
    generator.load_state_dict(checkpoint['g_state'])
    generator.cuda()
    generator.train()
    return generator

def evaluate(args, loader, generator, num_samples):
    with torch.no_grad():
        for idx,batch in enumerate(loader):
            if idx == 1:
                batch = [tensor.cuda() for tensor in batch]
                (obs_traj, pred_traj_gt, obs_traj_rel, pred_traj_gt_rel,
                 non_linear_ped, loss_mask, seq_start_end) = batch

                i = random.randint(0,63)
                start,end = seq_start_end[i]

                for _ in range(1):
                    pred_traj_fake_rel = generator(
                        obs_traj, obs_traj_rel, seq_start_end
                    )
                    pred_traj_fake = relative_to_abs(
                        pred_traj_fake_rel, obs_traj[-1]
                    )

                    gt = pred_traj_gt[:, start:end, :].data.cpu()
                    input_a = obs_traj[:, start:end, :].data.cpu()
                    out_a = pred_traj_fake[:, start:end, :].data.cpu()
                    aa = np.concatenate((input_a, gt), axis=0)
                    bb = np.concatenate((input_a, out_a), axis=0)
                    global x0, y0, x1, y1, total_aa, total_bb
                    for i in range(abs(start-end)):
                        total_aa.append(aa[:,i,:])
                        total_bb.append(bb[:,i,:])


def main(args):
    if os.path.isdir(args.model_path):
        filenames = os.listdir(args.model_path)
        filenames.sort()
        paths = [
            os.path.join(args.model_path, file_) for file_ in filenames
        ]
    else:
        paths = [args.model_path]

    for path in paths:
        checkpoint = torch.load(path)
        generator = get_generator(checkpoint)
        _args = AttrDict(checkpoint['args'])
        path = get_dset_path(_args.dataset_name, args.dset_type)
        _, loader = data_loader(_args, path)
        evaluate(_args, loader, generator, args.num_samples)
        ploot()

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)