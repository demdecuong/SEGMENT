import torch
def cal_performance(pred, gold, trg_pad_idx,config):
    ''' Apply label smoothing if needed '''

    # loss = cal_loss(pred, gold, trg_pad_idx, smoothing=smoothing)
    pred = (pred > config.threshold).type(torch.uint8) 
    # pred = pred.max(1)[1]
    # gold = gold.contiguous().view(-1)
    # non_pad_mask = gold.ne(trg_pad_idx)
    # n_correct = pred.eq(gold).masked_select(non_pad_mask).sum().item()
    n_correct = pred.eq(gold).sum().item()
    # n_word = non_pad_mask.sum().item()
    n_word = gold.shape[0] * gold.shape[1]

    return n_correct, n_word