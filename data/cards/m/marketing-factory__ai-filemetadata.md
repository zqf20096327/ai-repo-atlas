# marketing-factory/ai-filemetadata

⭐ 14 · PHP · GPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/marketing-factory/ai-filemetadata) · [官网](https://www.marketing-factory.de) · 组织维护

**TYPO3 扩展：用 OpenAI 自动为图片生成替代文本**

面向 TYPO3 CMS（v12+，PHP 8.2+）的扩展，调用 OpenAI API（默认 gpt-4o-mini，可换其他支持图像处理的模型）为 FAL 文件管理中的图片自动生成替代文本，服务无障碍需求（EU 2019/882 / BFSG）与屏幕阅读器用户，不用于 SEO 文本。支持自定义提示词、按文件夹的语言映射、排除目录、发送前将图片缩放至 512px 以降低 token 成本，提供 CLI 命令批量生成。图像数据会发送至外部 AI 服务，README 提示需核查隐私政策与图片许可条款。

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

- 调用 OpenAI 视觉模型为图片自动生成替代文本（默认 gpt-4o-mini）
- 可自定义提示词并按语言映射生成多语言替代文本
- 图片缩放至 512x512px 以降低 token 成本
- 提供 bin/typo3 ai:generate-alt-texts CLI 批量生成

## 适用场景

- TYPO3 站点批量补齐图片替代文本以满足无障碍法规
- 为视障用户与屏幕阅读器提供图片描述
- 通过自定义提示词控制替代文本的语言与风格

## 场景标签

 · 领域:CMS 扩展/无障碍

## 证据(README 行号)

> L3: Automatically generates FAL metadata (alternative texts, for the time being) for files by means of public LLMs.
> L7: The extension generates descriptive text for images, making them accessible to visually impaired individuals,

## 星数曲线

```mermaid
xychart-beta
    title "marketing-factory/ai-filemetadata 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3f0942768096` · [字段定义](../../DATASET.md)*
