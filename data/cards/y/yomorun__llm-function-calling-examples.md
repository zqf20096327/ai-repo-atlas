# yomorun/llm-function-calling-examples

⭐ 23 · TypeScript · MIT · 推送 2026-07-02 · [GitHub](https://github.com/yomorun/llm-function-calling-examples) · [官网](https://yomo.run) · 组织维护

**YoMo LLM 函数调用的 TypeScript/Go 强类型示例集合**

为 YoMo 框架提供 LLM function calling 示例：每个示例导出描述、类型化参数与处理函数，可被 YoMo 暴露为 LLM 可调用工具。覆盖天气、时间时区、汇率、网页搜索、IP 延迟、邮件发送（SMTP/Resend/AutoSend）与 PostgreSQL 查询等场景，分 TypeScript 与 Go 两组。使用流程：安装 YoMo CLI，配置并启动 yomo serve 的 LLM Bridge，再以 yomo run 运行单个函数，通过本地 OpenAI 风格 chat completions API 调用。各示例依赖自身所需的环境变量（如 OPENWEATHERMAP_API_KEY）。

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

- 每个示例导出描述、类型化参数与处理函数三要素
- 覆盖天气/时间/汇率/搜索/邮件/数据库等 20 余个示例
- 提供 TypeScript 与 Go 双语言实现
- 通过 yomo serve 暴露本地 /v1/chat/completions API 并自动路由调用

## 适用场景

- 学习如何在 YoMo 中实现强类型的 LLM 可调用工具
- 复用现成工具函数（天气、搜索、邮件、数据库）接入自己的 LLM 应用
- 本地搭建 LLM bridge 验证 function calling 流程

## 场景标签

 · 领域:LLM 工具调用/开发示例

## 证据(README 行号)

> L3: This repository contains TypeScript and Go examples for YoMo LLM function calling.
> L10: Each example exports a description, typed arguments, and a handler that YoMo can expose as an LLM callable tool.
> L117: YoMo routes the request to the LLM provider, exposes the running functions as tools, invokes the matching function

## 星数曲线

```mermaid
xychart-beta
    title "yomorun/llm-function-calling-examples 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-31 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `02c7a332a3e0` · [字段定义](../../DATASET.md)*
