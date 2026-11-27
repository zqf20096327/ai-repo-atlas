# leaningtech/browsercode

⭐ 174 · Svelte · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/leaningtech/browsercode) · [官网](https://browsercode.io) · 组织维护

**在浏览器中运行 AI 编码 CLI 的 WebAssembly 沙箱 IDE**

基于 BrowserPod（多语言 WebAssembly 沙箱）的浏览器端编码环境，完全客户端运行，无需安装、服务器或云端算力。内置 Node.js v22、Rust、Python（预览）、POSIX 风格文件系统及 bash/git/npm 等命令行工具；以未修改形式在浏览器内运行 Claude Code、Codex CLI 和 Pi 三个 AI 编码 CLI，后续计划支持 Antigravity 与 OpenCode。出站网络限于白名单主机（npm registry、GitHub、主要 AI provider API）。提供托管版与自托管路径，支持 iframe 嵌入。限制：不支持原生二进制；Agent 运行需支持 WebAssembly JSPI 的浏览器版本，iOS/iPadOS 暂不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 在浏览器内完全客户端运行 Claude Code、Codex CLI、Pi，无需安装或服务器
- BrowserPod 多语言 WebAssembly 沙箱（Node.js、Rust、Python 预览）与 POSIX 风格文件系统
- 出站网络白名单隔离，覆盖 npm registry、GitHub 与主要 AI provider API
- 支持 Vite/Express/Svelte/Next/Nuxt/React/Vue 框架模板及 iframe 嵌入

## 适用场景

- 不安装任何东西就在浏览器里试用 AI 编码 CLI
- 在沙箱中直接原型化 agent 生成的全栈应用并即时预览
- 把浏览器端编码环境嵌入到自己的网站页面

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L11:  Run AI coding CLIs and frameworks in the browser
> L32: BrowserCode started out as a way to run AI coding CLIs entirely client-side. It's since grown into a full IDE: alon
> L34: BrowserCode 2.0.0 is our latest beta release. It runs a full code editor, development environment, and unmodified v

## 星数曲线

```mermaid
xychart-beta
    title "leaningtech/browsercode 星数(近 23 点)"
    x-axis ["2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27"]
    y-axis "stars" 141 --> 177
    line [144, 145, 147, 148, 149, 150, 151, 152, 153, 144, 158, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 174, 174]
```

2026-10-25 144 → 2026-11-27 174（+30）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `050709860f24` · [字段定义](../../DATASET.md)*
