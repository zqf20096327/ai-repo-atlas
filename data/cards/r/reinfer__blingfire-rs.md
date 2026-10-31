# reinfer/blingfire-rs

⭐ 15 · Rust · MIT · 推送 2026-06-23 · [GitHub](https://github.com/reinfer/blingfire-rs) · 组织维护

**BlingFire 分词库的 Rust 封装：文本转词/句**

对微软 BlingFire 分词库的薄封装 crate，以 Rust 提供 text_to_words 与 text_to_sentences 两个函数，分别将文本切分为词与句子。开发者通过 cargo add blingfire 加入 Cargo.toml 即可使用，代码以 MIT 许可发布。README 仅说明函数签名与基础用法示例，未涉及模型加载或额外配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 BlingFire 分词库，暴露两个函数
- 提供 text_to_words 与 text_to_sentences 文本切分
- cargo add 一行安装，MIT 许可

## 适用场景

- Rust 项目中做词级或句级文本切分
- NLP 流水线前置的分句与分词处理

## 场景标签

 · 领域:NLP/文本处理

## 证据(README 行号)

> L7: `blingfire` is a thin Rust wrapper for the BlingFire tokenization library.
> L14: The library exposes two functions `text_to_words` and `text_to_sentences`

## 星数曲线

```mermaid
xychart-beta
    title "reinfer/blingfire-rs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 mid · 依据 README sha `c0243669f464` · [字段定义](../../DATASET.md)*
