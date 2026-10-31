# android-com-pl/wp-ai-alt-generator

⭐ 20 · TypeScript · GPL-3.0 · 推送 2026-10-30 · [GitHub](https://github.com/android-com-pl/wp-ai-alt-generator) · [官网](https://wp.org/plugins/alt-text-generator-gpt-vision/) · 组织维护

**WordPress 插件：按需或批量生成图片替代文本**

基于 WordPress AI Client 的图片 alt 文本生成插件：支持手动生成、批量生成与上传时可选自动生成，需在后台配置带图像能力的 AI 提供商（OpenAI、Google Gemini、Anthropic Claude 等）。生成使用站点语言，可通过过滤器自定义 system/user 提示词、locale 与首选视觉模型列表（按顺序回退到任一兼容视觉模型）。要求 WordPress 7.0+ 与 PHP 8.1+，经插件目录或 Composer（wp-plugin/alt-text-generator-gpt-vision）安装，并集成 Polylang 语言检测。

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

- 按需、批量与上传时自动三种生成模式
- 通过 WordPress AI Client 接入 OpenAI/Gemini/Claude 等提供商
- 提示词、locale、首选视觉模型均可经 PHP 过滤器定制
- Polylang 集成自动检测图片或文章语言

## 适用场景

- 为 WordPress 媒体库批量补齐图片 alt 文本以提升无障碍与 SEO
- 上传图片时自动生成替代文本
- 多语言站点按图片/文章语言生成对应语言的 alt 文本

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L3: Generate image alt text in your site's language on demand or in bulk. Helps improve accessibility and SEO. Automatic
> L5: Uses the WordPress AI Client with your choice of AI provider, including OpenAI, Google Gemini, and Anthropic Claude.

## 星数曲线

```mermaid
xychart-beta
    title "android-com-pl/wp-ai-alt-generator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-31 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `643118e7b71a` · [字段定义](../../DATASET.md)*
