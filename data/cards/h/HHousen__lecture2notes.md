# HHousen/lecture2notes

⭐ 67 · Jupyter Notebook · AGPL-3.0 · 推送 2026-07-02 · [GitHub](https://github.com/HHousen/lecture2notes) · [官网](https://lecture2notes.com/) · 个人维护

**将课程讲座视频自动转换为格式化笔记的研究代码**

研究项目 Lecture2Notes 的配套代码：解析讲座视频的视觉与听觉内容，先用深度 CNN 幻灯片分类器提取关键帧，经透视裁剪、聚类去重、OCR 结构分析得到幻灯片转录文本，再对音频做语音转写，最后用抽取式与生成式摘要（自研 TransformerSum 库，也可用 BART/PEGASUS）合并生成 HTML/Markdown/TXT 等格式的笔记，支持一条命令端到端完成。面向学生与教育场景，附网站 lecture2notes.com 可处理用户视频；README 指出语音转写与部分摘要方法是已知薄弱点。采用 AGPL-3.0 许可，未在 README 内给出安装命令，需查阅文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 深度 CNN 幻灯片分类器提取并聚类去重关键帧
- OCR 幻灯片结构分析生成含插图的格式化转录
- TransformerSum 训练/推理库做长文本摘要，可换用 BART/PEGASUS
- 一条命令端到端输出 HTML/TXT/Markdown 笔记

## 适用场景

- 学生把讲座录像快速转成可复习的笔记
- 研究者复现或扩展多模态讲座摘要流程
- 教育内容制作者批量生成课程文字版

## 场景标签

`语音识别` `多模态` `OCR` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L9: **Lecture2Notes** is a project that **summarizes lectures videos**. At a high level, it parses both the **visual** a
> L17: Note-taking is a universal activity among students because of its benefits to the learning process. This research f

## 星数曲线

```mermaid
xychart-beta
    title "HHousen/lecture2notes 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 66 --> 68
    line [67, 67]
```

2026-10-18 67 → 2026-10-29 67（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `19c92386385a` · [字段定义](../../DATASET.md)*
