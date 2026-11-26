# adhocteam/cloud-gov-instructions

⭐ 10 · MIT · 推送 2026-09-22 · [GitHub](https://github.com/adhocteam/cloud-gov-instructions) · [官网](https://adhocteam.github.io/cloud-gov-instructions/) · 组织维护

**为 AI 编码助手提供 cloud.gov 平台规范的指令文件集**

该仓库打包了一组可直接复制进目标项目的指令文件，包括仓库级 Copilot 指令、AGENTS.md 行为守则、按文件模式生效的任务指令（部署、清单配置、服务集成、CI/CD、安全、日志）、自定义 Copilot Agent（合规文档生成）与技能文件（CF 故障排查）。AI 助手据此遵循 cloud.gov 惯例、生成含 NIST SP 800-53 控制引用的代码，并在执行高风险 cf 命令前要求确认。使用前提是具备自定义指令支持的 GitHub Copilot 订阅、VS Code 及 Cloud Foundry CLI。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 copilot-instructions.md、AGENTS.md、任务级指令、自定义 Agent 与技能五类文件
- AI 安全护栏：高风险 cf 删除命令强制确认，生产环境限制修改类命令
- compliance-docs Agent 生成 SSP 章节、控制实现矩阵与控制继承文档
- 生成安全相关代码时自动附带 NIST SP 800-53 控制引用

## 适用场景

- 将部署到 cloud.gov 的项目让 Copilot 自动遵循平台部署与清单惯例
- 为应用生成 FedRAMP/NIST 控制实现矩阵与 SSP 合规文档
- 约束 AI 助手不擅自执行破坏性 Cloud Foundry 命令

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: A reusable set of instruction files for AI coding assistants (GitHub Copilot) that encapsulate cloud.gov platform gu
> L11: This repository provides a comprehensive set of instruction files that help AI coding assistants understand and fol
> L160: - **GitHub Copilot**: Active subscription with custom instructions support

## 星数曲线

```mermaid
xychart-beta
    title "adhocteam/cloud-gov-instructions 星数(近 2 点)"
    x-axis ["2026-10-24", "2026-11-26"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-24 10 → 2026-11-26 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `013cae208e53` · [字段定义](../../DATASET.md)*
