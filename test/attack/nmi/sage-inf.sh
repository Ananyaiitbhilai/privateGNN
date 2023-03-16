python attack.py sage-inf nmi \
--dataset facebook \
--shadow_base_layers 2 \
--shadow_head_layers 1 \
--shadow_mp_layers 2 \
--shadow_hidden_dim 64 \
--shadow_activation selu \
--shadow_optimizer adam \
--shadow_learning_rate 0.01 \
--shadow_batch_norm True \
--shadow_epochs 100 \
--shadow_batch_size full \
--shadow_val_interval 0 \
--num_nodes_per_class 1000 \
--attack_hidden_dim 64 \
--attack_num_layers 3 \
--attack_activation selu \
--attack_batch_norm True \
--attack_batch_size full \
--attack_epochs 100 \
--attack_optimizer adam \
--attack_learning_rate 0.01 \
--attack_val_interval 1 \
--repeats 10