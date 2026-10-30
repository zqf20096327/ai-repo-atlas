# Eiztrips/ai-responder

⭐ 27 · Python · MIT · 推送 2026-05-20 · [GitHub](https://github.com/Eiztrips/ai-responder) · 个人维护

**用聊天记录训练模型、模仿特定 Telegram 用户语气的自回复机器人**

基于 PyTorch 与 HuggingFace Transformers 的 Telegram 个人机器人工具：把 Telegram 聊天历史转换为训练数据集，训练模仿指定用户风格的语言模型，训练后自动回复消息。支持多模型切换、生成参数配置（温度/长度等四种预设）、三种工作模式（私聊/群组频道/指定用户）。通过 Pyrogram 接入 Telegram，需自备 api_id/api_hash。支持 CPU、NVIDIA GPU（CUDA）与 Apple Silicon（MPS），Debian/Ubuntu 需安装 python3-venv、python3-tk、python3-dev 系统依赖。注意其 self-bot 用法可能违反 Telegram 服务条款，README 未讨论此风险。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Telegram 聊天历史转换为训练数据集并训练个性化模型
- 支持 CPU / NVIDIA GPU (CUDA) / Apple Silicon (MPS)
- 多模型切换与四种生成参数预设（creative/precise/balanced/chatty）
- 三种工作模式：私聊、群组/频道、指定用户（stalker）

## 适用场景

- 用某人的聊天记录训练并生成模仿其语气的自动回复
- 在私聊或指定群组中运行个性化回复机器人
- 在不同硬件（CPU/GPU/MPS）上训练小型个性化模型

## 场景标签

`聊天机器人` `微调` · 领域:对话与助手

## 证据(README 行号)

> L14: AI Telegram Responder — инструмент для создания и обучения моделей, имитирующих стиль общения выбранного пользовате
> L18: - Конвертация истории чатов Telegram в датасеты для обучения

## 星数曲线

```mermaid
xychart-beta
    title "Eiztrips/ai-responder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `0a9bf565ef69` · [字段定义](../../DATASET.md)*
