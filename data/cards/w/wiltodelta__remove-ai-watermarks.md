# wiltodelta/remove-ai-watermarks

⭐ 6,558 · Python · Apache-2.0 · 推送 2026-11-27 · [GitHub](https://github.com/wiltodelta/remove-ai-watermarks) · [官网](https://raiw.cc) · 个人维护

**清除自生成图像/视频/音频中可见与隐性 AI 水印及来源元数据的工具**

面向自生成内容的 AI 来源标记清理工具，以 Python 库、CLI 和 agent skill 三种形式提供。功能覆盖已知可见水印（如 Gemini 星标、23 种视频水印）的定位与修复填充、C2PA/EXIF/XMP/IPTC 等 AI 元数据剥离、兼容公共音频水印的检测与清理；隐性像素水印处理依赖扩散重生成，需 CUDA。另提供基于像素的 10 提供商来源分类（opt-in）。作者声明仅限对自拥有的内容合法使用，部分司法辖区限制移除 AI 标签。raiw.cc 以托管服务形式运行同一库。

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

- 23 种可见 AI 视频水印的选择性 GOP 流复制清除
- C2PA/EXIF/XMP/IPTC 元数据及 TC260 AIGC 标签识别与剥离
- 隐性水印经扩散重生成移除（CUDA 必需，Wan 2.1 可选后端）
- 音频兼容公共水印方案（AudioSeal/wavmark/perth 等）检测与清理

## 适用场景

- 清除自己生成的 Gemini/Sora/Veo 图片视频上的可见水印
- 批量剥离视频文件中的 AI 来源元数据标签
- 检测并清理兼容的公共音频水印并验证输出文件
- 为 agent 添加移除 AI 水印的技能

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: Remove AI provenance marks from images, video, and audio you generated yourself:
> L73: |Regenerate an image to disrupt invisible watermarks|`invisible`|Required (CUDA)|
> L40: > This is a research project on AI provenance signals, for lawful use on content

## 星数曲线

```mermaid
xychart-beta
    title "wiltodelta/remove-ai-watermarks 星数(近 27 点)"
    x-axis ["2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-11", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28"]
    y-axis "stars" 6071 --> 6602
    line [6121, 6142, 6152, 6169, 6180, 6221, 6227, 6243, 6115, 6317, 6340, 6353, 6361, 6377, 6388, 6401, 6415, 6432, 6447, 6462, 6473, 6480, 6483, 6490, 6520, 6540, 6558]
```

2026-10-26 6,121 → 2026-11-28 6,558（+437）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `12a8e6fb450c` · [字段定义](../../DATASET.md)*
