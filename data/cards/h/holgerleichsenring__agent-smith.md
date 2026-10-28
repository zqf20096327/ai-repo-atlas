# holgerleichsenring/agent-smith

⭐ 31 · C# · MIT · 推送 2026-10-27 · [GitHub](https://github.com/holgerleichsenring/agent-smith) · [官网](https://agent-smith.org) · 个人维护

**自托管 agentic 软件工厂：工单进，规格、验证、PR 出**

开源的 agentic 软件工厂，由 Holger Leichsenring 主导。用户将工单投递到 Azure Boards/Jira/GitHub/GitLab，系统推导规格，把每个仓库克隆进带各自工具链的沙箱（dotnet/sdk:8.0、node:20、python:3.12），按规格顺序构建、运行各仓库声明的验证，为每个仓库开一个交叉关联的 PR 并回写工单。验收由独立 reader 逐条裁定并引用分支证据；推理过程、决策与成本落盘到 .agentsmith/ 目录。以 CLI 单二进制、Docker Compose、Kubernetes 方式自托管。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 工单→规格→沙箱构建→逐条验证→PR→回写工单的完整闭环
- 独立 reader 逐条裁定验收标准并引用分支证据
- 每次运行记录规格、决策（含被否备选）与 token/美元成本
- 提供 code、pr-review、security-scan、legal-analysis 等多条流水线

## 适用场景

- 把缺陷或需求工单自动变成经验证的拉取请求
- 在 Azure DevOps/Jira/GitHub/GitLab 环境内闭环处理工单
- 审查 PR、执行安全扫描与合同分析的流水线
- 事后追溯某次变更的决策依据与成本

## 场景标签

`编码 Agent` `代码审查` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L14: Agent Smith is an open source agentic software factory, a project led by its creator, Holger Leichsenring. You drop
> L22: You drop a ticket into your tracker. Agent Smith reads it and derives a specification: the specs the work needs and
> L50: |Trackers|AI providers|Hosting|

## 星数曲线

```mermaid
xychart-beta
    title "holgerleichsenring/agent-smith 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25", "2026-10-28"]
    y-axis "stars" 28 --> 32
    line [29, 30, 31, 31]
```

2026-10-18 29 → 2026-10-28 31（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a42d8a1c3e42` · [字段定义](../../DATASET.md)*
