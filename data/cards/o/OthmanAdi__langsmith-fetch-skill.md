# OthmanAdi/langsmith-fetch-skill

⭐ 28 · MIT · 推送 2026-04-06 · [GitHub](https://github.com/OthmanAdi/langsmith-fetch-skill) · 个人维护

**Claude Code 技能：在终端拉取 LangSmith 追踪调试 LangChain/LangGraph agent**

面向 Claude Code 的 SKILL.md 格式调试技能：安装后 Claude 监听调试类提问，自动调用 langsmith-fetch CLI 从 LangSmith Studio 拉取执行追踪，分析错误、执行耗时、token 用量、工具调用与 LTM 内存操作，并支持导出调试会话。需配置 LANGSMITH_API_KEY 与项目名。技能经 npx skills add 安装（兼容 Cursor、Codex、Gemini CLI 等 40+ 支持 Agent Skills 规范的 agent），CLI 依赖经 pip 安装，版本 0.1.0，状态为积极开发中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 自动拉取并分析 LangSmith 执行追踪（traces/trace/threads/config 四条命令）
- 错误检测、性能与 token 成本分析、瓶颈识别
- 调试会话导出与多 agent 编排决策调试
- 兼容 Claude Code、Cursor、Codex、Gemini CLI 等 40+ agent

## 适用场景

- 让 Claude Code 直接回答'我的 agent 为什么慢/出错了'
- 排查 LangChain/LangGraph agent 的工具调用与内存操作
- 导出调试会话留档复查

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: Debug LangChain and LangGraph agents by fetching execution traces from LangSmith Studio directly in your terminal us
> L15: This Claude Code skill teaches Claude how to debug your LangChain and LangGraph agents by automatically fetching an
> L252: - **Category:** AI Observability & Debugging

## 星数曲线

```mermaid
xychart-beta
    title "OthmanAdi/langsmith-fetch-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `c3d603fe7423` · [字段定义](../../DATASET.md)*
