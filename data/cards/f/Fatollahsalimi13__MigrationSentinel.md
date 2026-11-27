# Fatollahsalimi13/MigrationSentinel

⭐ 3 · C# · MIT · 推送 2026-11-18 · [GitHub](https://github.com/Fatollahsalimi13/MigrationSentinel) · 个人维护

**.NET/EF Core 数据库迁移零停机风险扫描 CLI**

面向 .NET/EF Core 与 SQL Server/PostgreSQL 的数据库迁移守卫工具：通过 Roslyn C# AST 与方言感知 SQL 解析器做静态分析，内置 14 条 DBA 风险规则（数据丢失、表锁、契约破坏等），生成方言特定的安全上线 SQL（如 CREATE INDEX CONCURRENTLY）与 SARIF v2.1.0 报告。支持 Git diff 做 PR 门禁，可上传 GitHub Security tab；另提供可选的 OpenAI 或本地 Ollama AI 审查层。以 .NET 全局工具、NuGet 库或源码方式分发，需 .NET 8 SDK。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Roslyn 解析 EF Core 迁移 C# AST，含 migrationBuilder.Sql() 内嵌 SQL 的递归解析
- 14 条确定性风险规则（MS001–MS014）与风险评分、缓解 SQL 生成
- SARIF v2.1.0 报告上传 GitHub Security，支持 Git diff PR 门禁与退出码控制
- 可选 AI 审查：OpenAI API 或本地 Ollama（气隙环境）

## 适用场景

- CI/CD 中拦截含 DROP TABLE、无 WHERE 的 DELETE 等高危迁移的 PR
- 为既有 EF Core 迁移生成零停机上线的 SQL 方案
- 气隙环境下用本地模型做迁移脚本审查

## 场景标签

 · 领域:开发者工具/数据库/DevOps

## 证据(README 行号)

> L29: 3. **Hybrid Deterministic + AI Review Layer:** Pairs 14 zero-latency, deterministic DBA rules with optional context
> L34: MigrationSentinel is built with strict **Clean Architecture** separation so you can run it as a global `.NET` CLI t
> L181: - **Enterprise-Ready Open Standards:** Ships under a permissive **MIT License** with zero vendor lock-in, full **S

## 星数曲线

```mermaid
xychart-beta
    title "Fatollahsalimi13/MigrationSentinel 星数(近 2 点)"
    x-axis ["2026-11-20", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-20 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `2498fe69c028` · [字段定义](../../DATASET.md)*
