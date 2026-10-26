# proyecto26/slides-ai-plugin

⭐ 41 · TypeScript · MIT · 推送 2026-04-13 · [GitHub](https://github.com/proyecto26/slides-ai-plugin) · [官网](https://proyecto26.com/slides-ai-plugin/) · 组织维护

**Claude Code 幻灯片生成技能插件：一句话产出动画 HTML 或可编辑 PPTX**

面向 Claude Code 的技能/插件包，由 slide-design 编排技能驱动完整流程：内容发现、按时长索引规划结构、从 12 套风格预设中选样式、生成与校验。输出两种格式：单文件动画 HTML（GSAP + CSS、视口适配、Mermaid 图）与可编辑 .pptx（PptxGenJS + Bun、skia-canvas 字号自适应、布局重叠校验），均带演讲者备注；另提供 PPTX 转 HTML 的 Python 脚本。通过 npx skills、Claude Code 插件市场、git clone 等五种方式安装，运行时依赖首次运行自动安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- slide-design 技能编排：内容发现→结构规划→样式选择→生成→校验
- 单文件动画 HTML（GSAP/CSS、视口适配、可离线降级）与可编辑 PPTX 双格式
- 12 套风格预设、按时长索引的幻灯片结构与内容密度上限
- validateDeck 布局校验与 PostToolUse/Stop 自动校验钩子

## 适用场景

- 用自然语言让 Claude 生成会议演讲或路演幻灯片
- 把已有 PPTX 转成带动画的单文件 HTML 演示
- 按指定风格预设生成可编辑、带演讲备注的 .pptx

## 场景标签

 · 领域:AI 工具/演示生成

## 证据(README 行号)

> L11: **Turn any idea, outline, or existing deck into a professional presentation — straight from Claude Code.** Generate
> L74: That's it — the skill handles everything: content discovery, structure planning, style selection, slide generation,

## 星数曲线

```mermaid
xychart-beta
    title "proyecto26/slides-ai-plugin 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-26 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `78384d54a09a` · [字段定义](../../DATASET.md)*
