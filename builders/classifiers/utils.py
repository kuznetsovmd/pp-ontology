import math
import time


def time_since(since):
    now = time.time()
    s = now - since
    m = math.floor(s / 60)
    s -= m * 60
    return '%dm %ds' % (m, s)


def print_stats(epoch, n_epochs, start, stats):
        print(f'R: epoch={epoch} [{epoch * 100 // n_epochs}%] time=[{time_since(start)}]\n'
              f'T loss={stats["t_loss"]:.3f}, T f1={stats["t_f1"]:.3f}, T pr_auc={stats["t_pr_auc"]:.3f}\n'
              f'V loss={stats["v_loss"]:.3f}, V f1={stats["v_f1"]:.3f}, V pr_auc={stats["v_pr_auc"]:.3f}')
    