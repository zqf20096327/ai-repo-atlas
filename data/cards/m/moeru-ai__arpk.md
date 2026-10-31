# moeru-ai/arpk

⭐ 42 · TypeScript · MIT · 推送 2026-01-08 · [GitHub](https://github.com/moeru-ai/arpk) · [官网](https://www.npmjs.com/package/arpk) · 组织维护

**用 LLM 做翻译的 CLI 与 DeepLX 兼容 API 服务**

ARPK 是基于 Node.js 的翻译工具，将 LLM 用作翻译引擎，支持大多数 OpenAI 兼容 API（默认 Ollama + llama3.2）。提供 CLI 翻译命令（arpk translate）与 serve 模式：后者在 1188 端口提供 /translate、/api/v1/translate、/api/v2/translate 端点，兼容 DeepLX API。可通过环境变量配置模型、base url、API key、seed、系统提示词与访问令牌（仅 Bearer Auth）。安装方式为 npm 全局安装或 npx，另提供 Docker 与 docker-compose 镜像。

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

- CLI 翻译命令支持 stdin 管道输入
- serve 模式提供 DeepLX 兼容的 /translate API
- 支持任意 OpenAI 兼容 API，默认 Ollama（llama3.2）
- ARPK_TOKEN Bearer 认证保护 API

## 适用场景

- 命令行快速翻译文本
- 部署自托管翻译 API 替换 DeepLX 调用方
- 接入本地 Ollama 模型做离线翻译服务

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L3: > LLM as your translator, with DeepLX-compatible API.
> L9: ARPK supports most OpenAI-compatible APIs, Ollama is used here as an example (and is also the default):
> L33: arpk translate --from "EN-US" --to "ZH" --input "Hello, World!"

## 星数曲线

```mermaid
xychart-beta
    title "moeru-ai/arpk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b606e2e830ac` · [字段定义](../../DATASET.md)*
