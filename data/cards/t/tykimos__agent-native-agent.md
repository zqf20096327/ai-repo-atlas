# tykimos/agent-native-agent

⭐ 128 · HTML · AGPL-3.0 · 推送 2026-10-15 · [GitHub](https://github.com/tykimos/agent-native-agent) · [官网](https://github.com/tykimos/ana-starter) · 个人维护 · 中文 README

**自托管看板应用：以编码 agent 为运行时，边用边改**

ANA 是一个自托管的 agent-native 应用基座：用户通过浏览器查看实时看板并与编码 agent（Claude Code 或 Codex CLI）对话，agent 作为后端在批准后直接改写应用自身代码并使看板热更新，无需 PR 或发布流程。机制上无桥接层、不用 MCP：浏览器经服务器将文本注入 tmux 面板，300ms 循环经 SSE 回传会话；agent 提交前后对比提案，批准后应用 diff。基座内置任务/日历/笔记三个区域与基于 NodeRel+SQLite 的关系图，agent 可从笔记生成本体与知识图谱并导出 OWL。需 Node≥24、tmux 与编码 agent CLI，支持 Codespaces 浏览器运行与 WSL 安装脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 编码 agent 即运行时：批准提案后改写应用代码并热更新
- 无桥接无 MCP：浏览器→服务器→tmux 注入，SSE 回传 append-only 会话账本
- 聊天直接渲染自 Claude Code/Codex 的结构化日志，含提问卡片与权限菜单
- NodeRel 关系图 + agent 生成本体与知识图谱，可导出 OWL Turtle

## 适用场景

- 用对话方式让编码 agent 按需扩展我正在使用的自托管应用
- 在手机/浏览器上看板式管理任务、日历、笔记并让 agent 协作
- 从自己的笔记任务数据生成本体与知识图谱

## 场景标签

 · 领域:开发者工具/Agent 运行时

## 证据(README 行号)

> L20: **ANA is an _Agent‑Native Agent_ for _Agent‑Native Lifestyle_ (ANL).** It is a self‑hosted app you operate by **wat
> L41: 2. **Agent as Runtime** — the agent reads your data, acts, and **rewrites the app's own code** when asked. Inferenc
> L55: There is **no bridge and no MCP**. The browser posts to the server, the server injects the text straight into the t

## 星数曲线

```mermaid
xychart-beta
    title "tykimos/agent-native-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 115 --> 129
    line [116, 127, 128]
```

2026-10-18 116 → 2026-10-22 128（+12）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `f944d4f3bc32` · [字段定义](../../DATASET.md)*
