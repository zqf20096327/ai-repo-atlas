# microsoft/github-copilot-modernization

⭐ 54 · JavaScript · MIT · 推送 2026-09-23 · [GitHub](https://github.com/microsoft/github-copilot-modernization) · 组织维护

**给开发者的 Copilot CLI 插件：自动化 Java/.NET 应用现代化**

GitHub Copilot CLI 的插件，以多 agent 编排（orchestrator→coordinator→executor 三级）实现 Java 与 .NET 应用的自动化现代化：评估阶段本地运行 AppCAT、npm-check-updates 与 GitHub advisory 检查并生成 HTML 报告，规划阶段生成可执行任务计划（企业 rulebook 约束可覆盖评估建议），执行阶段将任务路由到专门 agent 并行处理 Java 升级、Azure 迁移、CVE 修复与架构重写。评估可检测 Java/.NET/JS，但自动化规划与执行仅限 Java/.NET。经 Copilot 插件 marketplace 安装，仅 modernize agent 可由用户调用，其余 agent 由编排器自动路由。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三级 agent 层级编排，executor 并行执行任务并带重试验证
- 企业 rulebook（目标架构/护栏/编码标准）可覆盖评估建议
- Java 8→21 升级、Spring Boot 2→3、javax→jakarta 迁移
- Maven/NuGet 依赖 CVE 扫描与修复，含分阶段提交记录

## 适用场景

- 把 Spring Boot 应用升级到 Java 21 并迁移到 Azure
- 扫描并修复 Maven/NuGet 依赖中的 CVE 漏洞
- 按企业标准（rulebook）执行单体到微服务的架构重写
- 无人值守（--allow-all）批量执行现代化计划

## 场景标签

`编码 Agent` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: Autonomous application modernization using multi-agent orchestration for GitHub Copilot CLI.
> L9: This plugin enables autonomous modernization of Java and .NET applications through a multi-agent orchestration syste
> L123: - Each executor queries MCP knowledge base for migration patterns

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/github-copilot-modernization 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28"]
    y-axis "stars" 52 --> 55
    line [53, 54, 54]
```

2026-10-18 53 → 2026-10-28 54（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `78511e359feb` · [字段定义](../../DATASET.md)*
