# fiorastudio/buddy

⭐ 116 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/fiorastudio/buddy) · 组织维护

**给 AI 编程 CLI 养的 MCP 虚拟宠物伴侣，含推理审查与代码反馈**

本地优先的 MCP 服务器，为 Claude Code、Codex、Gemini、Copilot、Cursor 等 MCP 客户端提供跨会话的虚拟宠物伴侣：21 个物种、5 项性格属性、心情系统、XP 升级与本地 SQLite 持久记忆。Guard Mode 从对话中抽取带认识论标记的声明构建有向图，识别 6 种推理模式（未验证假设、无质疑推理链、回声室等）并以宠物口吻提示；每会话声明上限 200、检测预算 30ms、数据 30 天自动清理且无网络代码。一键脚本安装，要求 Node 18+ 与 git。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨客户端 MCP 服务器，状态存本地 SQLite 持久化
- Guard Mode 构建 claim 有向图，识别 6 种推理模式（3 谨慎 + 3 肯定）
- 21 物种 / 5 属性 / 心情 / XP 升级的宠物系统
- 本地运行无网络代码，提供 buddy_forget 清除数据

## 适用场景

- 在 Claude Code / Codex 等 CLI 中养一个跨会话的宠物伴侣
- 让宠物在对话中发现 AI 与自己共同的未验证假设
- 换用不同编程 CLI 时保留同一只宠物与记忆

## 场景标签

 · 领域:开发者工具/AI 编程代理配套

## 证据(README 行号)

> L30: Buddy is a local-first MCP companion that persists across sessions and clients, reacts to your work, and can catch 
> L63: - **Works across clients and chat surfaces.** Buddy is an MCP server, not a one-client hack, and it can ride throug
> L75: |**Cross-client setup**|Claude Code, Codex, Gemini, Copilot, Cursor, and other MCP-capable CLIs|

## 星数曲线

```mermaid
xychart-beta
    title "fiorastudio/buddy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 114 --> 117
    line [115, 116, 116]
```

2026-10-18 115 → 2026-10-24 116（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `dec72d9ccf93` · [字段定义](../../DATASET.md)*
