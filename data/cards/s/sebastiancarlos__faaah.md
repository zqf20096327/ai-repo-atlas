# sebastiancarlos/faaah

⭐ 13 · Python · MIT · 推送 2026-08-15 · [GitHub](https://github.com/sebastiancarlos/faaah) · 个人维护

**把 AI Agent 订阅复用为 OpenAI 兼容本地服务器的文件代理**

面向已有 AI 编程助手订阅的开发者：FAAAH 在本地 127.0.0.1 启动 OpenAI 兼容 HTTP 服务器，把收到的请求写成队列目录中的 prompt-*.txt 文件；由既有编码 agent（如 Claude Code、opencode）通过 faaah --watch 协调循环读取并写回 response-*.txt，再封装成 OpenAI 格式 JSON 返回调用方。零依赖（仅 Python http.server），308 行代码，支持会话日志回放、自动重试与人工接管回退；可选安装 spaCy 模型提供本地 embeddings。要求所用 agent 支持按提示创建子代理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以纯文本文件协议在 OpenAI 兼容 API 与 AI 编码 agent 之间转发请求/响应
- 零依赖实现（Python http.server），308 行代码
- 会话日志镜像记录所有队列文件与原始请求/响应，便于调试
- 人工接管回退：可直接编辑 response 文件补写答案

## 适用场景

- 复用已付费的 AI 编程助手订阅跑个人项目，避免另购 API key
- 让仅支持 OpenAI API 格式的工具（GraphRAG、LangChain 等）经由本地 agent 处理请求
- 离线/限额时代价下由人工直接编辑响应文件完成请求

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: FAAAH allows you to reuse your AI Agent subscription as a generic
> L18: 3. FAAAH then packages the responses into OpenAI-compatible JSON, and returns
> L173: Filesystem As An AI Handler: an OpenAI-compatible proxy backed by an AI agent working over text files.

## 星数曲线

```mermaid
xychart-beta
    title "sebastiancarlos/faaah 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `0b473bd60f69` · [字段定义](../../DATASET.md)*
