# poloclub/wordflow

⭐ 272 · TypeScript · MIT · 推送 2026-04-07 · [GitHub](https://github.com/poloclub/wordflow) · [官网](https://poloclub.github.io/wordflow/) · 组织维护

**社交化 AI 写作助手：运行提示词、分享提示词社区**

Wordflow 是面向写作用户的 Web 端 AI 助手，支持存储与运行提示词，可调用外部 LLM（如 GPT、Gemini Pro）和本地设备端模型（如 Llama 2、Phi 2，基于 WebGPU 在浏览器运行），并提供温度、模板等自定义参数。社交层面支持发现与分享社区提示词。提供在线版（poloclub.github.io）、macOS/Chrome 的 Web App 保存方式以及 Google Docs 插件（Google Workspace Marketplace 可装）；开发方式为 git clone 后 npm install 并 npm run dev。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时支持外部 LLM（GPT、Gemini Pro）与本地模型（Llama 2、Phi 2）
- 浏览器内通过 WebGPU 运行本地 LLM（需 Chrome，Safari 不支持 WebGPU）
- 提示词存储、运行与社区分享
- 提供 Google Docs 插件与独立 Web App 形态

## 适用场景

- 写作时调用自定义提示词生成/润色文本
- 在 Google Docs 内直接使用 AI 写作辅助
- 与社区分享和发现常用提示词
- 不依赖外部 API、在本地浏览器运行 LLM

## 场景标签

`AI 写作` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L20: Wordflow is a social and customizable AI writing assistant tool! With Wordflow, you can easily write and run AI pro
> L29:  Support multiple on-device LLMs (e.g., Llama 2 and Phi 2)

## 星数曲线

```mermaid
xychart-beta
    title "poloclub/wordflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 271 --> 273
    line [272, 272]
```

2026-10-18 272 → 2026-10-31 272（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `fca1419f7454` · [字段定义](../../DATASET.md)*
