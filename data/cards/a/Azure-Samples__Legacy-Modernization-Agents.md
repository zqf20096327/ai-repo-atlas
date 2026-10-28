# Azure-Samples/Legacy-Modernization-Agents

⭐ 227 · C# · MIT · 推送 2026-10-25 · [GitHub](https://github.com/Azure-Samples/Legacy-Modernization-Agents) · 组织维护

**AI agent 框架：将 COBOL 大机代码自动迁移到 Java Quarkus 或 C#**

基于 Microsoft Agent Framework 的开源迁移框架，面向遗留大机代码现代化。多 provider 架构支持 Azure OpenAI、GitHub Copilot SDK 与直接 OpenAI，由分析、转换、依赖映射等 agent 协作，把 COBOL 及其依赖转换为 Java Quarkus 或 C# .NET。本地用 REKT 解析 COBOL 与 JCL 构建 Neo4j 依赖图，提供 Web 门户可视化迁移进度与切片规划。限制：需 .NET 10 SDK 与 Docker（Neo4j），Java 输出尚无编译门禁，源码会包含在发送给模型的提示中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多 provider 架构：Azure OpenAI、GitHub Copilot SDK、直接 OpenAI，含模型能力自动检测
- REKT 本地解析 COBOL/JCL 入 Neo4j 依赖图，不调用模型
- Estate Mission Control 门户：资产概览、切片规划与转换命令生成
- JCL 迁移不调用模型，生成后可用 dotnet build / mvn compile 编译

## 适用场景

- 把 COBOL 程序与 JCL 作业转换为 Java Quarkus 或 C# .NET
- 迁移前梳理遗留资产依赖关系并规划分批切出方案
- 仅提取 COBOL 业务逻辑文档（reverse-eng）

## 场景标签

`Agent 框架` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L3: This open source migration framework was developed to demonstrate AI Agents capabilities for converting legacy code 
> L4: The migration uses Microsoft Agent Framework with a multi-provider architecture supporting **Azure OpenAI** (Respons

## 星数曲线

```mermaid
xychart-beta
    title "Azure-Samples/Legacy-Modernization-Agents 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-28"]
    y-axis "stars" 225 --> 228
    line [226, 227, 227]
```

2026-10-18 226 → 2026-10-28 227（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `22b36f43e695` · [字段定义](../../DATASET.md)*
