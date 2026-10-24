# aliyun/rdsai-cli

⭐ 63 · Python · Apache-2.0 · 推送 2026-05-02 · [GitHub](https://github.com/aliyun/rdsai-cli) · 组织维护 · 中文 README

**阿里云出品的 AI 数据库命令行工具，自然语言查询与 SQL 优化**

面向数据库使用者的 AI 驱动 CLI：连接 MySQL 或本地/远程文件（CSV、Excel）后，可用中英文自然语言查询、自动识别输入是 SQL 还是自然语言，并提供 SQL 优化、执行计划分析、Schema 合规检查与 sysbench 性能基准测试。支持 Qwen、OpenAI、DeepSeek、Anthropic、Gemini 及 OpenAI 兼容 API 等多模型，可经 MCP 服务器扩展能力。默认只读，DDL/DML 需确认（可选 YOLO 自动批准模式）。由阿里云维护，提供一键安装脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言与 SQL 混合输入，自动检测并执行
- 多模型 LLM 支持：Qwen、OpenAI、DeepSeek、Anthropic、Gemini 及兼容 API
- 执行计划分析、Schema 合规检查与 sysbench 自动基准测试
- 默认只读，写操作需逐条确认，支持 MCP 服务器扩展

## 适用场景

- 用自然语言查询和优化 MySQL 数据库
- 分析 SQL 执行计划与慢查询原因
- 对数据库 Schema 做合规检查与优化建议
- 运行自动化性能基准测试并获取报告

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L13: RDSAI CLI is an AI-powered command-line interface for database management.
> L20: - **AI Assistant** - Natural language queries (English/Chinese), SQL optimization, diagnostics, and explanations

## 星数曲线

```mermaid
xychart-beta
    title "aliyun/rdsai-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-24 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ab85f8e24b02` · [字段定义](../../DATASET.md)*
