# Tencent-Hunyuan/UniRL

⭐ 1,052 · Python · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/Tencent-Hunyuan/UniRL) · [官网](https://unirl-project.github.io/unirl/) · 组织维护

**面向研究者的统一多模态模型强化学习后训练框架**

UniRL 对图像/视频扩散模型、AR/VLM/LLM 及统一多模态模型执行同一套 RL 后训练循环：生成样本、打分、计算优势、更新策略并回同步权重到 rollout worker。系统分层组合，由 Hydra 配置驱动的多个训练入口（扩散 RL、AR RL、SFT、Agentic RL、异步 RL 等）协调可插拔的 rollout 引擎、算法、模型包与奖励服务，共享 Ray/FSDP/LoRA 同步等分布式运行时。安装依赖见 INSTALL.md，通过 python 模块命令或单节点脚本启动示例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一套 RL 后训练循环覆盖扩散、AR、统一多模态多类模型
- 8 种训练入口：扩散 RL、AR RL、SFT、Agentic、异步 AR/扩散等
- 自带 Flow-DPPO、DRPO、CPPO 等团队提出的算法及教程
- 基于 Ray DevicePool、FSDP、TQ 与 LoRA/全量权重同步的分布式运行时

## 适用场景

- 对 Stable Diffusion、WAN、HunyuanVideo 等扩散模型做 RL 后训练
- 对 Qwen3、Qwen2.5-VL 等文本/视觉语言模型做 GRPO 类 RL 训练
- 用奖励服务打分的多轮工具使用 Agentic RL 训练
- 在分离的 train/rollout worker 上做异步 RL 训练

## 场景标签

`强化学习` · 领域:训练与推理

## 证据(README 行号)

> L1: UniRL — A Reinforcement Learning Framework for Unified Multimodal Models
> L31: UniRL is a layered, composable system. Each **training entrypoint** loads a
> L33: coordinate generation, scoring, and updates across pluggable

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/UniRL 星数(近 19 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-19", "2026-11-22", "2026-11-25", "2026-11-28"]
    y-axis "stars" 1023 --> 1054
    line [1025, 1029, 1031, 1032, 1033, 1034, 1035, 1037, 1025, 1045, 1046, 1045, 1046, 1049, 1050, 1052, 1051, 1052, 1052]
```

2026-10-26 1,025 → 2026-11-28 1,052（+27）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `c07e1c340bb7` · [字段定义](../../DATASET.md)*
