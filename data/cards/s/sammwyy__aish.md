# sammwyy/aish

⭐ 23 · Rust · MIT · 推送 2025-12-06 · [GitHub](https://github.com/sammwyy/aish) · 个人维护

**用自然语言执行 shell 命令与文件操作的 CLI 助手**

Rust 编写的命令行 AI 助手：接收自然语言请求，经 LLM 理解后生成并执行 shell 命令与文件读写操作，每个操作默认需用户批准。支持 OpenAI、OpenRouter 及任意 OpenAI 兼容自定义 API 作为后端，配置存于 ~/.aish/。自动检测工作区上下文（语言、包管理器、Docker/K8s、云厂商、IaC 工具等）辅助决策。安全机制含路径校验、.aishignore 模式屏蔽、白名单自动执行（仅限 --accept-all）。提供交互式会话模式保留完整对话历史。从源码用 cargo 编译安装，需 Rust 1.70+ 与 LLM API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转 shell 命令执行，操作需逐项批准
- 支持 OpenAI / OpenRouter / 任意 OpenAI 兼容 API
- 自动检测工作区上下文（语言、Docker、云厂商、IaC 等）
- 白名单自动执行与 .aishignore 敏感路径屏蔽

## 适用场景

- 不记得命令语法时用自然语言完成系统操作
- 连续对话式执行多步运维与分析任务
- 让 AI 按模板批量创建项目结构与文件

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L8: `aish` is an intelligent command-line assistant that uses Large Language Models (LLMs) to understand your natural la
> L26: - 🔧 **Flexible**: Supports multiple LLM providers (OpenAI, OpenRouter, Custom)

## 星数曲线

```mermaid
xychart-beta
    title "sammwyy/aish 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-27 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `e7e7df938908` · [字段定义](../../DATASET.md)*
