# qsumm/CodeFlow

⭐ 5 · TypeScript · GPL-3.0 · 推送 2026-11-23 · [GitHub](https://github.com/qsumm/CodeFlow) · [官网](https://codeflow.com.cn) · 个人维护 · 中文 README

**AI 需求交付平台：从需求澄清到验收的全流程管理**

自托管的 Java/Spring Boot 平台，将需求交付拆为澄清→开发→测试→验证四步流程：AI 数字员工先反问澄清并生成 spec/plan，再由部署在用户机器上的执行器节点（主动回连、零入站端口）完成开发与测试，交付结论回写禅道/TAPD。平台提供完成门卡步、失败留痕重试、产物归档、周期/一次通过率/Token 消耗度量与操作审计。执行器支持 6 种 CLI，模型端点可换任意 Anthropic 兼容服务。Docker 部署，GPL-3.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 需求澄清前置：AI 反问后落档 spec/plan，确认才开工
- 执行器主动回连架构，防火墙/NAT 后零入站端口
- 完成门卡步与失败派发留痕重试
- 提供 MCP Server（19 工具）供外部 Agent 操作平台

## 适用场景

- 团队在禅道/TAPD 流程中用 AI 完成需求的开发与测试
- 内网环境下接入 AI 编码执行器交付需求
- 需要全过程留痕与操作审计的 AI 交付管理

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L52: - **运行节点** — 主动回连领任务，代码在内网照样干活；6 种 CLI（Claude Code / Codex / Cursor / Gemini / Qoder）
> L94: 模型任意 Anthropic 兼容端点（Claude / MiniMax / GLM / DeepSeek…），改执行器 env 三个变量即换，平台不绑定。
> L80: |MCP Server（外部 Agent 操作平台）|✅ 19 工具|✅|❌|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `8810226bf128` · [字段定义](../../DATASET.md)*
