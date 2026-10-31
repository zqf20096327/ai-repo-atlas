# hamza01055/hamza-voice-studio

⭐ 28 · Python · NOASSERTION · 推送 2026-10-11 · [GitHub](https://github.com/hamza01055/hamza-voice-studio) · 个人维护

**本地离线 TTS 语音制作工作室：写作、生成、多 take 编辑与导出**

面向本地优先用户的语音制作应用：编写与组织脚本，用本地安装的 Kokoro-82M 模型（经 sherpa-onnx 在 CPU 上运行）生成语音，按段落比较多 take、重生成单个片段，组装长篇朗读并导出 WAV/MP3。支持乌尔都语等 RTL 文本编辑、文本规范化预览、独立 worker 进程的任务队列（进度/取消/崩溃恢复）、语音库与模型管理器（离线可用、校验和固定下载）。v0.1.0 仅在 Linux x86-64 测试，Windows 未测；语音克隆、转写验证等尚未提供。需 Python 3.11、Node.js 20+、FFmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Kokoro-82M v1.0 本地 CPU 语音生成（53 个内置音色）
- 每片段多 take 比较、选择与编辑后过期检测
- 独立 worker 进程的持久任务队列（进度/取消/崩溃恢复/SSE）
- Unicode 与 RTL 编辑（乌尔都语、混排）及文本规范化预览

## 适用场景

- 离线制作有声书或长篇朗读并导出 WAV/MP3
- 逐段生成、比较多个录音 take 后挑选组装
- 隐私敏感、无 GPU 环境下的本地语音合成

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L3: A local-first AI voice-production studio: write and organise scripts, generate speech with
> L23: - Real speech generation with **Kokoro-82M v1.0** (Apache-2.0 weights) via sherpa-onnx on CPU:

## 星数曲线

```mermaid
xychart-beta
    title "hamza01055/hamza-voice-studio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-31 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `68144984e2f3` · [字段定义](../../DATASET.md)*
