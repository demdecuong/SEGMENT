python evaluate.py --task=SM --model=PG --load_glove=False --data=cnndm \
    --batch_size=16 --eval_batch_size=32 \
    --use_focus=True --n_mixture=1 --decoding=beam \
    --load_ckpt=5 --eval_only