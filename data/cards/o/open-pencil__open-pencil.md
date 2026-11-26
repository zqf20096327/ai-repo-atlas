# open-pencil/open-pencil

⭐ 10,114 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/open-pencil/open-pencil) · [官网](https://openpencil.dev) · 个人维护

**开源设计编辑器：读写 .fig 文件并内置 AI 助手**

开源设计编辑器，可读写原生 Figma（.fig）与 .pen 设计文件，桌面端经 Tauri v2 打包（约 15 MB），也可作为 PWA 在浏览器运行。内置 AI 聊天助手，通过 100+ 工具创建和修改画布节点，采用 BYOK 方式接入各家模型 API，无需后端与账号。提供 headless CLI（检查/XPath 查询/导出/lint/tokens 提取）、Figma Plugin API 兼容的 eval 脚本、MCP 服务器、Vue SDK，并支持 WebRTC 点对点实时协作。桌面版每日发送一次匿名 ping。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 读写原生 Figma .fig 文件，支持导出 PNG/SVG/PDF/PPTX/JSX 等格式
- 内置 AI 助手：100+ 工具创建与修改节点，BYOK 接入多供应商
- headless CLI + XPath 查询 + Figma Plugin API eval + MCP 服务器
- WebRTC 点对点实时协作，无需服务器与账号

## 适用场景

- 在没有 Figma 账号的环境下打开和编辑 .fig 设计文件
- 通过命令行批量检查、转换、导出设计文档
- 让 Claude Code 等 agent 通过 MCP 检查和修改设计稿
- 团队之间点对点共享链接进行实时协作设计

## 场景标签

 · 领域:设计工具

## 证据(README 行号)

> L9: Open-source design editor. Opens `.fig` and `.pen` design files, includes built-in AI, and ships as a programmable t
> L34: - **AI builds designs** — describe what you want in chat, 100+ tools create and modify nodes. Bring your own key fo
> L41: - **Vue SDK for custom editors** — headless components and composables for embedding OpenPencil into other apps or 

## 星数曲线

```mermaid
xychart-beta
    title "open-pencil/open-pencil 星数(近 27 点)"
    x-axis ["2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 9129 --> 10203
    line [9218, 9239, 9265, 9299, 9325, 9376, 9433, 9471, 9507, 9522, 9239, 9706, 9755, 9788, 9808, 9831, 9849, 9863, 9889, 9912, 9938, 9962, 9979, 9998, 10024, 10065, 10114]
```

2026-10-24 9,218 → 2026-11-26 10,114（+896）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `3fc2ecd4fe2a` · [字段定义](../../DATASET.md)*
