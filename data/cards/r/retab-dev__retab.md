# retab-dev/retab

⭐ 45 · Go · 推送 2026-10-04 · [GitHub](https://github.com/retab-dev/retab) · [官网](https://www.retab.com) · 组织维护

**面向开发者的 LLM 文档处理平台与 SDK**

Retab 提供文档处理平台及 Python/Node/Go SDK：基于 LLM 读取文档并按 schema 返回结构化数据，提供预处理、提示与抽取 schema 生成、针对多模型的适配，以及 Projects 评估流程（对已知标注数据测量准确率、迭代优化 schema 后部署）。使用需注册获取 API key（Bearer 认证），平台侧配置，SDK 驱动评估与集成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM-first 文档抽取：给文档和 schema 即返回结构化数据
- 支持生成适配所用模型提供商的提示与抽取 schema
- Projects 评估工作流：测量字段准确率并迭代优化 schema
- 提供 Python / Node / Go 三种语言 SDK

## 适用场景

- 从发票、表单等文档中自动抽取结构化字段
- 对抽取 schema 做准确率评估与迭代优化
- 在现有代码库中集成文档处理自动化

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L13: Retab is the complete developer platform and SDK for shipping state-of-the-art document processing in the age of LL
> L17: For this mission, we provide the best-in-class preprocessing, help you generate prompts & extraction schemas that f

## 星数曲线

```mermaid
xychart-beta
    title "retab-dev/retab 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-26 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `19f77c915547` · [字段定义](../../DATASET.md)*
