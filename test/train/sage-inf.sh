python train.py sage-inf \
--dataset facebook \
--base_layers 2 \
--head_layers 1 \
--mp_layers 2 \
--hidden_dim 16 \
--activation selu \
--optimizer adam \
--learning_rate 0.01 \
--repeats 10 \
--batch_norm True \
--epochs 100 \
--batch_size full $@