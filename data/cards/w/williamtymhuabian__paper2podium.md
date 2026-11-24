# williamtymhuabian/paper2podium

⭐ 3 · Python · NOASSERTION · 推送 2026-11-01 · [GitHub](https://github.com/williamtymhuabian/paper2podium) · 个人维护 · 中文 README

**把论文自动生成答辩/路演 PPT 的 AI 技能套装**

三个 SKILL.md 格式的 AI 演示技能集成套装，面向支持该格式的 AI 编码智能体（ZCode、Claude Code 等）。用户提供论文 PDF 并下达指令后，AI 依次执行读论文、caption 锚定图表提取（450 DPI 裁剪）、按学术/竞演/商业三套设计系统排版、注入讲稿，产出可登台的 pptx/PDF；另含 A0 海报与 3 分钟宣传片管线（edge-tts 配音、ffmpeg 推近、ASS/SRT 字幕）。渲染 QA 需 LibreOffice + poppler。中英双语，MIT 许可。

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

- caption 锚定算法提取论文图表，450 DPI 精准裁剪
- 学术/竞演/商业三套设计系统，逐页版式配方
- A0 海报与 3 分钟宣传片生成管线（edge-tts 配音 + 硬字幕）
- 构建后逐页 PNG 渲染，视觉模型验收溢出/重叠/变形

## 适用场景

- 把论文做成组会汇报或毕业答辩 PPT
- 为挑战杯/国创赛项目生成路演 deck
- 给公司展会做循环大屏与宣传物料
- 生成 A0 学术海报和会议投稿宣传片

## 场景标签

 · 领域:学术/办公自动化

## 证据(README 行号)

> L21: Paper2Podium 是三个 AI 演示技能（skill）的集成套装：你说「把这篇论文做成答辩 PPT」、
> L68: 面向支持 SKILL.md 格式的 AI 编码智能体（ZCode、Claude Code 等）：
> L78: 依赖：`pip install PyMuPDF python-pptx pillow qrcode[pil] edge-tts imageio-ffmpeg`；

## 星数曲线

```mermaid
xychart-beta
    title "williamtymhuabian/paper2podium 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-24"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-26 3 → 2026-11-24 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `47df79fe9df4` · [字段定义](../../DATASET.md)*
