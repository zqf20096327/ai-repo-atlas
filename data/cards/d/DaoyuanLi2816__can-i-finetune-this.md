# DaoyuanLi2816/can-i-finetune-this

⭐ 793 · Python · MIT · 推送 2026-10-08 · [GitHub](https://github.com/DaoyuanLi2816/can-i-finetune-this) · [官网](https://daoyuanli2816.github.io/can-i-finetune-this/) · 个人维护

**单卡 LLM 微调预检工具：估算显存并生成可运行的 LoRA/QLoRA 方案**

面向持有单张消费级 NVIDIA GPU 的开发者：在加载权重前估算 LoRA/QLoRA 训练的显存占用（权重、量化、梯度、优化器状态、激活、logits 等），输出组件级拆解、候选配置与可运行配方；核心估算无需 PyTorch 与模型权重下载。同一配置契约可衔接真实训练，生成 Transformers/PEFT 运行时配方，并度量本地执行峰值与计划对比。限定 Python 3.10–3.14（训练层 3.12），Windows 原生 CPU/CUDA 与 Linux CPU 受验证，分布式训练与预量化基座不在支持范围。

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

- 加载权重前完成显存预算估算，无需 PyTorch 与权重下载
- 同一配置契约衔接计划与执行，生成 Transformers/PEFT 可运行配方
- 本地基准度量加载、优化器分配与有限更新并记录证据
- 提供 127.0.0.1:8765 本地交互式 demo

## 适用场景

- 在单张消费级 GPU 上判断某个开源模型能否微调
- 预算紧张时获取序列长度/批大小/LoRA 秩的候选配置建议
- 执行真实 QLoRA 快速上手配方并核对实测显存与估算的差异

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L19: `canifinetune` turns those questions into a memory breakdown, configuration
> L59: logits/loss and overhead. Generated recipes use one Transformers/PEFT runtime,

## 星数曲线

```mermaid
xychart-beta
    title "DaoyuanLi2816/can-i-finetune-this 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-24"]
    y-axis "stars" 791 --> 794
    line [793, 792, 793, 793]
```

2026-10-18 793 → 2026-10-24 793（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `2454b4558566` · [字段定义](../../DATASET.md)*
