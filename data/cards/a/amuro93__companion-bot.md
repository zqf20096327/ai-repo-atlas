# amuro93/companion-bot

⭐ 3 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/amuro93/companion-bot) · [官网](https://drizzt-studio.com) · 个人维护 · 中文 README

**本地运行、存原句长期记忆的 Telegram 陪伴 Bot**

以 SQLite 为核心的 Telegram 单一拥有者陪伴对话 Bot，可在任何 OpenAI 兼容 /v1/chat/completions 端点上运行。记忆层存用户原句而非 LLM 摘要，区分短期历史、固定设定、key-value 事实、语义检索与延迟抽取队列，写入走单事务，来源撤回时衍生记忆一并排除。启动采用 fail-closed 严格校验（端点白名单、凭证仅从环境变量读取），支持运行期 /model 切换多后端，为推理模型设置 bounded thinking 预算。含 555 项自动化测试；作者声明尚未做多实例或大规模部署验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 分层记忆只存用户原句，不做 LLM 摘要，可回溯原文
- fail-closed 启动检查：严格配置校验、端点白名单、凭证仅从环境变量读取
- 运行期 /model 切换多个 OpenAI 兼容后端，重启保留选择
- 555 项自动化测试，无需网络或真实模型/token

## 适用场景

- 自托管一个长期记得个人生活细节的陪伴聊天机器人
- 敏感对话走本地模型、日常走云端的切换使用
- 研究存原句而非摘要的记忆系统实现

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L7: 一個以 SQLite 為核心、可完全在地端模型上運行的陪伴型對話 Bot。目標不是「問答」，而是讓角色記得你說過的事、說得像人、並且在模型出狀況時**明確失敗而不是胡言亂語**。
> L9: - 對話後端：任何 OpenAI 相容的 `/v1/chat/completions`（llama.cpp、vLLM、Ollama、雲端 API 皆可）
> L11: - 介面：Telegram（私人對話，單一擁有者）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `0d4ce7f1f2fe` · [字段定义](../../DATASET.md)*
