# THU-BPM/RLCSD

⭐ 115 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/THU-BPM/RLCSD) · [官网](https://arxiv.org/abs/2606.11709) · 组织维护

**面向 LLM 推理训练的对比式 on-policy 自蒸馏 RL 方法代码**

论文 "RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation" 的官方代码库。RLCSD 通过对同一 prompt 下的正确与错误参考解计算师生分布差的对比信号，用以调制 verifier 导出的 GRPO 优势并保持更新方向。仓库基于 verl 实现，提供 GRPO/OPSD/SDPO/SRPO/RLSD 等方法及 RLCSD 本身，附带数学（DeepMath）与逻辑（Knights & Knaves）训练/评测数据下载与启动脚本。实验使用 8 卡 H20 GPU 全参训练，模型覆盖 Qwen3 1.7B–8B 与 Olmo-3-7B。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对比式 token 级信号调制 GRPO 优势的 RLCSD 实现
- 仓库同时实现 GRPO/OPSD/SDPO/SRPO/RLSD 五种基线方法（YAML method 键切换）
- 提供 DeepMath 与 Knights & Knaves 训练/评测数据的一键下载脚本
- 附带各模型规模（Qwen3 1.7B/4B/8B、Olmo-3-7B）的启动脚本与 Hydra 式超参覆盖

## 适用场景

- 复现论文中 RLCSD 与各基线方法的训练结果
- 在自建数学或逻辑推理数据上运行对比式自蒸馏 RL 训练
- 将对比式 hint 构造作为插件组件嫁接到 OPSD/RLSD 等方法上

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L1: # RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation
> L81: Each YAML config selects a method via the `method:` key. Implementations live in
> L92: |`rlcsd`|**This work** — contrastive cancellation across symmetric positive/negative hints, then K-marginalized and

## 星数曲线

```mermaid
xychart-beta
    title "THU-BPM/RLCSD 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 114 --> 116
    line [115, 115]
```

2026-10-18 115 → 2026-10-25 115（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `ad15bd809a3b` · [字段定义](../../DATASET.md)*
