# Mnemosyne-OS/Mnemosyne-Neural-OS

⭐ 20 · TypeScript · MIT · 推送 2026-10-27 · [GitHub](https://github.com/Mnemosyne-OS/Mnemosyne-Neural-OS) · [官网](https://mnemosyne-os.io) · 组织维护

**本地优先的 AI 记忆操作系统：统一管理文件与对话形成可检索记忆**

基于 Electron/React 的桌面应用（Windows/macOS/Linux），将用户文件与对话转化为存储在本机加密 Vault 中的可检索记忆，供用户接入的任意模型读取。包含多引擎架构：嵌入链（云端/本地 ONNX/Ollama）、自适应 RAG、语义分类 Spine、闲置期记忆固化 Dream State、本地语音 STT/TTS、图像记忆引擎 Theia，以及 FGAC 细粒度访问控制与 400 个 Zod 校验 IPC 通道。提供 MCP 包让 Claude Code/Cursor 等编码 agent 接入记忆。声明部分功能仍处实验阶段，许可通过本地 Web3 钱包（Engramm License）驱动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 记忆 Vault 本地存储，支持 AES-256 静态加密与 FGAC 访问控制
- 多引擎架构：嵌入链/自适应 RAG/Spine 分类/Dream State 固化/本地 STT-TTS
- npx @mnemosyne_os/mcp 连接 Claude Code、Cursor、Claude Desktop
- 7 语言界面，语言切换会重新选择推荐的嵌入模型

## 适用场景

- 让多个 AI 助手跨会话共享我的本地记忆
- 给我的编码 agent（Claude Code/Cursor）挂载可审计的记忆库
- 在本机集中管理哪些内容可进入、移动或移出 AI 记忆

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L1: Mnemosyne OS Infinity Edition. Your memory. Your machine. Your rules. A sovereign, local-first memory OS the relatio
> L91: **Mnemosyne OS is the control surface for your memory, your agents and your
> L138: The reference application of the ecosystem: a **local-first AI Operating System** that

## 星数曲线

```mermaid
xychart-beta
    title "Mnemosyne-OS/Mnemosyne-Neural-OS 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d3c3b60041f6` · [字段定义](../../DATASET.md)*
