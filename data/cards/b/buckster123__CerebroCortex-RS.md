# buckster123/CerebroCortex-RS

⭐ 15 · Rust · 推送 2026-08-09 · [GitHub](https://github.com/buckster123/CerebroCortex-RS) · [官网](http://www.apexaurum.no) · 个人维护

**给 AI agent 的脑类比记忆系统（纯 Rust 单二进制+SQLite）**

CerebroCortex 的纯 Rust 移植版，为 AI agent 提供记忆存取：通过 MCP-over-stdio 暴露 67 个工具（remember/recall/dream 等），agent 经任意 MCP 客户端接入。内部含九个以脑区命名的引擎，召回混合向量相似度、ACT-R 激活、FSRS 可提取性与 salience；夜间 dream 周期做重放、模式抽取、剪枝与 REM 重组，程序性记忆按胜负账本竞争择优。另含视觉回路（Ollama/Anthropic 分层描述+CLIP 索引）、文件摄取与多 agent 范围隔离。编译为单个二进制，SQLite 为唯一数据源，无模型时 23 MB RSS 运行；三个 dream 相位需 LLM（ANTHROPIC_API_KEY），缺失时自动跳过。零 Python 运行时，可从 Python 版数据迁移。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 召回混合向量相似度 + ACT-R 激活 + FSRS 可提取性 + salience 四因子打分
- 8 相位 dream 周期（3 相位用 LLM，缺 key 时跳过）与 Wilson 下界的技能竞争选择
- 67 个 MCP 工具经 stdio 提供，SQL 层强制多 agent 可见性范围与审计日志
- 单二进制 + 单 SQLite 文件，无模型 23 MB RSS，可从 Python 版迁移

## 适用场景

- 给我的 MCP agent 加上有遗忘曲线和巩固机制的记忆层
- 多 agent 共享一个记忆库且保持私有记忆隔离
- 离线/低配设备（树莓派）上运行轻量记忆系统
- 从 Python 版 CerebroCortex 迁移现有数据

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L5: **A brain-analogous memory system for AI agents — pure Rust, one binary, one SQLite file.**
> L15: Your agent calls `remember` and `recall` over MCP. Underneath, nine engines named after the brain regions they imit
> L82:   cerebro-mcp/    # MCP-over-stdio binary — the agent-facing drop-in (67 tools)

## 星数曲线

```mermaid
xychart-beta
    title "buckster123/CerebroCortex-RS 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b1dbc27490c2` · [字段定义](../../DATASET.md)*
