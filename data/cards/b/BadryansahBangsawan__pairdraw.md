# BadryansahBangsawan/pairdraw

⭐ 3 · TypeScript · MIT · 推送 2026-11-21 · [GitHub](https://github.com/BadryansahBangsawan/pairdraw) · 个人维护

**开源设计编辑器：读写 .fig 文件并内置 AI 与编程代理集成**

以 MIT 许可发布的桌面/网页设计编辑器，可读写 Figma `.fig` 与 Pencil `.pen` 文件。AI 聊天面板通过 100+ 工具创建和修改画布节点，用户自带各服务商 API key，或接入本机已装的编码代理（Claude Code、Codex、Gemini CLI 等）；另提供 CLI、MCP 服务器、VS Code 扩展、headless Vue SDK 与可选自托管 Cloud 协作。桌面应用基于 Tauri v2，目前发布 macOS Apple Silicon 构建包，其余平台需从源码构建；无托管网页版。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 读写 .fig 原生 Figma 文件，支持 HTML/CSS 导入为可编辑图层
- AI 聊天面板 100+ 工具直接创建/修改设计节点，BYOK 接入主流服务商
- 提供 CLI、MCP 服务器、VS Code 扩展与 headless Vue SDK 的可编程工具集
- Tauri v2 桌面应用（macOS 安装包约 20 MB），无遥测数据上传

## 适用场景

- 打开和编辑 Figma 设计文件而不依赖 Figma 平台
- 通过对话或编码代理让 AI 在画布上生成设计
- 用 CLI 批量检查、导出、转换设计文件并提取设计令牌
- 通过自托管 Cloud 服务器与团队协作编辑

## 场景标签

 · 领域:设计工具

## 证据(README 行号)

> L6: Open-source design editor. Opens `.fig` and `.pen` design files, includes built-in AI, and ships as a programmable t
> L25: - **AI builds designs** — describe what you want in chat, on Home, or in the prompt at the bottom of the canvas, an
> L30: - **Fully programmable** — headless CLI, XPath queries, Figma Plugin API plus a `pairdraw` API via `eval`, MCP serv

## 星数曲线

```mermaid
xychart-beta
    title "BadryansahBangsawan/pairdraw 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-16 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `ff408a0ad35c` · [字段定义](../../DATASET.md)*
