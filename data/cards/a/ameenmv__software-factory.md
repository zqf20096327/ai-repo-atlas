# ameenmv/software-factory

⭐ 4 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/ameenmv/software-factory) · 个人维护

**以 Claude 为编排者、廉价模型为实现者的软件开发流水线参考实现**

以 Claude Code 为编排层、其他模型为实现者的软件构建流水线工具包：每个阶段有机器可校验的退出标准，规则由 hooks 强制执行而非写在提示词中，门禁印章绑定代码树指纹，每次实现运行记入 ledger 记录接受率、耗时与成本。附带零依赖 Node CLI、角色 subagent、编排技能、实现者适配器与模板；支持以 Claude Code 插件安装或整体 vendor 进仓库两种方式。要求 Node 20+、git 与 Claude Code。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- hooks 强制规则：阻止读取 .env、force push、无门禁提交
- 绑定代码树指纹的门禁印章，无印章则拒绝提交
- 实现者通过五行 shell 契约适配，可更换模型
- ledger 记录每次运行的接受率与成本

## 适用场景

- 按阶段化流水线用多个模型协作构建功能
- 防止 AI 编码会话中的范围蔓延与未测试声明
- 按成本路由任务：便宜模型处理简单切片

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A reference pipeline for building production software with Claude as the orchestrator and
> L8: It ships as documentation **and** a working kit: a zero-dependency CLI, Claude Code hooks,
> L66: 3. **Build**: the `brief-writer` turns each slice into a validated brief. `factory delegate` sends it to the first 


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `3afc2d23cc1c` · [字段定义](../../DATASET.md)*
