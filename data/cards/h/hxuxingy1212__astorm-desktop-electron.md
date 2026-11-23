# hxuxingy1212/astorm-desktop-electron

⭐ 4 · Rust · MIT · 推送 2026-10-21 · [GitHub](https://github.com/hxuxingy1212/astorm-desktop-electron) · 个人维护 · 中文 README

**本地优先的跨平台桌面 AI 智能体客户端，含沙箱与 MCP**

基于 Electron + Vue 3 + Rust（napi-rs）的桌面 AI 智能体客户端，模型可读写文件、执行 Shell、操作 Git、检索网页、驱动内置浏览器、生成与编辑 Office 文档、管理邮件与定时任务，每步受权限审批与分层沙箱（macOS Seatbelt、Windows AppContainer 等）约束。支持 OpenAI 兼容 Chat Completions / Responses / Anthropic Messages 协议接入多模型供应商，提供 MCP 扩展、插件系统、长期记忆与多智能体协作。同一 Rust 内核可编译为无头服务（HTTP+SSE+WS），配套 CLI、Web UI 与 Docker 单用户容器。源码构建需 Node.js ≥20.19、pnpm 10 与 Rust ≥1.85 及各平台编译工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层沙箱与默认拒绝策略，拦截/批准/执行全程留痕
- 多模型供应商接入：OpenAI 兼容、Responses、Anthropic Messages
- MCP（stdio 与 HTTP/Streamable HTTP）与 iframe 沙箱插件系统
- 桌面与云端共用同一 Rust 内核，支持 Docker 单用户容器

## 适用场景

- 在本地桌面让 AI 代为读写文件、执行 Shell 与 Git 操作
- 通过审批与沙箱机制控制智能体的文件与网络权限
- 用 Docker 容器在服务器端运行无头智能体服务并经 Web UI 访问

## 场景标签

`AI 助手` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: Astorm Agent 是一个**本地优先**的跨平台桌面 AI 智能体客户端。它把大模型放进一个可操作的桌面工作台：模型可以读写文件、执行 Shell、操作 Git、检索网页、驱动内置浏览器、生成和编辑 Office 文档、管理
> L19: - 多模型供应商：OpenAI 兼容 Chat Completions、Responses、Anthropic Messages；文本与图片输入；重试、限流、熔断与结构化输出。
> L39: - **分层沙箱**：策略层（文件/网络/危险命令）→ 平台强制层（macOS Seatbelt、Windows AppContainer + Job Object + WFP）→ 会话策略层（Plan / Execute / A

## 星数曲线

```mermaid
xychart-beta
    title "hxuxingy1212/astorm-desktop-electron 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-23"]
    y-axis "stars" 3 --> 5
    line [4, 4]
```

2026-10-23 4 → 2026-11-23 4（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `890bcc4cdce8` · [字段定义](../../DATASET.md)*
