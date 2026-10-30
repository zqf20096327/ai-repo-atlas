# ssmall256/mlx-audio-separator

⭐ 18 · Python · MIT · 推送 2026-10-02 · [GitHub](https://github.com/ssmall256/mlx-audio-separator) · 个人维护

**Apple Silicon 上 MLX 原生的人声/伴奏分轨工具**

将 audio-separator（nomadkaraoke/python-audio-separator）的推理路径移植到 MLX，使 Demucs、MDX、MDXC、VR、Roformer 等模型的音轨分离可在 Apple Silicon 上运行，推理时不依赖 PyTorch 或 ONNX Runtime。提供 CLI 与 Python API，首次运行可将上游 checkpoint 转换为 MLX 权重（safetensors 缓存，含校验机制），预转换模型可从 Hugging Face 下载。限制：需 macOS 13+ 与 Apple Silicon（M1-M4）、Python 3.10+；性能数字仅限标注的基准设置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Roformer/MDXC/MDX/VR/Demucs 五类分离架构
- MLX 原生推理，无需 PyTorch 或 ONNX Runtime
- checkpoint 转换为 safetensors 缓存并做文件匹配校验，旧 pkl 缓存不被反序列化
- 发布验证快照：163/163 模型通过，与上游 parity smoke 4/4 通过

## 适用场景

- 在 Mac 上把歌曲拆分成人声与伴奏音轨
- 首次运行时将已有 Demucs/MDX checkpoint 转换为 MLX 格式使用
- 做卡拉OK或混音前的素材分离

## 场景标签

 · 领域:音频处理/音乐源分离

## 证据(README 行号)

> L3: MLX-native stem separation for Apple Silicon Macs.
> L5: This project ports the inference paths from audio-separator (upstream repo: nomadkaraoke/python-audio-separator) to 
> L44: outputs = sep.separate("song.mp3")

## 星数曲线

```mermaid
xychart-beta
    title "ssmall256/mlx-audio-separator 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-30"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-30 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `3babb212ed47` · [字段定义](../../DATASET.md)*
