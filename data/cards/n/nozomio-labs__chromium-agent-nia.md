# nozomio-labs/chromium-agent-nia

⭐ 22 · TypeScript · NOASSERTION · 推送 2025-12-20 · [GitHub](https://github.com/nozomio-labs/chromium-agent-nia) · [官网](https://chromium.trynia.ai/) · 组织维护

**基于 Nia 的 Chromium 代码库问答 AI agent**

面向 Chromium 开发者/研究者的问答 agent：在用户已索引的 Chromium 仓库与文档上作答，答案以索引内容为依据。通过 Nia API 与 AI 网关运行，需配置 NIA_API_KEY、AI_GATEWAY_API_KEY 及指向 Chromium 仓库/文档数据源的 ID。使用 Bun 安装依赖并运行开发服务。README 仅含快速开始说明，其余详见 docs.trynia.ai。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于已索引的 Chromium 仓库与文档作答
- 通过 Nia 数据源 ID 指定问答范围
- Bun 安装与开发运行流程

## 适用场景

- 在 Chromium 大型代码库中查找代码实现依据
- 针对 Chromium 文档提问并得到有据回答

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: AI agent that answers questions grounded in your indexed **Chromium repository + documentation**. Powered by Nia.
> L9:  - `NIA_API_KEY` - Get from trynia.ai

## 星数曲线

```mermaid
xychart-beta
    title "nozomio-labs/chromium-agent-nia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `36185e5a4b7d` · [字段定义](../../DATASET.md)*
