# Checkpoints and Weights

In our work, we generated final checkpoints for the six main model configurations. In this public version of the repository, we do **not** redistribute those checkpoints or any complete trained weight files.

## Why Checkpoints Are Not Included

We avoid publishing complete model weights for security, size and licensing reasons. Some models are based on external initialization sources such as ImageNet, RadImageNet/RAC, ISIC/MaxNet or other pretrained resources. Final fine-tuned checkpoints may contain parameters derived from those external sources, so redistribution must respect their original terms.

## Public Repository Policy

The repository keeps only:

- code and notebooks;
- aggregate metrics;
- final aggregate figures;
- documentation and the final report.

The following files are intentionally excluded:

- `*.keras`
- `*.h5`
- `*.pt`
- `*.pth`
- `*.ckpt`
- model checkpoints;
- external pretrained weights;
- local training logs;
- dataset caches;
- raw DermaMNIST images or arrays.

## Checkpoint Folder

The folder `models/checkpoints/` is kept only as a placeholder with `.gitkeep`.

```text
models/checkpoints/
`-- .gitkeep
```

To reproduce the models, obtain datasets and external pretrained weights from their official sources and run the notebook or scripts locally.

