# unitshaperextol/Legion-os

⭐ 75 · MIT · 推送 2026-10-29 · [GitHub](https://github.com/unitshaperextol/Legion-os) · 个人维护

**多 Agent 集群编排引擎：协调 50+ 异构 LLM 节点运行**

面向多智能体规模化编排的可执行程序 legion.exe：以网格网络运行 50+ 异构 LLM 节点（OpenAI/Anthropic/Google/DeepSeek 模型分派不同角色），提供动态竞拍与网格路由、预算上限与按成本改路由、Supervisor 节点对幻觉/超时响应作废并重生子任务、输出 schema 校验，以及终端 TUI 与 Web 仪表盘遥测。安装方式为下载 Legion.rar 解压后直接运行二进制，支持 YAML 配置文件与 headless 模式，MIT 许可。README 列出的适配模型（GPT-6 Astra、Claude 5.5 Opus 等）为文档声明，无法独立核验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 声明支持 50–500+ 并发 Agent 节点的网格编排
- 预算硬上限与超限自动改路由到低成本模型
- 幻觉/超时响应作废与子任务自动重生
- 零依赖单体二进制，内置 TUI 遥测与 Web 仪表盘

## 适用场景

- 在单集群中混合使用多家厂商模型分派不同角色
- 为大规模 Agent 任务设置成本上限并实时监控
- 服务器上以 headless 模式部署多 Agent 工作流

## 场景标签

`多智能体` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L10: LEGION is an enterprise-grade, zero-overhead orchestrator designed to run 50+ autonomous frontier AI models in a un
> L43: - **⚔️ Heterogeneous Model Mesh:** Assign different LLMs to different roles in a single swarm (`GPT-6` for planning


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `9bc2b5c8acf6` · [字段定义](../../DATASET.md)*
