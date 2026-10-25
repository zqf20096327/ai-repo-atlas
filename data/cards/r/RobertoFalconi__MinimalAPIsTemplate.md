# RobertoFalconi/MinimalAPIsTemplate

⭐ 38 · C# · 推送 2026-08-05 · [GitHub](https://github.com/RobertoFalconi/MinimalAPIsTemplate) · 个人维护

**面向 .NET 10 的 Clean Architecture Minimal API 项目模板**

一个 ASP.NET Core Minimal APIs 起始模板：按 Clean Architecture 组织为 Api/Application/Infrastructure/Domain 四层，外层依赖内层、Domain 零依赖；用两个泛型接口实现无 MediatR 的 CQRS；内置 JWT Bearer 认证、EF Core + SQL Server code-first 数据库、Scalar API 文档。通过 git clone 获取，需 .NET 10 SDK、SQL Server 实例与 dotnet-ef CLI 工具，运行 dotnet ef database update 后 dotnet run 启动。仓库描述中还列出 OpenAI 接入、OAuth 2.0、JWE/JWS、MediatR、Dapper、Hangfire 等组件，但 README 正文未展开说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 层 Clean Architecture，Domain 层零依赖
- 不依赖 MediatR 的轻量 CQRS 泛型接口实现
- 内置 JWT Bearer 认证（POST /auth/token 签发）
- EF Core + SQL Server code-first，启动时自动建库

## 适用场景

- 以模板起步搭建符合 Clean Architecture 的 .NET 10 API 服务
- 学习 Minimal APIs 与无中介库的 CQRS 组织方式
- 在带认证的骨架上快速添加新用例（命令/处理器/端点）

## 场景标签

 · 领域:Web 后端开发

## 证据(README 行号)

> L3: A production-ready template for building **.NET 10 Minimal APIs** following **Clean Architecture**, **Domain-Driven 
> L9: This repository provides a clean, minimal, and opinionated starting point for ASP.NET Core APIs. It demonstrates how

## 星数曲线

```mermaid
xychart-beta
    title "RobertoFalconi/MinimalAPIsTemplate 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-25 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `d78c761c9080` · [字段定义](../../DATASET.md)*
