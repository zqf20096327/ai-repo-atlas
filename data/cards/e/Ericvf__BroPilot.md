# Ericvf/BroPilot

⭐ 12 · C# · GPL-3.0 · 推送 2026-04-24 · [GitHub](https://github.com/Ericvf/BroPilot) · 个人维护

**连接本地 LLM 的 Visual Studio/SSMS 代码辅助扩展**

Visual Studio 扩展（另支持 SSMS），连接本地 LLM 服务器（Ollama、LM Studio 或兼容后端）提供代码补全、代码解释、重构建议；所有处理在本机完成，代码与上下文不外发。包含 Try 按钮功能，可在 C# 文件中生成插入或替换类/方法（限 C#、需文件属于活动解决方案）。LLM 响应流式逐 token 显示，重操作后台线程处理。要求 Visual Studio 2022+、.NET Framework 4.8 / .NET 8 及运行中的本地 LLM 服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 连接 Ollama、LM Studio 等本地 LLM 后端，代码不出本机
- Try 按钮可在 C# 文件内生成插入或替换类/方法
- SQL Server Management Studio (SSMS) 内的 SQL 解释与重构建议
- 流式 token 显示与后台线程处理

## 适用场景

- 在 Visual Studio 里用本地模型获得代码解释与重构建议
- 合规要求下不把代码发给云端服务的 AI 辅助编程
- 在 SSMS 中理解和重构 SQL 查询

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: BroPilot is a Visual Studio extension that brings the power of local Large Language Models (LLMs) directly into your
> L39: - Connects to local LLM servers (such as Ollama, LM Studio, or other compatible backends).

## 星数曲线

```mermaid
xychart-beta
    title "Ericvf/BroPilot 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-27", "2026-11-01"]
    y-axis "stars" 10 --> 13
    line [12, 11, 12, 12]
```

2026-10-18 12 → 2026-11-01 12（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-01 · 置信度 high · 依据 README sha `6390970df653` · [字段定义](../../DATASET.md)*
