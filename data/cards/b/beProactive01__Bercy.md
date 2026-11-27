# beProactive01/Bercy

⭐ 3 · JavaScript · MIT · 推送 2026-11-26 · [GitHub](https://github.com/beProactive01/Bercy) · 个人维护 · 中文 README

**给开发者的本地多 Agent 工作流编排桌面应用**

基于 Electron 的 macOS 本地桌面应用，把一句话目标拆解为多 Agent DAG 工作流：规划角色与依赖、并行执行独立节点、下游节点汇聚上游输出。内置跨模型评审节点（最多两轮退回修订）、运行中动态补插缺失步骤并记录版本原因。通过接入用户已登录的 CLI 编码 Agent（Codex、Claude Code、OpenClaw、DeepSeek Harness、Pi 及任意 ACP 兼容运行时）运行，按节点能力路由到合适运行时。支持工作流保存/版本化/定时/导入导出，状态存于本地 SQLite，应用自身不发起网络请求。仅支持 Apple Silicon Mac。

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

- 一句话目标自动规划为多节点 DAG 工作流并并行执行
- 评审节点用不同模型交叉检查上游工作，最多两轮修订
- 按能力匹配节点到运行时，支持任意 ACP 兼容运行时接入
- 工作流可保存版本、定时执行、导出为 .bercy.json 分享

## 适用场景

- 把一个发布任务拆给多个编码 Agent 并行产出文档与检查清单
- 让不同厂商的模型互相评审代码产出
- 定时在本地仓库上运行固定流程并留存执行记录

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3:  Turn one sentence into a team of AI agents that split the work, check each other and adapt as results come in.
> L4:  A local desktop app for the coding agents you already use: Codex, Claude Code, OpenClaw, DeepSeek Harness and Pi.
> L20: - **The best agent for each step.** Mix Codex, Claude Code, OpenClaw, DeepSeek Harness, Pi or any ACP runtime in on


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `3f1ed7ab64bb` · [字段定义](../../DATASET.md)*
