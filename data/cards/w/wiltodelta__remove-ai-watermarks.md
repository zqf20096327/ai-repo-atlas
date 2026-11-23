# wiltodelta/remove-ai-watermarks

⭐ 6,483 · Python · Apache-2.0 · 推送 2026-11-22 · [GitHub](https://github.com/wiltodelta/remove-ai-watermarks) · [官网](https://raiw.cc) · 个人维护 · 中文 README

**清除图像/音视频 AI 水印与溯源元数据的 Python 库和 CLI**

面向自生成内容的 AI 溯源标记处理工具，覆盖四类对象：可见 AI 标记（Gemini sparkle、Sora、Veo、Seedance、豆包、海螺、可灵等）、不可见像素水印（局部破坏或扩散重生成）、兼容的公开音频水印（AudioSeal/WavMark/Perth 等，带源解码与输出校验）、C2PA/EXIF/XMP/IPTC 等 AI 元数据。以 Python 库、CLI 与 agent skill 三种形式提供，功能按 extras 组合安装；不可见水印去除需 CUDA，文本水印重写可走本地 Transformers 或 Ollama。声明仅限自有内容 lawful 使用，并提示部分地区限制去除 AI 标签。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 图像、视频、音频、文本四类 AI 水印与 C2PA/EXIF/XMP 元数据清除
- 从像素做 10 提供商来源分类的 opt-in 分类器（CPU 可运行，会弃权）
- 按功能拆分的 PyPI extras 安装体系（visible/video/audio/text/source-classify 等）
- agent skill 可装入 Claude Code、Codex、Cursor 等工具

## 适用场景

- 清除自己生成的图片中的 Gemini 可见水印与元数据
- 批量处理视频目录，去除可见标记并剥离 AIGC 元数据
- 检查音频中是否存在兼容的公开水印并验证输出文件

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L53: |Strip AI metadata|`metadata`|No|
> L71: |Regenerate an image to disrupt invisible watermarks|`invisible`|Required (CUDA)|
> L83: locally served Ollama model. Review generated prose for factual fidelity.

## 星数曲线

```mermaid
xychart-beta
    title "wiltodelta/remove-ai-watermarks 星数(近 28 点)"
    x-axis ["2026-10-21", "2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23"]
    y-axis "stars" 6017 --> 6525
    line [6059, 6076, 6092, 6106, 6115, 6121, 6142, 6152, 6169, 6180, 6221, 6227, 6243, 6115, 6317, 6340, 6353, 6361, 6377, 6388, 6401, 6415, 6432, 6447, 6462, 6473, 6480, 6483]
```

2026-10-21 6,059 → 2026-11-23 6,483（+424）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-23 · 置信度 high · 依据 README sha `f8ec60419234` · [字段定义](../../DATASET.md)*
