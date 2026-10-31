# Vrooli/Vrooli

⭐ 56 · Go · AGPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/Vrooli/Vrooli) · [官网](https://vrooli.com) · 组织维护

**本地自主 AI 开发团队：在你的硬件上生成完整应用**

自我托管的应用生成平台：用户用自然语言描述需求，系统编排 30+ 本地服务（数据库、AI 模型、UI 框架等）生成包含 UI、REST API、CLI 与数据库的完整应用。核心机制是场景（scenario）组合与修改保留系统——用户对 AI 生成代码的修改会被检测并保留，后续更新不覆盖。默认本地运行（含 Ollama 模型），也提供 vrooli.com 托管版本；AGPLv3 许可。限制：需自行管理本地服务器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言生成含 UI/API/CLI/数据库的完整应用
- 30+ 集成本地服务，初始设置后无外部 API 依赖
- 场景组合体系：核心/增强/平台/元四类场景模板
- 修改保留系统：AI 生成代码的人工改动被检测并永久保留

## 适用场景

- 在本地硬件上生成内部业务工具，数据不出网
- 医疗/金融等敏感行业在本地生成合规应用
- 生成个人生产力工具并通过增强场景逐步添加功能

## 场景标签

`代码生成` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L11: Vrooli is the first platform that lets you generate complete applications locally - UI, API, database, CLI - withou
> L90: 1. **Tell Vrooli What You Want**: Describe your application in plain English
> L92: 3. **Complete Application Generated**: Working software with UI, API, CLI, and database

## 星数曲线

```mermaid
xychart-beta
    title "Vrooli/Vrooli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-31 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `53e8ee856401` · [字段定义](../../DATASET.md)*
