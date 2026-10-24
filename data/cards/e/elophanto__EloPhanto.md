# elophanto/EloPhanto

⭐ 106 · Python · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/elophanto/EloPhanto) · [官网](https://elophanto.com) · 组织维护

**持久身份的自主 AI agent：可自写工具、驱动浏览器与运营业务**

本地或托管运行的自主 agent，具备跨会话持久身份：价值观、信念与能力数据存于 SQLite 并以可读文件呈现。通过 287 个工具访问真实 Chrome 浏览器、shell、文件系统、邮箱日历与任意 MCP 服务器，缺少工具时可自行编写。内建基于结果度量的能力信心分数、后台自主循环、分级权限（ask_always/smart_auto/full_auto）与十八个始终需确认的 CRITICAL 操作。支持以公司为实体运营外展与销售流程。运行需 Python 3.12+、Node.js 24+ 与一个 LLM 提供商。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 跨会话持久身份，存于 SQLite 并可读 diff
- 287 个工具：真实浏览器、shell、文件、邮箱、REST、MCP
- 基于实测结果的逐能力信心分数与分级权限门控
- 缺少工具时自行编写，附影响分析与 git 回滚

## 适用场景

- 夜间无人值守时让 agent 推进目标并在关键操作前请求批准
- 把一项业务交给 agent 以 learning→trial→operating 分级运营
- 审计 agent 的工具轨迹、开销账本与自我绩效文件

## 场景标签

`AI 助手` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L10: EloPhanto is an autonomous agent with a persistent identity. It drives a real Chrome profile, your files, the shell
> L58: It reaches the world through 287 tools: a real browser (47 of them, driving your Chrome profile and its logged-in s
> L78: Needs Python 3.12+, uv, Node.js 24+, and one LLM provider (OpenRouter is the easiest; Ollama keeps it entirely loca

## 星数曲线

```mermaid
xychart-beta
    title "elophanto/EloPhanto 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-24 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ace0188db41b` · [字段定义](../../DATASET.md)*
