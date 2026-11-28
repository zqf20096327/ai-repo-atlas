# pavelveter/AGENTS.md

⭐ 95 · Shell · MIT · 推送 2026-11-20 · [GitHub](https://github.com/pavelveter/AGENTS.md) · 个人维护

**为 AI 编码代理提供工程化规则与工作流模板**

一套面向 AI 编码代理的模块化工程规则集：核心 AGENTS.md 加上调试、依赖、Git、重构、安全、测试、规格驱动开发等分模块文档，以及按 Go/Node/Python/Web 拆分的栈级规则。围绕上下文工程、代理边界约束、验证优先、根因调试等原则组织，并配套 evals 评估场景与标准报告格式。以 OpenCode 环境为实际运行背景，规则本身声明不绑定特定运行时，可通过复制 Markdown 文件到项目并配置代理加载使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 模块化规则文件：核心规则 + 调试/依赖/Git/安全/测试等分模块按需加载
- 提供 stacks/ 目录下 Go、Node、Python、Web 的栈级规则
- 带 benchs/evals.md 评估场景与标准任务报告格式（STATUS/VERIFICATION 等）
- 声明核心规则不绑定 OpenCode，可迁移到其他代理运行时

## 适用场景

- 给 AI 编码代理设定任务边界与验证要求
- 在团队项目中统一代理的提交、测试与报告规范
- 评估规则变更是否真正改变代理行为

## 场景标签

`提示工程` `模型评测` · 领域:Agent 开发

## 证据(README 行号)

> L22: This repository contains a modular set of rules, workflows, and tools designed to make AI coding agents more predic
> L285: 1. Copy `AGENTS.md` and the supporting Markdown files into your project.
> L264: The core engineering rules are not tied to OpenCode.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 low · 依据 README sha `50c6200d7bdc` · [字段定义](../../DATASET.md)*
