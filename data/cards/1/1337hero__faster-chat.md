# 1337hero/faster-chat

⭐ 175 · JavaScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/1337hero/faster-chat) · [官网](https://www.fasterchat.ai) · 个人维护

**自托管多供应商 AI 聊天界面，支持云端与本地离线模型**

基于 Preact + Hono + Bun 的自托管聊天界面，面向个人与团队：内置 17 个供应商（OpenAI/Anthropic/Google/Groq/DeepSeek 等），并可通过 models.dev 自动发现 50+ 供应商，也支持 Ollama、LM Studio、llama.cpp 完全离线运行。功能含流式对话、跨对话记忆、Brave 网络搜索、图像上传与生成、语音输入输出、多用户认证与白标。会话存于服务端 SQLite，API 密钥加密存储。处于维护模式，明确不做 RAG、插件系统、移动端等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 17 个内置供应商 + 50+ 自动发现，支持 Ollama/LM Studio/llama.cpp 离线运行
- 跨对话记忆系统（三级控制、异步提取、用户隔离）
- 服务端 SQLite 存储与加密 API 密钥存储
- 多用户角色认证（admin/member/readonly）与白标定制

## 适用场景

- 部署一个自己掌控数据的私有 AI 聊天界面
- 在管理面板中直接拉取 Ollama 模型，无需 CLI
- 为团队/组织提供带用户管理的统一 LLM 入口

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L31: > **A blazingly fast, privacy-first chat interface for AI that works with any LLM provider—cloud or completely offl
> L33: Connect to OpenAI, Anthropic, Google, Groq, Mistral, xAI, DeepSeek, and more—or run completely offline with Ollama,
> L43: - 🤖 **17 built-in providers** (plus 50+ more auto-discoverable via models.dev): OpenAI, Anthropic, Google, Google V

## 星数曲线

```mermaid
xychart-beta
    title "1337hero/faster-chat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 174 --> 176
    line [175, 175]
```

2026-10-18 175 → 2026-10-29 175（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `6b7e09e42898` · [字段定义](../../DATASET.md)*
