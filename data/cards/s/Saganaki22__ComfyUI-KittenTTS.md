# Saganaki22/ComfyUI-KittenTTS

⭐ 10 · Python · Apache-2.0 · 推送 2026-03-04 · [GitHub](https://github.com/Saganaki22/ComfyUI-KittenTTS) · [官网](https://huggingface.co/KittenML) · 个人维护

**ComfyUI 自定义节点：运行轻量 TTS 模型 KittenTTS 合成语音**

为 ComfyUI 提供的 KittenTTS 自定义节点，将 KittenTTS 文本转语音模型接入 ComfyUI 工作流。提供单节点界面，含模型选择（19MB-80MB 四档）、8 种内置音色、语速调节、立体声输出与自定义 HuggingFace 模型 ID 输入。模型自动下载并缓存于 ComfyUI/models/kittentts/。需预先安装 espeak-ng 并设置 PHONEMIZER_ESPEAK_LIBRARY 环境变量。依赖 onnxruntime，按环境是否支持 CUDA 自动选择 CPU 或 GPU 版本。通过 ComfyUI Manager 或 git clone 安装，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 4 个模型档位（15M-80M 参数，19MB-80MB）
- 支持 CUDA 与 CPU 运行，GPU 可选
- 单节点集成全部设置，8 种内置音色（4 男 4 女）
- 模型自动下载并缓存到 ComfyUI 模型目录

## 适用场景

- 在 ComfyUI 工作流中为视频/音频管线合成语音
- 在无 GPU 的 CPU 环境下运行文本转语音
- 通过自定义 HuggingFace 模型 ID 加载其他 KittenTTS 模型

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L7: A simple ComfyUI custom node for KittenTTS - an ultra-lightweight text-to-speech model. Works on **CUDA** and **CPU*
> L21: - ⚡ **Fast inference**: Real-time speech synthesis

## 星数曲线

```mermaid
xychart-beta
    title "Saganaki22/ComfyUI-KittenTTS 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `838704d4e8b9` · [字段定义](../../DATASET.md)*
