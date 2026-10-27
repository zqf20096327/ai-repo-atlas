# FasterAI-Labs/fasterai

⭐ 269 · Jupyter Notebook · Apache-2.0 · 推送 2026-09-25 · [GitHub](https://github.com/FasterAI-Labs/fasterai) · [官网](https://fasterai-labs.github.io/fasterai/) · 个人维护

**基于 PyTorch/FastAI 的模型压缩库：剪枝、蒸馏、量化、稀疏化**

面向使用 PyTorch 与 FastAI 的开发者的模型压缩库，通过回调（Callback）与独立类形式提供五种压缩能力：稀疏化（Sparsifier/SparsifyCallback，支持 magnitude/movement/gradient 等多种选择准则与 one_shot/iterative/gradual 等调度）、结构剪枝（Pruner）、知识蒸馏（KnowledgeDistillationCallback，支持 SoftTarget/Logits/Attention 等损失）、正则化与量化（static/dynamic/qat，x86/qnnpack 后端）。压缩操作可在训练循环中以几行代码接入。以 pip 安装的 Python 库形式提供，Apache-2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 稀疏化/剪枝/蒸馏/正则化/量化五类压缩方法
- 多种权重选择准则与稀疏调度策略可配置
- 以 FastAI Callback 形式接入训练循环
- 量化支持 static/dynamic/qat 与 x86/qnnpack 后端

## 适用场景

- 把 PyTorch 模型压缩后部署到边缘设备
- 用知识蒸馏把大模型能力迁移到小模型
- 降低模型的体积与推理开销

## 场景标签

`模型量化` · 领域:训练与推理

## 证据(README 行号)

> L12: fasterAI is a PyTorch-based library that makes neural networks **smaller**, **faster**, and **more efficient** thro
> L100: learn.fit_one_cycle(n_epochs, cbs=SparsifyCallback(sparsity, granularity, context, criteria, schedule))

## 星数曲线

```mermaid
xychart-beta
    title "FasterAI-Labs/fasterai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 268 --> 270
    line [269, 269]
```

2026-10-18 269 → 2026-10-27 269（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `bac4d9f17bda` · [字段定义](../../DATASET.md)*
