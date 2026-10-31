# beekeeper-studio/bks-ai-shell

⭐ 13 · TypeScript · GPL-3.0 · 推送 2026-10-28 · [GitHub](https://github.com/beekeeper-studio/bks-ai-shell) · 组织维护

**Beekeeper Studio 插件：用 AI 分析数据库并生成 SQL 查询**

Beekeeper Studio 5.3+ 的插件，提供对话式界面，让用户向 AI 提问以分析数据库结构并生成 SQL 查询。通过 Anthropic API 实现模型调用；README 的 Security Note 指出使用 anthropic-dangerous-direct-browser-access: true 头在浏览器中直接调用 Anthropic API，并提示该方式会在生产环境暴露 API key。开发方式为 git clone 后 yarn build 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话式 AI 分析数据库并生成 SQL 查询
- 以插件形式集成到 Beekeeper Studio 5.3+
- 基于 Anthropic API 的模型调用

## 适用场景

- 在 Beekeeper Studio 内通过对话生成 SQL 查询
- 让 AI 分析数据库结构辅助写查询

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L3: Ask AI to analyze your database and generate SQL queries.
> L28: This application uses the `anthropic-dangerous-direct-browser-access: true` header to enable browser usage of the A

## 星数曲线

```mermaid
xychart-beta
    title "beekeeper-studio/bks-ai-shell 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `d82b5e4f3c9b` · [字段定义](../../DATASET.md)*
