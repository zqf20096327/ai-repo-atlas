# arifszn/seemore

⭐ 21 · TypeScript · MIT · 推送 2026-10-26 · [GitHub](https://github.com/arifszn/seemore) · [官网](https://arifszn.github.io/seemore) · 个人维护

**零配置 Markdown 文档渲染工具：把现有文件夹变文档站点**

面向已有 Markdown 文件夹（含 AI 生成的笔记/规格/README）的文档站点工具：无需脚手架与配置文件，npx seemore 即可在 localhost 渲染文件夹为站点，文件增删改实时同步更新。提供 macOS/Windows/Linux 桌面应用（含集成终端）、VS Code 兼容编辑器扩展、seemore build 静态导出、单页自包含 HTML 导出、构建时加密的密码保护、静态全文搜索、GFM/Mermaid/D2/MDX 支持与 12 套主题。底层基于 fumadors/Shiki/Vite。另提供 SKILL.md 格式的 agent 技能，供 Claude Code、Codex、Cursor 等 AI 代理调用完成配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 零配置：指向任意现有 Markdown 文件夹即渲染，不移动文件
- 桌面应用（macOS/Windows/Linux）与 VS Code 系编辑器扩展
- seemore build 静态导出与构建时加密的密码保护（无服务器）
- 内置静态全文搜索、Mermaid/D2/MDX、12 套主题

## 适用场景

- 把 AI 代理生成的批量 Markdown 笔记/规格直接变成可浏览站点
- 让 AI 代理通过 seemore 技能自动搭建文档站点
- 将项目文档静态导出并部署到任意主机，可加密码保护

## 场景标签

 · 领域:开发者工具/文档

## 证据(README 行号)

> L34: **seemore** points at that folder and renders it as a real site. Other docs frameworks need a project first: a scaf
> L52: npx seemore   # renders this folder at http://localhost:4040
> L63: ### Claude Code (Plugin Marketplace)

## 星数曲线

```mermaid
xychart-beta
    title "arifszn/seemore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `70300bc4fab9` · [字段定义](../../DATASET.md)*
