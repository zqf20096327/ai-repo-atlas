# ShirleyRex/assertify.io

⭐ 121 · TypeScript · 推送 2026-03-15 · [GitHub](https://github.com/ShirleyRex/assertify.io) · [官网](https://assertify.io) · 个人维护

**输入项目描述，AI 生成测试策略与多框架样板代码**

基于 Next.js 14 / TypeScript 的 Web 应用：用户输入项目描述后，应用自动分类并生成澄清问题，随后产出覆盖单元/集成/功能/性能/手工场景的测试套件与优先级标注，可为 Vitest、Jest、Pytest、JUnit 等 8 种框架生成样板代码，支持 JSON/CSV 导出与本地存储历史。支持 OpenAI、Anthropic、Gemini 三家 LLM，API key 以明文存于浏览器 sessionStorage。运行需自行 clone 源码并 npm install 启动开发服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 分析项目描述并生成澄清式追问（API 不可用时有回退问题列表）
- 覆盖单元/集成/功能/性能/手工测试并带优先级元数据
- 8 种测试框架的样板代码生成，可在设置中禁用指定框架
- OpenAI / Anthropic / Gemini 三家 LLM 可选

## 适用场景

- 为新项目快速生成测试策略与场景清单
- 为 Vitest/Jest/Pytest 等框架生成可直接使用的测试样板
- 导出 JSON/CSV 测试数据集用于规划或管理

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L7: Assertify is an intelligent testing assistant that analyzes your project description, asks clarifying questions, and
> L15: - **Boilerplate code generation** for eight popular frameworks, respecting the frameworks you disable in settings.

## 星数曲线

```mermaid
xychart-beta
    title "ShirleyRex/assertify.io 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-23"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-23 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `2e8ff2324a12` · [字段定义](../../DATASET.md)*
