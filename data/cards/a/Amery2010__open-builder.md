# Amery2010/open-builder

⭐ 93 · TypeScript · GPL-3.0 · 推送 2026-08-28 · [GitHub](https://github.com/Amery2010/open-builder) · [官网](https://builder.u14.app) · 个人维护 · 中文 README

**通过自然语言对话生成可运行 Web 应用的桌面端 AI 生成器**

桌面优先（Tauri，macOS/Windows/Linux）的 AI Web 应用生成器，兼有浏览器界面。用户用自然语言描述需求，AI 通过 Tool Call 循环在内存文件系统中创建、修改、删除文件，Sandpack 提供实时预览；支持 20+ 前端框架模板、项目快照回滚、健康检查、上下文压缩、Plan Mode 与只读子代理。内置 OpenAI Responses、Anthropic、Google 原生适配器及 OpenAI 兼容端点（如 Ollama）。API Key 存于浏览器本地存储；本地 CLI 运行时支持 Codex，Claude CLI 适配器目前为不支持状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成完整项目结构，AI 用 patch_file 精确修改文件
- 20+ 框架模板（React/Vue/Svelte/Angular/SolidJS/Astro 等）
- 项目快照历史、diff 查看与回滚；/health 健康检查
- 支持远程 HTTPS MCP 与桌面端 stdio MCP（逐调用审批）

## 适用场景

- 用自然语言描述想法，快速生成可运行的 Web 应用
- 在生成过程中实时预览、修改并导出 ZIP 项目
- 通过 Plan Mode 与子代理协作进行代码审查与迭代

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L18: Open Builder is a desktop-first AI web app generator with a browser-compatible interface. Simply describe the appli
> L24: > Native adapters are included for OpenAI Responses, Anthropic, and Google, plus OpenAI-compatible endpoints such a

## 星数曲线

```mermaid
xychart-beta
    title "Amery2010/open-builder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 92 --> 94
    line [93, 93]
```

2026-10-18 93 → 2026-10-31 93（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ebafc1de88a3` · [字段定义](../../DATASET.md)*
