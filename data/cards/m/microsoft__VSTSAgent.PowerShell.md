# microsoft/VSTSAgent.PowerShell

⭐ 36 · PowerShell · MIT · 推送 2025-12-02 · [GitHub](https://github.com/microsoft/VSTSAgent.PowerShell) · 组织维护

**管理 Azure DevOps/VSTS 构建代理的 PowerShell 模块**

由 Microsoft 维护的 PowerShell 模块，面向使用 Visual Studio Team Services / Azure DevOps 的用户，提供 Get-VSTSAgent、Install-VSTSAgent、Uninstall-VSTSAgent、Find-VSTSAgent、Start/Stop-VSTSAgent 等 Cmdlet，用于列出、安装、卸载、启停本机构建代理；内含 xVSTSAgent DSC 资源支持声明式配置。通过 PowerShell Gallery 以 Install-Module 安装，master 分支自动构建发布，develop 分支发布为预发布版本。README 未提及任何 AI 相关功能。本项目与 AI 无直接关系，按分类规则归为 ai-ecosystem 之外的非 AI 工具范畴（如目录要求仅收 AI 项目，本条应标记为不适用）。

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

- 提供 Install/Uninstall/Get/Find/Start/Stop-VSTSAgent 等 Cmdlet
- 内含 xVSTSAgent DSC 声明式配置资源
- 通过 PowerShell Gallery 安装：Install-Module VSTSAgent

## 适用场景

- 在 Windows 机器上安装和卸载 VSTS/Azure DevOps 构建代理
- 脚本化管理本机构建代理的启动与停止
- 用 DSC 配置声明式部署代理

## 场景标签

 · 领域:DevOps/CI-CD 工具

## 证据(README 行号)

> L1: # VSTS Agent PowerShell Module
> L3: Tools for managing and automating your Visual Studio Team Services Agents.

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/VSTSAgent.PowerShell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 low · 依据 README sha `7a626f596868` · [字段定义](../../DATASET.md)*
