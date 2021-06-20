python train.py --task=SM --model=PG --load_glove=False --data=cnndm \
    --batch_size=8 --eval_batch_size=16 \
    --use_focus=True --n_mixture=1 --decoding=beam  \
    --load_ckpt=-1 --dropout=0.02