# ayazelrico/freya-build-the-builder

⭐ 4 · Python · 推送 2026-10-11 · [GitHub](https://github.com/ayazelrico/freya-build-the-builder) · 个人维护

**把银行需求简报和 OpenAPI 规格构建成语音电话 agent 的构建器**

面向 Freya 语音平台的自动化构建工具：读取银行需求简报与 OpenAPI 规格文件，经 SPEC 提取、工作流生成、本地校验、Freya dry-run 修复循环、agent 参数调优（土耳其语 STT/TTS、轮次时序）与自测后，导出可发布的电话 agent workflow JSON。日期、金额、结果编码与必读话术由代码生成，模型仅负责对话。输出包含每次模型调用的 trace 日志。支持通过 Claude Code CLI 代替 API key 运行模型调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一条命令从 brief + openapi.json 生成并发布 Freya 电话 agent 工作流
- 生成/本地检查/dry-run 修复循环/自测/导出的完整流水线
- 每次模型调用记录 trace 日志（模型、用途、步骤数与自测结果）
- 可通过 BUILDER_BACKEND=cli 经 Claude Code CLI 运行模型调用

## 适用场景

- 把银行业务需求简报快速转换为语音电话 agent
- 在 Freya 平台上批量更新同一 slot 的电话工作流
- 对生成的 agent 工作流做本地模拟与自测验证

## 场景标签

`工作流自动化` `代码生成` · 领域:效率与自动化

## 证据(README 行号)

> L1: # Freya "Build the Builder": a builder that turns a bank brief into a phone agent
> L13: - `submission/<brief name>.workflow.json`: the exported phone agent (`freya.export_workflow`)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `8517e3dc1af5` · [字段定义](../../DATASET.md)*
