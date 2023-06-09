python train.py mlp-dp \
--dataset facebook \
--epsilon 8 \
--num_layers 3 \
--hidden_dim 16 \
--activation selu \
--optimizer adam \
--learning_rate 0.01 \
--repeats 10 \
--max_grad_norm 1 \
--epochs 10 \
--batch_size 256
