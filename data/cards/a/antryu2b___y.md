# antryu2b/_y

⭐ 23 · TypeScript · MIT · 推送 2026-05-04 · [GitHub](https://github.com/antryu2b/_y) · 个人维护 · 中文 README

**可视化多 AI Agent 编排看板：30 个部门 Agent 独立分析后综合**

以 Next.js 构建的本地优先 Web 看板，把 AI Agent 组织成 10 层虚拟公司与治理层级（主席—参谋—部门）。输入业务 URL 后，30 个 Agent 按市场、工程、风险、财务等职能独立分析，经跨部门评审与 Skepty 质询后由 Counsely 综合成高管简报，最终由用户决策。支持 Ollama 本地运行或 OpenAI/Anthropic/Google 云端，可按部门混用不同厂商。默认 SQLite，可选 PostgreSQL/Supabase；需 Node.js 18+，本地模式需 Ollama 与 8GB+ 内存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30 个 Agent、10 层楼层的公司化层级与决策管线
- 本地 Ollama 免费运行或云端 OpenAI/Anthropic/Google，可按部门混用
- Agent 独立分析（Byzantine 原则），综合前互不可见对方输出
- 硬件感知安装向导按 RAM/GPU 推荐模型档位

## 适用场景

- 输入公司网址获得多部门的独立业务分析报告
- 用 War Room 与 AI 团队就任意议题开会讨论
- 在 UI 中观察多 Agent 从分析到综合的全流程

## 场景标签

`多智能体` `数据分析` · 领域:Agent 开发

## 证据(README 行号)

> L18: _y makes agent work **visible**. See who's analyzing what, how reports flow between functions, where agents disagre
> L24: Connect your business URL and _y's agents go to work:
> L348: Business analysis (SEO, risk, market positioning), strategic planning, content strategy, technical audits. Connect

## 星数曲线

```mermaid
xychart-beta
    title "antryu2b/_y 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `4cda5a51def4` · [字段定义](../../DATASET.md)*
