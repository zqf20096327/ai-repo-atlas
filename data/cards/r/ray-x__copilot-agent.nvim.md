# ray-x/copilot-agent.nvim

⭐ 18 · Lua · NOASSERTION · 推送 2026-06-03 · [GitHub](https://github.com/ray-x/copilot-agent.nvim) · 个人维护

**Neovim 内的 GitHub Copilot 代理式编码插件（Go 桥接官方 SDK）**

Neovim 插件，通过 Go 服务嵌入官方 Copilot Go SDK，提供带工具执行的代理循环（文件读写、终端执行、网页搜索）、ask/plan/agent/autopilot 四种模式、分级权限管理、跨 Neovim/VS Code/CLI 的会话持久化、状态回退、LSP 代码动作（fix/test/explain）及 .github/agents 与 .github/skills 配置发现。仅支持 Copilot（或自带 key），不支持多 provider。安装方式为插件管理器加载后用 :CopilotAgentInstall 下载预编译二进制，需 Neovim 0.12+、curl 与 Copilot CLI 运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 官方 Copilot Go SDK 驱动的完整代理循环（文件/终端/网页工具）
- 四级监督模式与会话感知的权限管理
- 跨 Neovim/VS Code/CLI 的会话持久化与状态回退
- LSP code_action 触发的 fix/test/explain 及自定义 agent/skill 发现

## 适用场景

- 在 Neovim 中让 Copilot 自主完成编码任务（编辑文件、跑命令、搜网页）
- 通过权限模式控制代理的自主程度
- 在 Neovim 与 VS Code 间延续同一会话继续工作

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: GitHub Copilot's agentic runtime, natively in Neovim. A lightweight Go bridge to the official SDK with native tool e
> L14: |**Autonomous SDK Loop**|Native file I/O, terminal execution, and web search via official Go SDK.|

## 星数曲线

```mermaid
xychart-beta
    title "ray-x/copilot-agent.nvim 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `70900dbe07e9` · [字段定义](../../DATASET.md)*
