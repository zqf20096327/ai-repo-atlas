# sous-labs/songe

⭐ 150 · Python · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/sous-labs/songe) · [官网](https://souslabs.ai/songe) · 组织维护

**利用空闲算力在本地持续微调你的本地模型的训练引擎**

Songe 是一个本地模型训练引擎：以本地代理服务器（127.0.0.1:7613）形式运行在 agent 与模型服务器之间，记录对话中的纠错、偏好声明与工具错误，在 agent 空闲时执行 Quick Dream（把偏好写入模型指令）或 Deep Dream（通过 on-policy distillation 训练小型适配器），新版本仅在自检通过后启用，支持一键回退。需本地模型服务器与 agent 配合；无 GPU 机器只记录不训练；数据不出本机，无账号与遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拦截式记录 agent 对话中的纠错、偏好与工具错误作为学习素材
- Quick Dream 分钟级改写指令，Deep Dream 用 on-policy distillation 训练 LoRA 适配器
- 新版本经对比检查通过才启用，可一键回退任意旧版本
- 仅在 agent 空闲、内存充足、电池状态良好时运行

## 适用场景

- 让本地编码 agent 在日常使用中逐步吸收我的偏好与纠错
- 利用机器空闲时段自动训练专属模型版本
- 在不上传对话数据的前提下做私有化模型微调

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L3:  A training engine for your local model, using your idle compute.
> L73: |Model servers|LM Studio, vLLM, Ollama, llama.cpp, mlx-lm|LM Studio (macOS), vLLM (Linux)|
> L110:  (on-policy distillation). Earlier skills are rehearsed so they stay.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `91741a121442` · [字段定义](../../DATASET.md)*
