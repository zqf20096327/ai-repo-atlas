# genesisinteractive/Spark-TTS-Unity

⭐ 43 · C# · Apache-2.0 · 推送 2026-09-19 · [GitHub](https://github.com/genesisinteractive/Spark-TTS-Unity) · 组织维护

**在 Unity 中离线运行 Spark-TTS 语音合成的 C# 包**

Spark-TTS 的 Unity 移植包：将原 PyTorch 模型转换为 ONNX，通过 com.github.asus4.onnxruntime 在设备上离线完成文本转语音。提供性别/音高/语速调节、参考音频声音克隆、三种内存模式（Performance 预加载约 3GB / Balanced / Optimal 适合移动端）与模型部署编辑器工具。需 Unity 6000.0.46f1+、至少 16GB RAM 与约 3GB 模型存储，支持 macOS/iOS，Windows 未测试。README 顶部声明本包已弃用，开发转向 Qwen3-TTS-Unity。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ONNX 模型在设备上离线推理，无需联网
- 声音克隆（参考音频）与性别/音高/语速风格调节
- 三种内存使用模式，覆盖桌面与移动场景
- 内置模型部署编辑器工具（FP16/FP32 精度选择）

## 适用场景

- 为独立游戏的对话内容生成语音
- 在应用中加入无障碍语音功能
- 用参考音频克隆特定音色做原型验证

## 场景标签

`语音合成` · 领域:内容生成

## 证据(README 行号)

> L10: Unity package for using Spark-TTS on-device models. This is a C# port of https://github.com/SparkAudio/Spark-TTS by
> L72: - On-device text-to-speech synthesis

## 星数曲线

```mermaid
xychart-beta
    title "genesisinteractive/Spark-TTS-Unity 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `848aef9a7896` · [字段定义](../../DATASET.md)*
