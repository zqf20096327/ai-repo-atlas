# Unsupervisedcom/deepwork

⭐ 50 · Python · NOASSERTION · 推送 2026-10-24 · [GitHub](https://github.com/Unsupervisedcom/deepwork) · 组织维护

**给 Claude 用户的多步任务自动化插件：工作流+审查+文件契约**

面向 Claude Code 与 Claude Desktop（Cowork 模式）的插件，由 Unsupervisedcom 维护。核心机制包括：Workflows 强制 agent 按步骤执行并设置质量门禁；Reviews 通过 .deepreview 配置文件对每次变更并行运行审查规则；DeepSchemas 在写入时校验文件契约（RFC 2119 关键词定义严重级别）；DeepPlan 将计划转换为可执行工作流。使用方式：先与 Claude 完成一次任务，再通过 /deepwork 命令将其固化为可复用工作流（约 10 分钟问答）。源码以 BSL 1.1 提供，免费使用。限制：marketplace 添加在 Windows 上会失败（Claude Desktop 场景）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Workflows 按步骤执行并设质量门禁，阻止 agent 跳步
- Reviews 按 .deepreview 规则对每次变更并行自动审查
- DeepSchemas 在写入时校验文件契约（MUST/SHOULD/MAY）
- 把一次性任务固化为可复用工作流，支持 /deepwork learn 自动调优

## 适用场景

- 把竞争对手研究等重复任务固化为可复用工作流
- 让 agent 自动审查每次代码或文档变更
- 为 API 端点、配置等文件类型定义并自动执行校验规则

## 场景标签

`工作流自动化` `代码审查` · 领域:效率与自动化

## 证据(README 行号)

> L5: DeepWork fixes this with two systems: **Workflows** that force agents to follow a structured process step by step, a
> L11: claude plugin marketplace add Unsupervisedcom/deepwork && claude plugin install deepwork@deepwork-plugins && claude
> L81: Reviews are the second layer of trust. You define review policies in `.deepreview` config files — what files to wat

## 星数曲线

```mermaid
xychart-beta
    title "Unsupervisedcom/deepwork 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-29 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `e7ea13f9fcf5` · [字段定义](../../DATASET.md)*
