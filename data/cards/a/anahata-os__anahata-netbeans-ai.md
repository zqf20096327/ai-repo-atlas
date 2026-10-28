# anahata-os/anahata-netbeans-ai

⭐ 40 · Java · Apache-2.0 · 推送 2026-10-01 · [GitHub](https://github.com/anahata-os/anahata-netbeans-ai) · [官网](http://anahata.uno) · 个人维护

**NetBeans IDE 内运行的 Gemini 自主编码代理插件**

Apache NetBeans 的 AI 插件，接入 Google Gemini（基于 gemini-java-client 1.1.2），以在 NetBeans JVM 内直接编写、编译并执行 LLM 生成的 Java 代码为主要机制；可在运行时从 Maven Central 下载所需库执行而不修改项目 pom.xml，支持 IDE 动作触发、构建、重构、Javadoc 读写，并通过 Prune-As-You-Go v2 算法管理上下文窗口。所有工具执行与代码变更需用户批准并可视化 diff 审查。面向 Java 开发者，Apache 2.0 许可（另附面向 AI 的 ASL 条款）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 NetBeans JVM 内编写、编译并执行 LLM 生成的 Java 代码
- 运行时从 Maven Central 下载依赖并立即使用，不改 pom.xml
- PAYG v2 上下文窗口动态管理算法
- 每次执行需用户批准并提供可视化 diff 审查

## 适用场景

- 在 NetBeans 中通过自然语言让 AI 执行 IDE 动作、构建与重构
- 让 AI 在 JVM 内做运行时诊断与堆分析
- 让 AI 下载并解析依赖源码进行解释

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L19: Anahata is an unprecedented, deeply integrated **Autonomous AI Agent** for the Apache NetBeans IDE. It's more than 
> L25: Anahata's main competitive advantage is its ability to **write, compile, and execute Java code directly within the 

## 星数曲线

```mermaid
xychart-beta
    title "anahata-os/anahata-netbeans-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-28 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `33bd53da2e16` · [字段定义](../../DATASET.md)*
