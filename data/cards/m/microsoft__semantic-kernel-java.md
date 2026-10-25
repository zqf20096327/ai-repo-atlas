# microsoft/semantic-kernel-java

⭐ 276 · Java · MIT · 推送 2026-10-23 · [GitHub](https://github.com/microsoft/semantic-kernel-java) · 组织维护

**面向 Java 开发者的 LLM 编排 SDK：插件链式调用与 AI 规划**

微软 Semantic Kernel 的 Java 版 SDK，将 OpenAI、Azure OpenAI、Hugging Face 等 LLM 与 Java 等常规编程语言集成。开发者以插件形式定义功能，插件可链式组合，也可由 planner 让 LLM 生成执行计划并自动编排运行。提供学习文档与社区渠道（Discord、办公时间）。安装方式为克隆仓库并按文档运行 Java 控制台示例；C# 与 Python 版本在另一仓库维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以插件形式集成 LLM，插件可链式调用
- planner 可让 LLM 自动生成并执行计划
- 支持 OpenAI、Azure OpenAI、Hugging Face 等 LLM 接入

## 适用场景

- 在 Java 应用中接入 OpenAI/Azure OpenAI 完成生成任务
- 通过 planner 让 LLM 自动编排插件实现用户目标
- 创建并运行 ChatGPT 插件

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L9: Semantic Kernel is an SDK that integrates Large Language Models (LLMs) like OpenAI, Azure OpenAI, and Hugging Face
> L12: What makes Semantic Kernel _special_, however, is its ability to _automatically_ orchestrate plugins with AI. With 

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/semantic-kernel-java 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 275 --> 277
    line [276, 276]
```

2026-10-18 276 → 2026-10-25 276（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `3d5beafea2b4` · [字段定义](../../DATASET.md)*
