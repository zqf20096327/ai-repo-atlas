# dakjdakd/PPT-Design-DNA

⭐ 30 · JavaScript · Apache-2.0 · 推送 2026-10-15 · [GitHub](https://github.com/dakjdakd/PPT-Design-DNA) · 个人维护 · 中文 README

**把参考图/设计简报转为可复用视觉系统并生成 HTML 演示的 AI 技能**

面向 AI host（如 Codex）安装的 agent 技能：从参考图片或设计简报中提取构图、排版、色彩、质感、密度与动效，形成 Design DNA，经用户确认后生成固定 16:9 舞台的 HTML 演示文稿；无参考图时可进行 Design Discovery 探索候选视觉方向。产出的视觉系统可保存为带版本的 Design Profile 跨演示复用，含现有演示翻新、场景适配与源级布局校验，可选 PDF/PPTX 导出（依赖宿主支持）。以 git clone 到用户技能目录方式安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从参考图提取 Design DNA（五层：Mood/Composition/Visual/Content Strategy/Presentation）
- Design Profile 保存、版本化与跨演示复用视觉系统
- 无参考图时基于设计简报探索候选视觉方向（Design Discovery）
- 固定 16:9 HTML 舞台输出，可选 PDF/PPTX 导出

## 适用场景

- 我有喜欢的风格参考图，想生成同风格的演示文稿
- 团队沉淀统一的视觉系统，在多份演示中复用
- 没有参考图，让 AI 从设计简报探索几个视觉方向再定稿
- 把已有演示按新视觉系统翻新或转换

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L14: **PPT-Design-DNA** is an AI skill that turns reference imagery or a design brief into a visual system for HTML pres
> L36: For a local Codex installation, clone the repository into your user skills directory.

## 星数曲线

```mermaid
xychart-beta
    title "dakjdakd/PPT-Design-DNA 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-26 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `3eaad85cb4c6` · [字段定义](../../DATASET.md)*
