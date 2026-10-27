# gongnyang/deck-factory

⭐ 78 · CSS · MIT · 推送 2026-07-15 · [GitHub](https://github.com/gongnyang/deck-factory) · [官网](https://github.com/kimsh-1/deck-factory) · 个人维护 · 中文 README

**Claude Code 技能：一句话生成编辑风格 HTML 演示文稿**

面向 Claude Code 的插件/技能，输入一句意图描述，按内置设计系统（暗色/纸光双配置、no_box 结构、巨号数字、四角 chrome、Pretendard 字体、CJK 安全换行）生成 HTML/CSS 幻灯片，经 Chromium 引擎渲染并可导出 PNG/PDF/PPTX，含 47 项确定性检查、90 分合格线的质量门。设计系统与技能当前可用，已交付 12 张幻灯片与 3 支动效影片；端到端全自动管线尚在开发中，自动评分待校准。通过 Claude Code 插件市场安装，另含 8 种风格预设。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 一句话意图生成暗色/纸光双配置的编辑风格幻灯片
- 47 项确定性检查、90 分合格线与 7 项硬性失败阈值的质量门
- 真实 Chromium 渲染，所见即所导出（PNG/PDF/PPTX）
- 8 种风格预设与 CJK 安全换行规则

## 适用场景

- 用一句需求描述快速生成可演示的 HTML 幻灯片
- 在 Claude Code 中按预设风格批量定制演示文稿
- 将幻灯片导出为 PDF 分享版或 PPTX 文件

## 场景标签

 · 领域:演示文稿生成/设计工具

## 证据(README 行号)

> L9: Claude Code Skill
> L27: ```bash
> L72: 3. **compose** — deterministically assemble slides from a fixed layout vocabulary (the model writes content; code o

## 星数曲线

```mermaid
xychart-beta
    title "gongnyang/deck-factory 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-27 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `005f5200b680` · [字段定义](../../DATASET.md)*
