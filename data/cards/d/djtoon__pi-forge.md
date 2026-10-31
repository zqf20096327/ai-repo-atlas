# djtoon/pi-forge

⭐ 14 · TypeScript · MIT · 推送 2026-10-05 · [GitHub](https://github.com/djtoon/pi-forge) · 个人维护

**面向开发者的 agent harness 生成器：访谈后定制专属 AI agent**

基于 pi 构建的 agent harness 生成工具：通过访谈了解用户工作，为其生成含专用工具、系统提示、护栏、主题、logo 与领域视图（3D 分子查看器、图表、表格等）的定制 agent。生成的 harness 可在浏览器 UI、终端、headless（JSON 事件流/RPC）中运行，或经 Bun 打包为无需 Node 的独立程序分发。以 harness.yaml 为唯一事实源，生成文件手改会被检测拒绝；支持按 harness 管理凭证、技能（SKILL.md）、MCP 服务器接入、沙箱模式与定时任务。需 Node.js 22.18+、Git 与模型供应商 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 访谈→工具集→spec→生成的 harness 定制流程
- 同一 harness 支持 web/终端/headless/独立程序四种运行形态
- harness.yaml 为源，custom/ 目录存用户扩展，生成文件手改被拒绝
- MCP 服务器接入、沙箱策略、定时任务与按模型用量统计

## 适用场景

- 为自己的领域工作流（如化学研究、3D 打印规划）生成定制 AI agent
- 把构建好的 agent 打包成 zip 分发给无需 Node 的使用者
- 通过 Add to harness 页面持续为现有 agent 增加工具、视图与技能

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5: **pi-Forge is an agent harness that builds agent harnesses**, on top of pi.
> L7: Tell it about your work. It interviews you, then generates a custom agent for that work: specialized tools, a system
> L38: Then describe what you need, for example *"build me a harness for planning 3D prints"* or *"I want an agent that he

## 星数曲线

```mermaid
xychart-beta
    title "djtoon/pi-forge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8504fef029be` · [字段定义](../../DATASET.md)*
