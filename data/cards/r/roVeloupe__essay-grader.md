# roVeloupe/essay-grader

⭐ 20 · JavaScript · 推送 2026-10-22 · [GitHub](https://github.com/roVeloupe/essay-grader) · [官网](https://github.com/roVeloupe/essay-grader/releases/latest) · 个人维护 · 中文 README

**面向中学语文教师的作文拍照识别与评分桌面工具**

Windows 桌面应用：教师拖入学生作文照片，经多模态模型逐句识别（含置信度与段落归属）、人工四态校对（正常/学生笔误/OCR修正/待核验）、内置初中记叙文（50分）与高中议论文（60分）评分模板打分，导出 Markdown/Word/PDF。内置 OpenCode Zen 免费模型通道（deepseek-v4.1-flash-free，备胎 minimax-m3.1-flash-free），无需 API key；v1 为 .NET 8/WinUI3 旧版，已停止维护。免费档有限流，连续批改可能等待 1–3 分钟。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 照片→逐句识别→四态校对→按评分量规打分的完整流水线
- 内置免费模型通道，无需 API key，主模型失败自动切换备胎
- 学生笔误只记录不改写，代码级 onlyHanSubstitutions 安全网兜底
- NSIS 安装包一键安装，数据本地存储于 %APPDATA%

## 适用场景

- 中学语文老师批改纸质作文并生成 Word 成绩单
- 保留学生原文笔误的前提下做评分量规打分
- 批量导入多页作文照片并合并批改

## 场景标签

`多模态` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: A desktop tool that takes **photos** of student essays and automates **recognition → review → rubric-based grading →
> L29: - **Sentence-level recognition**: the multimodal model returns the title, author, sentence-by-sentence body text, c
> L77: photo → base64 data URL → multimodal recognition (per sentence + confidence)

## 星数曲线

```mermaid
xychart-beta
    title "roVeloupe/essay-grader 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-26 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4b6bd2c9ff4c` · [字段定义](../../DATASET.md)*
