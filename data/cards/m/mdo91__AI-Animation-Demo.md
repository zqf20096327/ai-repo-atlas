# mdo91/AI-Animation-Demo

⭐ 32 · Swift · MIT · 推送 2026-06-07 · [GitHub](https://github.com/mdo91/AI-Animation-Demo) · 个人维护

**SwiftUI iOS 演示应用：展示 AI 风格的微光文字与加载动画**

SwiftUI 编写的 iOS 演示 app，收录多种以 AI 产品界面为参照的加载/状态动画组件：Grok 风格彩色渐变微光文字、ChatGPT 风格灰度微光文字、通用 ShimmeringText、脉冲光球、总结/处理标签等。动画基于 TimelineView 实现，支持全渐变填充与高亮条扫过两种模式及 repeatDelay 暂停。组件可复制到其他 SwiftUI 项目使用。要求 Xcode 15+、iOS 17.0+、Swift 5，克隆仓库后用 Xcode 打开运行。本库只做动画呈现，不含任何 AI 模型调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 种动画演示：渐变微光文字、处理标签、脉冲光球等
- ShimmeringText 基于 TimelineView，支持全渐变与高亮条两种模式
- 组件可直接复制到其他 SwiftUI 项目

## 适用场景

- 给 iOS 应用添加 AI 处理中/思考中的状态动画
- 参考实现自定义微光文字与加载指示器

## 场景标签

 · 领域:移动端 UI/动画

## 证据(README 行号)

> L3: A SwiftUI iOS demo app showcasing AI-inspired loading and status animations — text shimmers, processing labels, and 
> L9: |**Grok style**|Vibrant blue → purple → pink gradient on bold text|Voice transcription, live streaming status|
> L10: |**ChatGPT style**|Monochrome gray gradient sweep, medium subheadline|“Thinking…” / reasoning labels|

## 星数曲线

```mermaid
xychart-beta
    title "mdo91/AI-Animation-Demo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `af2cd012aa43` · [字段定义](../../DATASET.md)*
