# Kerneta/daidocs

⭐ 54 · Python · Apache-2.0 · 推送 2026-10-07 · [GitHub](https://github.com/Kerneta/daidocs) · [官网](https://daidocs.com) · 组织维护 · 中文 README

**面向 AI 助手的开放纯文本长期记忆文件格式（.dai/.cai）**

将 AI 助手的长期记忆落为本地纯文本文件：.dai 存文档与会话历史，.cai 用 tree-sitter 确定性构建 10 种语言的代码图谱，ask 路由器决定由哪一层回答问题。文件可用 grep/git/任意编辑器读取，模型无关，由廉价观察者模型写入、任意模型读取。通过内置 MCP server 接入 Claude Code、Claude Desktop、Cursor、Windsurf、Codex 等工具，npx daidocs setup 一条命令安装并自动配置。Node 18+/Python 3.10+ 两个引擎各自独立安装。README 附带基准结果及 sha256 证据清单。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- .dai/.cai 双格式覆盖会话历史与代码图谱，ask 路由分发问题
- 纯文本、本地优先，任意模型与 grep/git 可读，写入一次多模型复用
- 内置 stdio MCP server，自动检测配置 Claude Code、Cursor、Windsurf 等工具
- tree-sitter 确定性构建代码图谱，无模型调用与 API 成本

## 适用场景

- 让 Claude Code、Cursor 等编码助手跨会话记住项目决策与代码结构
- 本地保存并检索长期对话历史，不想被单一厂商服务绑定
- 用极小 token 预算回答需要长历史的回忆问题

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L27:  MCP: server included
> L134: **Any MCP-capable runtime, too.** The server is a plain stdio MCP server, so frameworks that speak MCP call `save_

## 星数曲线

```mermaid
xychart-beta
    title "Kerneta/daidocs 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-31"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-31 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1ea34e109255` · [字段定义](../../DATASET.md)*
