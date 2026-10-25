# ai-forever/gigachat

⭐ 172 · Python · MIT · 推送 2026-10-09 · [GitHub](https://github.com/ai-forever/gigachat) · 组织维护

**Sber GigaChat 大模型 REST API 的官方 Python SDK**

面向接入 GigaChat 大模型 API 的 Python 客户端库，属 GigaChain 生态并支撑官方 LangChain 集成包 langchain-gigachat。覆盖同步/异步对话补全、流式输出、嵌入、函数调用、多模态视觉、文件操作、token 计数与 JSON Schema 结构化输出（beta）。提供四种认证方式（OAuth 授权钥、用户名密码、mTLS 证书、访问令牌）及优先级回退机制，支持指数退避自动重试。需配置俄罗斯数字发展部证书链的 CA 信任，Python 3.8-3.13，pip 安装。

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

- 同步/异步 chat completions 与流式 token 生成
- 函数调用、多模态视觉与 JSON Schema 结构化输出（beta）
- 四种认证方式与优先级回退，含 mTLS
- 指数退避自动重试与 Pydantic V2 全类型化模型

## 适用场景

- 在 Python 应用中调用 GigaChat API 获得对话、嵌入等模型输出
- 为 GigaChat 构建带工具调用的 agent
- 通过 langchain-gigachat 在 LangChain 工程中使用 GigaChat

## 场景标签

 · 领域:LLM API 客户端库

## 证据(README 行号)

> L9: Python SDK for the GigaChat REST API — a large language model.
> L11: This library is part of GigaChain and powers langchain-gigachat, the official LangChain integration for GigaChat.

## 星数曲线

```mermaid
xychart-beta
    title "ai-forever/gigachat 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 170 --> 173
    line [171, 172, 172]
```

2026-10-18 171 → 2026-10-25 172（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `43611eada586` · [字段定义](../../DATASET.md)*
