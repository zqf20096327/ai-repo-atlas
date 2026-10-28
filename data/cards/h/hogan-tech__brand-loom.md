# hogan-tech/brand-loom

⭐ 25 · Python · Apache-2.0 · 推送 2026-07-22 · [GitHub](https://github.com/hogan-tech/brand-loom) · [官网](https://neoxra.com) · 个人维护

**给营销内容创作者：任意模型上运行的营销技能库（钩子/文案/SEO）**

Python 营销技能库：提供 hook、caption、hashtags、repurpose、SEO 大纲、FAQ、schema.org 标记、CTA、中英翻译、LinkedIn 帖文等 10 项技能，可运行在 OpenAI/Anthropic/Gemini/Ollama 任意 provider 上（BYOK，一个环境变量切换），另有无需 key 的 fake provider。每项技能接受可选 brand_context（语气/受众/禁用短语），并以 SKILL.md 格式兼容 Claude Code/Cursor/OpenClaw 等 agent host。高级功能（语音自动提取、多平台编排、质量评分）位于托管产品 Neoxra，开源部分采用 Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 项营销技能覆盖 hook/caption/SEO/FAQ/schema.org/双语翻译等
- 四个真实 provider + fake provider，BYOK，env var 切换
- npx skills add 可作为 agent 技能安装到 Claude Code/Cursor 等 host
- CI 跑 provider parity eval，各技能跨模型产出格式校验结果

## 适用场景

- 为社媒与博客批量生成钩子文案、标签和 CTA
- 让 agent（Claude Code/Cursor 等）直接调用营销技能
- 本地 Ollama 或自有 API key 下离线/低成本生成内容

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L9: `brand-loom` is a library of **commodity marketing skills** — hooks, captions, hashtags, content repurposing,
> L10: SEO outlines, FAQs, schema.org markup, CTAs, bilingual translation, and LinkedIn posts — that run on **any LLM**
> L34: use_provider("fake")              # runs with zero keys; swap for "openai"/"anthropic"/"gemini"/"ollama"

## 星数曲线

```mermaid
xychart-beta
    title "hogan-tech/brand-loom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `06d0d3e606c2` · [字段定义](../../DATASET.md)*
