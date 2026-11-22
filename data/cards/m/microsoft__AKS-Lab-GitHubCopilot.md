# microsoft/AKS-Lab-GitHubCopilot

⭐ 10 · Python · MIT · 推送 2026-11-16 · [GitHub](https://github.com/microsoft/AKS-Lab-GitHubCopilot) · 组织维护

**用 6 个 Copilot 编码代理构建的多代理零售供应链实验教程**

由五个实验组成的实操教程系列，教授如何端到端交付 ZavaShop 零售供应链多代理解决方案：库存/供应商/物流/定价四个专家代理加一个编排器（AKS 上长驻服务），每个专家通过专用 FastMCP 服务器访问后端能力。仓库本身的所有工件——规格、代理代码、MCP 服务器、测试、Bicep/Helm、CI——均由 6 个 GitHub Copilot Custom Coding Agents 编写，教程同时教授这套代理工作流本身。部署路径包含 Entra ID、Workload Identity、Key Vault 与 Defender for Cloud 的安全门禁检查。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 6 个命名的 Copilot Custom Coding Agents 分片负责仓库各部分（规格/MCP/代理/测试/部署）
- 运行时编队：5 个 MAF 代理 + 4 个 FastMCP 服务器，编排器长驻 AKS
- 三个工作流提示串接代理交接：/feature-from-issue、/spec-to-code、/ship-it
- 部署门禁覆盖 Entra ID、Azure Policy、Workload Identity、Key Vault、Defender for Cloud

## 适用场景

- 学习用 Copilot Custom Coding Agents 实践多代理应用的开发工作流
- 在 AKS + ACA 上搭建多代理零售控制平面演示
- 为工作坊运行快速部署轨道并执行冒烟测试与 evals

## 场景标签

`教程课程` `模型评测` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L5: > A hands-on lab series that teaches you to deliver a multi-agent retail supply-chain solution **end-to-end through 
> L8: This repo now includes the packaged ZavaShop stock-out response fleet: five MAF agents, four FastMCP servers, focuse
> L12: Every artifact in this repo — specs, agent code, MCP servers, tests, Bicep, Helm, CI — is authored by a **named Git

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/AKS-Lab-GitHubCopilot 星数(近 2 点)"
    x-axis ["2026-10-28", "2026-11-22"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-28 10 → 2026-11-22 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-19 · 置信度 high · 依据 README sha `ecf1f8dc8d36` · [字段定义](../../DATASET.md)*
