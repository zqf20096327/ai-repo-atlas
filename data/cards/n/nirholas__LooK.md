# nirholas/LooK

⭐ 26 · JavaScript · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/nirholas/LooK) · [官网](https://loook-production.up.railway.app/) · 个人维护

**把网站自动生成带 AI 解说的产品演示视频的 CLI 工具**

面向开发者的 Node.js 命令行工具：输入网站 URL，录制浏览器操作（60fps、光标特效、智能缩放），用 GPT-4 Vision 分析界面生成解说脚本，再用 OpenAI TTS 配音，导出适配 YouTube/Twitter 等平台的成品视频。支持多页 walkthrough、可视化 Web 编辑器、Android 应用录制（Docker 模拟器）。运行需 Node.js 18+、FFmpeg 和 OpenAI API key；源码许可为 All rights reserved（非典型开源许可）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- URL→截图→GPT-4V 分析→脚本→录制→配音→导出的自动流水线
- AI 自动探索多页站点并生成连贯叙事（walkthrough）
- 光标特效、智能缩放、字幕、转场、GIF/多平台导出预设
- 通过 Docker+Appium 录制 Android 应用演示

## 适用场景

- 给我的 SaaS 产品快速生成发布用的演示视频
- 让 AI 自动探索整个网站并产出多页连贯讲解
- 为移动端应用录制带解说的演示

## 场景标签

 · 领域:开发者工具/视频生成

## 证据(README 行号)

> L44: 2. **Analyzes** the UI using GPT-4 Vision
> L46: 4. **Narrates** with natural AI voice

## 星数曲线

```mermaid
xychart-beta
    title "nirholas/LooK 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 24 --> 27
    line [25, 26, 26]
```

2026-10-18 25 → 2026-10-28 26（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `13d3e80bec84` · [字段定义](../../DATASET.md)*
