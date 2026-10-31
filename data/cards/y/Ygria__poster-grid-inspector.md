# Ygria/poster-grid-inspector

⭐ 13 · HTML · MIT · 推送 2026-08-20 · [GitHub](https://github.com/Ygria/poster-grid-inspector) · [官网](https://github.com/Ygria/poster-grid-inspector) · 个人维护 · 中文 README

**用视觉模型检测海报版式网格并导出 SVG/CSS 的 agent 技能**

以多模态视觉模型分析海报图片的版式网格系统：识别网格类型（瑞士模块、12/6/3 栏、基线网格、黄金分割等）、参数（栏/行/边距/间距，均为百分比坐标）、元素包围盒与关键线，并在图上叠加显示，可导出为 Figma/Illustrator 可用的分层 SVG 参考线或 CSS Grid / Tailwind 脚手架代码。模型无关，走 OpenAI 或 OpenAI 兼容接口（如 Qwen-VL），用原生 fetch、不依赖 AI SDK。整个仓库即一个可安装的 agent 技能目录（SKILL.md），宿主模型调用时无需 API key；可选的 Web UI/CLI 远程模式需本地 .env 配置 key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测网格类型/参数/元素包围盒/关键线，坐标为分辨率无关的百分比
- 导出分层 SVG（稳定图层 ID，可入 Figma/Illustrator）及 CSS Grid / Tailwind 代码
- 模型无关：OpenAI Responses API 与 OpenAI 兼容 Chat Completions，原生 fetch 实现
- 以可安装技能形式提供（SKILL.md/AGENTS.md），宿主模型模式无需 API key

## 适用场景

- 上传海报图，让视觉模型反推其版式网格系统
- 把分析结果导出为 Figma/Illustrator 参考线用于复刻或重构版式
- 把海报网格转成 CSS Grid / Tailwind 代码作为前端开发起点
- 作为 Claude Code 等 agent 的技能按需调用

## 场景标签

`代码生成` `多模态` · 领域:编码与开发

## 证据(README 行号)

> L20: Upload (or point an agent at) a poster image, and the tool uses a **multimodal vision model** to
> L38: It is **model-agnostic**: it works with **OpenAI** or any **OpenAI-compatible** multimodal model

## 星数曲线

```mermaid
xychart-beta
    title "Ygria/poster-grid-inspector 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-31"]
    y-axis "stars" 11 --> 14
    line [12, 13, 13]
```

2026-10-18 12 → 2026-10-31 13（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `29640145648c` · [字段定义](../../DATASET.md)*
