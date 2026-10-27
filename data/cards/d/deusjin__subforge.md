# deusjin/subforge

⭐ 104 · Rust · MIT · 推送 2026-09-02 · [GitHub](https://github.com/deusjin/subforge) · [官网](https://github.com/deusjin/subforge#readme) · 个人维护 · 中文 README

**Rust CLI：把视频字幕转写、翻译、质检与压制整合为可复现管线**

面向反复处理视频的字幕生产 CLI 工具：以 faster-whisper 本地转写（CPU/CUDA）、SaT 切分、Google/Bing/OpenAI 兼容 LLM 翻译、GEMBA-MQM 质量估计与 ffmpeg 硬烧/软封装组成完整管线，支持批量处理、术语提取、项目级翻译记忆与缓存/模型管理。通过 cargo install 从源码构建，需 Rust 1.88+、Python 3.9+ 与 ffmpeg；当前版本 0.2.0，自述尚处早期，预编译二进制未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- faster-whisper 本地转写，CPU/CUDA 可选 GPU 绑定
- Google/Bing/OpenAI 兼容 LLM 翻译后端，链式与波次并发两种模式
- GEMBA-MQM 质量估计与低分重译，SubER/WER/BLEU 等评估指标
- ffmpeg 硬烧/软封装双语字幕，支持批量与翻译记忆

## 适用场景

- 批量给课程或创作者视频生成翻译字幕并压制成品
- 本地自动化跑通转写→切分→翻译→质检→封装的字幕流水线
- 对字幕产出做质量评估与低分片段重译

## 场景标签

`语音识别` · 领域:感知与多模态

## 证据(README 行号)

> L9: SubForge is a Rust CLI for transcribing, segmenting, translating, evaluating,
> L16:   -> speech recognition
> L45: - Local `faster-whisper` transcription with CPU or CUDA support

## 星数曲线

```mermaid
xychart-beta
    title "deusjin/subforge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 103 --> 105
    line [104, 104]
```

2026-10-18 104 → 2026-10-27 104（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `a231b1996a5a` · [字段定义](../../DATASET.md)*
