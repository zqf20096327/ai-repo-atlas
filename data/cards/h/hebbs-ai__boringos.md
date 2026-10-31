# hebbs-ai/boringos

⭐ 42 · TypeScript · AGPL-3.0 · 推送 2026-06-17 · [GitHub](https://github.com/hebbs-ai/boringos) · [官网](https://BoringOS.dev) · 组织维护

**面向 AI agent 的开源编排框架：Shell 门户 + 可安装模块**

用于构建 agentic 平台的开源框架：agent 接收任务后通过 CLI 子进程（Claude Code、Codex、Gemini CLI、Ollama 等）自主执行并回报，框架本身不直接调用 LLM API，只做编排。提供浏览器 Shell（任务、Copilot、agent 组织架构、工作流、预算面板）与可安装的 .hebbsmod 模块体系；内置 framework、memory、drive、inbox、workflow 等模块及 Google/Slack 连接器，默认内嵌 Postgres，可换外部数据库与 BullMQ 队列。以 pnpm monorepo 形式提供，含 npx 脚手架。限制：面向开发者，需 Node 工具链，多租户/预算等功能依赖其平台假设。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六个可插拔 CLI 运行时（Claude Code、ChatGPT CLI、Gemini、Ollama 等）
- Skills（markdown）+ Tools（Zod 类型化）两类注册表构建 agent prompt
- 模块统一形态：Connector/Capability/Hybrid 经 app.module() 注册
- 内置 workflow DAG 运行时、memory、drive、inbox 等模块与 Google/Slack 连接器

## 适用场景

- 搭建带 Web Shell 的多 agent 任务执行平台
- 为 agent 平台扩展第三方集成（Gmail、Slack 等）
- 以模块方式发布带技能、工具与 UI 的领域能力

## 场景标签

`Agent 框架` `多智能体` `工作流自动化` · 领域:Agent 开发

## 证据(README 行号)

> L8: BoringOS is an open-source framework for building agentic
> L11: report back. The framework never calls LLM APIs directly; CLIs
> L274: Six pluggable CLI runtimes ship out of the box: Claude Code,

## 星数曲线

```mermaid
xychart-beta
    title "hebbs-ai/boringos 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-31 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `24ac21e4d0c3` · [字段定义](../../DATASET.md)*
