# pzalutski-pixel/sharplens-mcp

⭐ 37 · C# · MIT · 推送 2026-10-17 · [GitHub](https://github.com/pzalutski-pixel/sharplens-mcp) · [官网](https://www.nuget.org/packages/SharpLensMcp) · 个人维护

**面向 AI 编程代理的 C#/.NET 语义代码分析 MCP 服务器**

基于 Microsoft Roslyn 的 Model Context Protocol 服务器，为 .NET/C# 项目提供 92 个语义分析工具，覆盖导航与发现（24 个）、分析（17 个）、重构（16 个）、代码生成（3 个）、复合查询（7 个）与审计质量（10 个），供 AI 编程代理执行编译级精度的代码理解、重构与生成。以 .NET 全局工具（dotnet tool）或 npx 安装运行；解决方案以内存表示承载，文件被外部修改后需代理显式调用 sync_documents 同步，未同步时查询可能返回过期数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 Roslyn 的 92 个语义分析工具，分 6 大类
- 诊断输出匹配 CI（含 StyleCop/Roslynator/NetAnalyzers 分析器结果）
- 重构支持预览模式与批量操作，写入保留文件编码与换行符
- 通过环境变量配置解决方案路径、超时与诊断上限等参数

## 适用场景

- 让 Claude Code 等 MCP 客户端对 C# 解决方案做语义级导航与影响分析
- 在 AI 辅助重构中安全重命名符号、提取方法并预览变更
- 审计项目质量：死代码检测、圈复杂度、未被测试覆盖的公共成员
- 对比 git 引用生成公共 API 破坏性变更报告

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: A Model Context Protocol (MCP) server providing **92 AI-optimized tools** for .NET/C# semantic code analysis, naviga
> L9: Built for AI coding agents - provides compiler-accurate code understanding that AI cannot infer from reading source 

## 星数曲线

```mermaid
xychart-beta
    title "pzalutski-pixel/sharplens-mcp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-26 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `32bdbe5530d2` · [字段定义](../../DATASET.md)*
