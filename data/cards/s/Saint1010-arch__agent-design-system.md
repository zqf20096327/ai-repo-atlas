# Saint1010-arch/agent-design-system

⭐ 89 · MIT · 推送 2026-04-01 · [GitHub](https://github.com/Saint1010-arch/agent-design-system) · 个人维护 · 中文 README

**AI Agent 角色配置的设计方法论与模板体系（五层架构）**

一套用于批量设计、质检与部署 AI Agent 角色配置的 Markdown 模板与方法论文档集合：以五层架构模板（Profile/Soul/Knowledge/Methodology/Protocol）为骨架，配生产手册 SOP、质检清单、角色矩阵与 Agent 设计方法论。核心章节"审美工程"提供 8 种工程手段与 3 种检测方法，用于区分 AI 模拟理解与真正理解。支持三种用法：配合 OpenClaw 作为 workspace 文件使用、把配置粘贴到 ChatGPT/Claude 等平台、或直接阅读学习。全部为 Markdown 文本，无需编程。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 五层架构模板（Profile→Soul→Knowledge→Methodology→Protocol）
- 审美工程：8 种工程手段 + 3 种检测方法（删除/替换/追问测试）
- 生产手册 SOP 与质检清单，覆盖从需求到交付流程
- 方法论来源可追溯（Anthropic/OpenAI/LangChain 最佳实践等）

## 适用场景

- 按模板和 SOP 设计一个可上架的专家级 Agent 配置
- 给已有的 OpenClaw 龙虾批量生产子 Agent
- 用质检清单在交付前检查 Agent 配置漏洞
- 学习 Agent 设计方法论与虚假表现检测思想

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L7: 这个项目提供的是：**一套经过体系化设计的 Agent 生产系统**，让你能批量生产**产品级、可上架、经过质检**的 AI Agent 角色配置。
> L11: - 🏗️ **用五层架构模板** 设计任何领域的专家级 Agent（Profile → Soul → Knowledge → Methodology → Protocol）
> L67: |`templates/生产手册.md`|从需求到交付的完整 SOP 流程|**最先读**——了解完整流程|✅ 第一次用时必读|

## 星数曲线

```mermaid
xychart-beta
    title "Saint1010-arch/agent-design-system 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 88 --> 90
    line [89, 89]
```

2026-10-18 89 → 2026-10-30 89（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1943b5cf16b8` · [字段定义](../../DATASET.md)*
