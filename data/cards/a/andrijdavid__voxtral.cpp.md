# andrijdavid/voxtral.cpp

⭐ 37 · C++ · MIT · 推送 2026-06-19 · [GitHub](https://github.com/andrijdavid/voxtral.cpp) · 个人维护

**Mistral Voxtral 语音转录模型的 C/C++ (ggml) 实现**

基于 ggml 的 C++ 实现，移植 Mistral 的 Voxtral 语音转文字模型，支持两个模型家族：Voxtral-Mini-4B-Realtime（流式，每 80ms 音频帧产出一个 token，面向低延迟/长音频）与 Voxtral-Mini-3B-2507（离线批转录）。提供 Python 脚本从官方 checkpoint 转 GGUF，附带原生量化工具（Q2_K 至 Q8_0 等多种格式），GPU 自动检测 Metal/CUDA/Vulkan 并可回退 CPU。输入须为 16kHz 单声道 16-bit PCM WAV，可用 ffmpeg 转换。面向希望在本地运行 Voxtral 推理的开发者，通过 CMake 编译或 Homebrew 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持流式（Realtime）与离线（Whisper 式）两种 Voxtral 模型
- GGUF 转换脚本与原生量化工具（Q2_K–Q8_0、Q4_K_M 混合策略）
- GPU 自动检测：Metal / CUDA / Vulkan，可回退 CPU
- 提供与参考实现的数值一致性测试（容差可经环境变量覆盖）

## 适用场景

- 在本地 CPU/GPU 上离线转录音频文件
- 低延迟长音频的流式语音识别
- 将官方 Voxtral 权重转换为量化 GGUF 并部署

## 场景标签

`语音识别` `推理引擎` · 领域:感知与多模态

## 证据(README 行号)

> L3: A ggml-based C++ implementation of Voxtral.
> L9: - **Voxtral-Mini-4B-Realtime** (`general.architecture = voxtral_realtime`) - streaming
> L12:  generates only the text tokens (Whisper-style), much faster for batch transcription of

## 星数曲线

```mermaid
xychart-beta
    title "andrijdavid/voxtral.cpp 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-25 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b427e71e4a3c` · [字段定义](../../DATASET.md)*
