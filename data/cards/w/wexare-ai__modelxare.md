# wexare-ai/modelxare

⭐ 3 · TypeScript · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/wexare-ai/modelxare) · [官网](https://modelxare.com) · 组织维护

**去中心化小模型平台：签名发布、本地校验并在设备/浏览器运行**

由 weXare 开发的去中心化 AI 模型平台。模型以签名 Nostr release 发布，存储于 IPFS、torrent 与 HTTP 镜像，由独立索引器汇成签名目录快照；浏览器应用直接读取 relay 或导入归档到 SQLite WASM+FTS5，逐字节校验后用 wllama 在浏览器内运行 GGUF 模型，并按 System 1 路由器把请求分发到设备上的专用小模型。另有 `pnpm modelxare` 本地运行时，用 llama.cpp 与 ONNX Runtime 跑同一目录，并提供 OpenAI 兼容 API。模型参数量 15M–500M，面向标题、摘要、分类等小任务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模型以签名 Nostr release 发布，存储于 IPFS/torrent/HTTP 镜像，逐字节 SHA-256 校验
- 浏览器内经 wllama 运行 GGUF，SQLite WASM+FTS5 本地搜索
- `pnpm modelxare` 本地运行时提供 OpenAI 兼容 API（/v1/chat/completions 等）
- System 1 路由器（Laya）按任务分发到目录内的专用小模型，支持运行时 LoRA

## 适用场景

- 在浏览器或本机离线运行社区发布的专用小模型
- 为 OpenAI 兼容客户端/Agent 提供本地模型 API
- 无需中心注册表地发布和发现模型版本

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L30: - **Run natively.** `pnpm modelxare` runs the same releases on your own machine with native llama.cpp and ONNX Runt
> L139: - **Native engines.**
> L145: - **The API.**


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `332128286b4e` · [字段定义](../../DATASET.md)*
