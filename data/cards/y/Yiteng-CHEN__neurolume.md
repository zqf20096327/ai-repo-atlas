# Yiteng-CHEN/neurolume

⭐ 4 · Python · MIT · 推送 2026-11-06 · [GitHub](https://github.com/Yiteng-CHEN/neurolume) · [官网](https://yiteng-chen.github.io/neurolume/) · 个人维护 · 中文 README

**Mac 上微调本地 LLM 并逐层可视化训练变化的应用**

面向 Apple Silicon Mac 的本地应用，将 LoRA 微调与可解释性观察放在同一界面：提供数据收集/导入与自动检查、引导式 LoRA 训练（不改基座模型，产出独立 adapter）、验证损失前后对比与逐层 ΔW 展示；推理侧提供 3D 分层活动视图、logit lens、逐 token 置信度回放。附带 OpenAI 兼容本地 API、知识库、网页搜索与逐项审批的 agent。声明处于 early alpha，已在 MacBook Pro M5 Max（128 GB）上验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 引导式 LoRA 训练：密钥扫描、去重、训练/验证切分，产出独立 adapter
- logit lens 与逐层活动视图，展示每层对生成 token 的预测与改动
- 训练前后对比：验证损失、逐层 ΔW 条形图与同问题双模型对照
- 导出 MLX（LM Studio 可直接加载）或到 Ollama

## 适用场景

- 在 Mac 上无代码微调本地 LLM 并观察训练效果
- 逐层查看模型生成与训练过程发生了什么变化
- 本地对话、知识库问答与代码修改建议的日常使用

## 场景标签

`微调` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L4: Fine-tune an LLM on your Mac in a few clicks — and see, layer by layer, what training actually changed.
> L15: Most fine-tuning tools stop at "training finished, loss = 1.23". Most interpretability tools show a model you canno
> L23: - **Guided LoRA training** with automatic checks (secret scan, de-duplication, train/validation split), live loss, 

## 星数曲线

```mermaid
xychart-beta
    title "Yiteng-CHEN/neurolume 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-15", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `a738cf8edb52` · [字段定义](../../DATASET.md)*
