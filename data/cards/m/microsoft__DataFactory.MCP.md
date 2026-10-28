# microsoft/DataFactory.MCP

⭐ 45 · C# · MIT · 推送 2026-10-22 · [GitHub](https://github.com/microsoft/DataFactory.MCP) · [官网](https://www.nuget.org/packages/Microsoft.DataFactory.MCP/) · 组织维护

**面向 Microsoft Fabric 资源管理的 MCP 服务器**

基于官方 MCP C# SDK 构建的 Model Context Protocol 服务器，供 IDE 中启用了 MCP 的聊天界面（VS Code / Visual Studio）调用，通过 Azure AD 交互式或服务主体认证后，以标准化 MCP 工具访问 Microsoft Fabric 资源：网关、连接、工作区、数据流、管道、复制作业、Airflow 作业与容量的列出/创建/运行/监控等操作，并暴露 VS Code 聊天内渲染的交互式 UI 表单资源。以 NuGet 包分发，开发需 .NET 10.0+；另附可选的 Claude 与 ChatGPT 知识文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖 Microsoft Fabric 网关/连接/数据流/管道/复制作业/Airflow 作业等 40+ MCP 工具
- Azure AD 交互式与服务主体两种认证方式
- 以 MCP App resources 形式在 VS Code 聊天内渲染交互式创建连接向导
- NuGet 包分发，IDE 配置后自动下载可用

## 适用场景

- 在 VS Code / Visual Studio 聊天界面中直接管理 Fabric 数据管道与数据流
- 通过 MCP 客户端以标准化工具接口访问 Microsoft Fabric 资源
- 结合 Claude/ChatGPT 知识文件获取 Data Factory 操作提示

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L3: A Model Context Protocol (MCP) server for Microsoft Fabric resource discovery and information retrieval. This server
> L22: - 🔧 **MCP Protocol**: Built using the official MCP C# SDK

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/DataFactory.MCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-28 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `44d8b6d3d0b0` · [字段定义](../../DATASET.md)*
