# klieret/wandb-offline-sync-hook

⭐ 92 · Python · MIT · 推送 2026-10-06 · [GitHub](https://github.com/klieret/wandb-offline-sync-hook) · [官网](https://wandb-offline-sync-hook.rtfd.io/) · 个人维护

**为无网计算节点触发 wandb 同步的钩子工具**

面向使用 Weights & Biases 记录机器学习实验、但计算节点无外网访问（如批处理系统）的用户。机制：训练循环每个 epoch 结束时调用钩子，在共享文件系统的通信目录（默认 ~/.wandb_osh_communication）创建文件；在有外网的登录/头节点上运行的 wandb-osh 脚本读取这些文件并执行 wandb sync。提供纯 wandb、PyTorch Lightning、Ray Tune 三种接入方式及通用回调类。支持 pip 安装，Python 3.8–3.11。README 注明 Ray Tune 场景下可能无需本包（可将 ray head 部署在头节点）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过共享文件系统的文件通信触发离线 run 的 wandb 同步
- 提供 wandb / PyTorch Lightning / Ray Tune 三种钩子与通用回调类
- wandb-osh 命令行脚本支持传递 wandb sync 参数（如 --sync-all）

## 适用场景

- SLURM 等批处理系统上计算节点无外网时同步 wandb 实验记录
- 离线训练中更及时地把 run 数据同步到 Weights & Biases
- PyTorch Lightning 或 Ray Tune 训练中一行接入同步触发

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L17: - ✅ You use `wandb`/Weights & Biases to record your machine learning trials?
> L18: - ✅ Your ML experiments run on compute nodes without internet access (for example, using a batch system)?
> L38: 1. You add a hook that is called every time an epoch concludes (that is, when we want to trigger a sync).
> L39: 2. You start the `wandb-osh` script in your head node with internet access. This script will now trigger `wandb syn

## 星数曲线

```mermaid
xychart-beta
    title "klieret/wandb-offline-sync-hook 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-25 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `873b859d99bb` · [字段定义](../../DATASET.md)*
