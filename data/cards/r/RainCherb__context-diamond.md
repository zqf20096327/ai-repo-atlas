# RainCherb/context-diamond

⭐ 20 · Python · MIT · 推送 2026-10-23 · [GitHub](https://github.com/RainCherb/context-diamond) · [官网](https://github.com/RainCherb/context-diamond) · 个人维护

**面向 LLM/编码代理的可审计上下文压缩与交接工具包**

面向在编码代理、OpenCode、聊天 UI 与 RAG 管道间切换的开发者的确定性上下文压缩工具包：把聊天、日志、issue、文档与仓库状态抽取为结构化胶囊（目标、约束、决策、状态、风险、锚点），支持 CLI、Python API、流式与批量处理，可 diff/merge 胶囊，输出损失报告与解释。默认引擎离线、零运行时依赖、无 API key；可按模型上下文窗口自适应压缩、级联压缩，并可透明拦截 API 消息。附带本地 stdio MCP 服务器接入 OpenCode。通过 pip 从 GitHub 安装，MIT 许可。

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

- 确定性抽取生成结构化上下文胶囊（目标/约束/决策/状态/风险/锚点）
- 损失报告与 ctxd explain 展示分片评分与舍弃原因
- 自适应/级联压缩与 API 前透明拦截中间件
- 本地 stdio MCP 服务器提供 12 个 OpenCode 工具，默认离线零依赖

## 适用场景

- 切换编码代理或 LLM 工具时交接工作并保留约束与决策
- 压缩长会话/仓库上下文以降低重复 prompt 成本
- 审计压缩过程中被舍弃的内容

## 场景标签

`Agent 记忆` · 领域:Agent 开发

## 证据(README 行号)

> L12: Context Diamond v0.7.0 is a deterministic context compression and handoff toolkit for
> L23: It is built for developers who switch between coding agents, OpenCode, chat UIs,
> L179: |"I need this in OpenCode."|Run it as a local MCP server.|

## 星数曲线

```mermaid
xychart-beta
    title "RainCherb/context-diamond 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-28 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `424bcbf4f646` · [字段定义](../../DATASET.md)*
