# nozomio-labs/paulgraham-ai

⭐ 43 · TypeScript · NOASSERTION · 推送 2025-12-07 · [GitHub](https://github.com/nozomio-labs/paulgraham-ai) · [官网](https://www.paulgraham-nia.com/) · 组织维护

**基于 Paul Graham 文章回答问题的 AI 问答 agent**

由 nozomio-labs 开发的 AI 问答 agent：以 Paul Graham 的 120+ 篇文章为语料，回答关于创业、写作、技术与生活的问题。底层接入 Nia API（需 trynia.ai 的 API key）并经 AI Gateway 使用自选 AI provider 的 key；语料源通过 Nia 的 /explore 预索引来源添加。以仓库形式提供，需复制 .env.example 配置环境变量，用 bun install 安装依赖并 bun run dev 运行，文档见 docs.trynia.ai。

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

- 回答以 120+ 篇 Paul Graham 文章为依据
- 通过 Nia API 提供索引与检索底座
- 支持配置自有 AI provider key（AI_GATEWAY_API_KEY）

## 适用场景

- 向 AI 询问 Paul Graham 关于创业与写作的观点
- 基于其文章语料获得有出处的回答

## 场景标签

`文档问答` · 领域:知识与检索

## 证据(README 行号)

> L3: AI agent that answers questions grounded in 120+ Paul Graham essays. Powered by Nia.
> L9:  - `NIA_API_KEY` - Get from trynia.ai

## 星数曲线

```mermaid
xychart-beta
    title "nozomio-labs/paulgraham-ai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-31 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `eea2f0cba5f9` · [字段定义](../../DATASET.md)*
