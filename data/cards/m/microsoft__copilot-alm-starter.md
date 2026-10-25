# microsoft/copilot-alm-starter

⭐ 70 · PowerShell · MIT · 推送 2026-10-19 · [GitHub](https://github.com/microsoft/copilot-alm-starter) · 组织维护

**Copilot Studio agent 的 ALM 模板：CI/CD 工作流与部署指南**

微软维护的 Power Platform 应用生命周期管理（ALM）模板仓库，面向 Copilot Studio agent 的导出、构建与部署。提供 GitHub Actions 与 Azure DevOps 两套等价的流水线（导出建 PR、构建部署、PR 校验）、跨平台复用的 PowerShell 脚本、建议目录结构与分步文档。认证采用联合凭据/Workload Identity Federation（无密钥管理），需自备 Power Platform 环境与 App Registration。通过 GitHub 模板或导入 Azure DevOps 项目使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GitHub Actions 与 Azure DevOps 双平台的导出/构建部署/PR 校验流水线
- 跨平台复用的 PowerShell 自动化脚本
- 联合凭据认证方案，无需管理密钥
- 覆盖环境配置、本地开发与故障排查的分步文档

## 适用场景

- 为 Copilot Studio agent 搭建从开发到生产的 CI/CD 流水线
- 在 GitHub 与 Azure DevOps 之间选择统一方案的 ALM 落地
- 规范化 Power Platform 解决方案的源码组织与部署配置

## 场景标签

 · 领域:开发运维/低代码平台

## 证据(README 行号)

> L3: A lightweight ALM toolkit for Copilot Studio agents – CI/CD pipelines, best practices, and deployment guidance for *
> L7: This repository provides everything you need to implement Application Lifecycle Management (ALM) for your Power Plat

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/copilot-alm-starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-25 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `a3827124b1c4` · [字段定义](../../DATASET.md)*
