# hyparam/hyllama

⭐ 51 · JavaScript · MIT · 推送 2026-09-29 · [GitHub](https://github.com/hyparam/hyllama) · 组织维护

**JavaScript 解析 llama.cpp GGUF 文件元数据的无依赖库**

面向 JavaScript/TypeScript 开发者的 GGUF 文件解析库：读取 llama.cpp 生态 .gguf 模型文件的元数据与张量信息，支持 Node.js 与浏览器环境。核心机制是部分加载——通过 HTTP Range 请求只获取文件头部字节即可解析元数据，无需下载整个大文件。自 2023 年起零依赖，MIT 许可，npm 安装。附带 index.html 拖拽解析示例。局限：仅解析元数据，不运行模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 解析 GGUF 文件的元数据与张量信息
- 无需加载整个文件，支持 Range 请求只取头部字节
- Node.js 与浏览器双环境可用
- 2023 年起零依赖

## 适用场景

- 在网页中展示用户拖入的 GGUF 模型文件元数据
- 批量读取 Hugging Face 上 GGUF 模型的量化与架构信息
- 在工具链中校验 GGUF 文件结构

## 场景标签

 · 领域:LLM 工具链/文件格式解析

## 证据(README 行号)

> L12: Javascript parser for llama.cpp gguf files.
> L14: This library makes it easy to parse metadata from GGUF files.

## 星数曲线

```mermaid
xychart-beta
    title "hyparam/hyllama 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 50 --> 52
    line [51, 51]
```

2026-10-18 51 → 2026-10-28 51（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `cf5e2c655cb7` · [字段定义](../../DATASET.md)*
