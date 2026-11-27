# sunnychase/lion-ai-studios

⭐ — · [GitHub]() · 个人维护

**为 NVIDIA DGX Spark 提供本地运行的 AI 视频/图像/音乐/配音生成工作室**

面向 DGX Spark 的本地媒体生成套件：Web 界面（单文件 Python、仅标准库）统一驱动 ComfyUI 渲染多种模型，产出带音轨的视频（最长 5 分钟分段拼接）、12 种图像模型与图像编辑、带歌词音乐与 MIDI 编曲、语音克隆与多说话人场景；内置视觉语言模型导演对每个片段打分并重拍一次。提供内存/温度守卫、任务队列、垃圾箱等管理功能。限制：要求 128 GB 统一内存的 GB10 硬件，核心模型约 150 GB，无云 API。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 视频与音效一体生成（MiniMax H3），分段拼接保留末帧与音频
- 从一段视频一次性克隆最多 6 个说话人声音（Qwen3-TTS + Whisper 校对）
- 视觉语言导演逐段审看、评分并重拍一次
- 内存守卫（低于阈值停渲染并停 ComfyUI）与 95 °C 温度暂停

## 适用场景

- 在 DGX Spark 上本地生成带音轨的短视频
- 为多人对话视频克隆并分配各自声音
- 文字描述编辑图像或生成海报/信息图
- 上传 MIDI 文件自动编排乐器与鼓组

## 场景标签

`图像生成` `视频生成` `语音合成` · 领域:内容生成

## 证据(README 行号)

> L5: Video with matching sound (MiniMax H3) · multi-shot films · cast scenes where several people talk in cloned voices (
> L105: |**Image**|Twelve image models behind one menu: **FLUX 3 Image Klein** (new: Black Forest Labs' 5.6B model with it

## 星数曲线

```mermaid
xychart-beta
    title "sunnychase/lion-ai-studios 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-15", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-08 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `6293a069c32b` · [字段定义](../../DATASET.md)*
