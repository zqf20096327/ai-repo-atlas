# john-carroll-sw/coffee-chat-voice-assistant

⭐ 32 · Jupyter Notebook · MIT · 推送 2026-06-22 · [GitHub](https://github.com/john-carroll-sw/coffee-chat-voice-assistant) · 个人维护

**模拟咖啡馆点单的语音助手：GPT-4o 实时 API 驱动对话点单**

面向终端用户的语音点单系统：前端 RTClient 采集音频，Python 后端经 RTMiddleTier 调用 Azure OpenAI GPT-4o Realtime API，结合 Azure AI Search 检索菜单知识库（RAG），提供实时转写、语音合成输出与基于 function calling 的实时订单更新展示。提供两个 Jupyter notebook 从 JSON/PDF 菜单导入数据。可经 GitHub Codespaces、VS Code Dev Container、本地脚本或 Docker 运行，也可用基础设施即代码部署到 Azure Container Apps；本地运行需配置 Azure OpenAI 与 Azure AI Search 服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Azure OpenAI GPT-4o Realtime API 实时语音对话与转写
- RAG 检索 Azure AI Search 菜单知识库做点单应答
- function calling 驱动的实时订单更新显示
- JSON/PDF 菜单数据导入 notebook 与 Azure Container Apps 部署脚本

## 适用场景

- 语音对话方式完成咖啡点单并实时看到订单变化
- 参考实时音频 + RAG + function calling 的应用架构实现
- 演示多语言语音点单或无障碍免手操作交互

## 场景标签

`语音 Agent` `RAG` · 领域:对话与助手

## 证据(README 行号)

> L3: Coffee Chat Voice Assistant is an advanced, voice-driven ordering system leveraging Azure OpenAI GPT-4o Realtime API
> L51: The `RTClient` in the frontend receives the audio input, sends that to the Python backend which uses an `RTMiddleTi
> L44: - **Retrieval-Augmented Generation (RAG)**: Leverages knowledge bases to ground responses in relevant and contextua

## 星数曲线

```mermaid
xychart-beta
    title "john-carroll-sw/coffee-chat-voice-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-29 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `c650c2d34294` · [字段定义](../../DATASET.md)*
