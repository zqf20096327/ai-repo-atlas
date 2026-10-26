# Alex8791-cyber/cognithor

⭐ 157 · Python · Apache-2.0 · 推送 2026-10-19 · [GitHub](https://github.com/Alex8791-cyber/cognithor) · [官网](https://cognithor.ai) · 个人维护

**本地优先的自主 agent 操作系统：私有 AI 助手与自动化**

运行在用户本机的自主 agent 操作系统，定位为个人 AI 助手与自动化平台。支持 19 个 LLM 提供商（Ollama/LM Studio/vLLM/llama-cpp-python 等本地后端，云上 OpenAI/Anthropic/Gemini 等可选），17 个通信渠道（CLI、Web UI、Telegram、Discord 等），6 层记忆与 4 通道混合检索，PGE（Planner-Gatekeeper-Executor）架构执行多步任务，含浏览器自动化、Computer Use、技能市场与 SQLCipher 静态加密。Python 3.12+，pip 安装，Apache 2.0。自称 Pre-v1.0 Beta，API 可能变更，不建议生产部署；默认语言为德语，可切换英语。由单人开发者以 AI 辅助开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 19 个 LLM 提供商，可完全离线运行（Ollama/LM Studio，无需 API key）
- 6 层认知记忆 + BM25/向量/知识图谱/分层文档推理的 4 通道混合搜索
- PGE 三层架构：Planner(LLM)→Gatekeeper(确定性策略引擎)→沙箱化 Executor
- SQLCipher(AES-256) 全库静态加密、审计链、GDPR 合规声明

## 适用场景

- 在本机运行私有 AI 助手，通过 CLI/Telegram/Discord 等对话并执行任务
- 自动化浏览器操作、桌面控制与文件/shell 任务
- 用知识库与文档分析做个人研究与知识管理

## 场景标签

`AI 助手` `浏览器自动化` `GUI 自动化` `知识库管理` · 领域:效率与自动化

## 证据(README 行号)

> L39: **In plain terms:** Cognithor is an AI assistant that lives entirely on your computer. You talk to it through your 
> L43: What makes it different from other local AI tools is that Cognithor is not just a chatbot. It is an agent operating
> L93: > **Cognithor** is a fully local, Ollama/LM Studio-powered, autonomous agent operating system that acts as your per

## 星数曲线

```mermaid
xychart-beta
    title "Alex8791-cyber/cognithor 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 156 --> 159
    line [158, 157, 157]
```

2026-10-18 158 → 2026-10-26 157（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `42aa9e2ff997` · [字段定义](../../DATASET.md)*
