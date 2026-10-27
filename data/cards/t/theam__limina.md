# theam/limina

⭐ 42 · Python · Apache-2.0 · 推送 2026-10-26 · [GitHub](https://github.com/theam/limina) · 组织维护

**给研究/工程团队的自主研究运行时：让 AI agent 假设-实验-迭代**

自主研究协调层：用户定义带可度量目标的研究任务，Limina 驱动 Codex 或 Claude Code 引擎执行假设→实验→发现→决策的证据链循环，并保留完整可审计的证据记录。提供两种运行方式：Docker 单容器托管运行时（含 CLI/REST/WebSocket/MCP 接口、凭据与密钥管理、执行恢复）和几乎无基础设施的项目模板路径。适用于检索质量优化、生产回归排查、技术方案比较等可评估场景。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Hypothesis → Experiment → Finding → Decision 证据链循环
- 托管运行时：单容器管理项目、凭据、执行循环与恢复，支持 CLI/REST/WebSocket/MCP
- 项目模板路径：无服务器，基于 Markdown/Git 与 kb/ 文件知识库
- 密钥加密写-only、运行事件脱敏、资源轮换触发受控重启

## 适用场景

- 让 agent 自主迭代优化检索质量等技术指标，保留完整证据记录
- 团队异步协作研究：通过 MCP/REST 查看进度并调整策略
- 以最轻基础设施在 Claude Code/Codex 内跑结构化研究项目

## 场景标签

`Agent 框架` `科研工具` · 领域:Agent 开发

## 证据(README 行号)

> L12: Give Limina a problem with a measurable goal. It will autonomously research it — forming
> L28: |Execution|Limina owns long-running Codex or Claude Code execution, recovery, and retries|You run Codex or Claude C

## 星数曲线

```mermaid
xychart-beta
    title "theam/limina 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-27 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `eebd717e128a` · [字段定义](../../DATASET.md)*
