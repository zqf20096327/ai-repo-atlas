# yantrikos/yantrikdb-hermes-plugin

⭐ 95 · Python · MIT · 推送 2026-10-14 · [GitHub](https://github.com/yantrikos/yantrikdb-hermes-plugin) · [官网](https://yantrikdb.com) · 个人维护

**为 Hermes Agent 提供自维护记忆的 YantrikDB 记忆插件**

以 pip 安装的 Hermes Agent 记忆提供者插件：默认 v0.2.0 起为进程内后端，无需单独服务器、token 或 GPU。通过 yantrikdb_recall/remember 等工具实现记忆存储与召回，附带 why_retrieved 召回解释、conflicts() 矛盾追踪与 resolve_conflict()、重复条目规范化、自调排序（reinforce 强化）与主动记忆卫生（yantrikdb_hygiene）。v0.8 起默认开启自导向循环：发现知识空白→排队任务→向 agent 提供议程。另支持所有者隔离、多 agent 舰队、可挂载的签名知识包（knowledge packs）与工具档案控制（core 7 工具约 1.7k tokens）。非 Hermes 用户可经 MCP 服务器或 Python 导入使用同一引擎。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 进程内后端默认：pip 安装即用，无服务器/token/GPU（约 23 MB，无 torch）
- 矛盾追踪（conflicts/resolve_conflict）与每次召回附带 why_retrieved 解释
- 自导向循环（v0.8 起默认开启）：记忆空白→任务→议程并闭合
- 可挂载的签名知识包与 CI 守护的可复现召回基准（recall@k/MRR）

## 适用场景

- 长会话 coding agent 保留约束不因压缩丢失
- 多平台 Hermes（Telegram/WhatsApp/Discord）按所有者隔离记忆
- 共享 group bot 中让每个用户拥有独立记忆命名空间
- 多 agent 部署共享语料或查看舰队记忆状态

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L14: > **YantrikDB as a memory provider for Hermes Agent.** Self-maintaining memory — canonicalizes duplicates, surfaces
> L25: hermes memory setup                   # → select "yantrikdb"
> L30: Not using Hermes? The same engine ships as an MCP server (yantrikdb-mcp) for Claude Code, Cursor, and other MCP-cap

## 星数曲线

```mermaid
xychart-beta
    title "yantrikos/yantrikdb-hermes-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 94 --> 97
    line [96, 95]
```

2026-10-18 96 → 2026-10-27 95（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `f569157f05a3` · [字段定义](../../DATASET.md)*
