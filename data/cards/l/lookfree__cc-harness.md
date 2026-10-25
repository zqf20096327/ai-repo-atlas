# lookfree/cc-harness

⭐ 49 · TypeScript · MIT · 推送 2026-08-06 · [GitHub](https://github.com/lookfree/cc-harness) · 个人维护 · 中文 README

**给 Claude Code 用户的桌面观测工作台：可视化子代理拓扑与成本**

基于 Electron 的开源桌面工作台，面向 Claude Code 用户，提供配置、调试、观测与编排能力：实时解析本地 session jsonl 渲染 5 层子代理调用树（含节点延迟、token 成本、嵌套深度）、Hook 沙箱试运行、按 skills/subagents/MCP/plugins 分桶的 token 成本拆解与重定价对比、后台任务与循环监控、自动记忆 diff、三层来源配置审计。只读取本地 ~/.claude 与项目 .claude 目录，不上传数据，不修改对话。源码构建需 Node.js 18+ 与已安装的 Claude Code CLI。

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

- 实时追踪 session jsonl 渲染 5 层子代理/工作流调用拓扑
- Hook 沙箱以模拟输入试运行，环境隔离不暴露凭据
- token 成本按 skills/subagents/MCP/plugins/基础会话分桶并可点击下钻到具体消息
- 聚合 ScheduleWakeup 事件的循环与后台任务监控及 MEMORY.md 变更 diff

## 适用场景

- 调试卡住的多子代理工作流，定位停滞分支
- 分析会话 token 成本构成并评估模型重定价的节省金额
- 在移交项目前审计三层来源（user/project/plugin）的配置覆盖关系

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L7: **An open-source desktop workbench for Claude Code: configure · debug · observe · orchestrate**
> L22: - **Live subagent call tree** — tails session jsonl in real time and renders the 5-level subagent/workflow graph wi
> L47: Not a chat client, not a CLI replacement. claudia replaces the CLI's interaction surface; CC Harness does not touch

## 星数曲线

```mermaid
xychart-beta
    title "lookfree/cc-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-25 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `d874375196d7` · [字段定义](../../DATASET.md)*
