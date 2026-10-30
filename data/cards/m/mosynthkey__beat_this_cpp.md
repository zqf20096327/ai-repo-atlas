# mosynthkey/beat_this_cpp

⭐ 15 · C++ · MIT · 推送 2026-07-01 · [GitHub](https://github.com/mosynthkey/beat_this_cpp) · 个人维护

**给开发者的 C++ 音乐节拍检测器：transformer 模型定位节拍与强拍**

将 JKU Linz 发表于 ISMIR 2024 的 Beat This! 节拍追踪系统移植为 C++ 实现：读取 WAV/FLAC/OGG/MP3 音频，经重采样与 128 维 Mel 频谱计算后，用内置 ONNX transformer 模型输出节拍与强拍概率，支持峰值检测或 madmom 兼容的 DBN/Viterbi 后处理两种模式。输出形式包括 .beats 时间戳文件、880/440Hz 音频打点轨及与原曲混合的音频。支持 macOS 与 Windows，通过 CMake 从源码构建，同时提供 C++ API。仓库内附带已转换的约 97MB ONNX 模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- transformer 模型经 ONNX Runtime 推理，检测节拍与强拍
- 可选 madmom 兼容 DBN（HMM+Viterbi）后处理
- 输出 .beats 文件、click 音轨或原曲混合音频三种形式
- 附带预转换 ONNX 模型（约 97MB），提供 C++ API 与 CLI

## 适用场景

- 为音乐文件批量生成节拍/强拍时间标注
- 生成带打点音的试听音频核验节拍检测结果
- 在其他 C++ 应用中集成节拍检测能力

## 场景标签

 · 领域:音频/音乐信息检索

## 证据(README 行号)

> L7: This is a C++ implementation of the Beat This! model, originally published at ISMIR 2024. The system uses a transfor
> L29: 4. **AI Inference**: Run the transformer model in chunks (1500 frames, 6-frame border) via ONNX Runtime

## 星数曲线

```mermaid
xychart-beta
    title "mosynthkey/beat_this_cpp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5203f9fc0414` · [字段定义](../../DATASET.md)*
