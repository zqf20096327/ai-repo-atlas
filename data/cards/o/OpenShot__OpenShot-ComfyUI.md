# OpenShot/OpenShot-ComfyUI

⭐ 18 · Python · GPL-3.0 · 推送 2026-04-16 · [GitHub](https://github.com/OpenShot/OpenShot-ComfyUI) · 组织维护

**面向 OpenShot 的 ComfyUI 节点集：分割/检测/音频增强**

由 OpenShot Studios 维护的 ComfyUI 自定义节点包，封装上游 AI 模型为 OpenShot 视频编辑工作流服务：SAM2 图像/视频分割（支持分块处理长视频）、GroundingDINO 文本提示目标检测、TransNetV2 场景边界检测、DeepFilterNet 音频降噪与 LavaSR 语音清晰度增强（输出 FLAC）。节点接受文件路径输入，首次使用时自动下载模型。要求 ComfyUI、PyTorch、ffmpeg、git，推荐 Python 3.10/3.11（Python 3.12 需先装 Rust）。GPLv3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SAM2 单图/视频分割，分块模式限制内存占用
- 文本提示目标检测输出 mask + JSON
- DeepFilterNet 降噪与 LavaSR 语音增强，按可调比例混合原始音频
- 首次使用自动从 Hugging Face 下载模型快照

## 适用场景

- 在视频编辑流程中对人物/物体做分割遮罩
- 长视频按场景边界切分（TransNetV2 输出 IN/OUT 区间）
- 低质量录音的对白降噪与清晰度增强

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L33: - `OpenShotDownloadAndLoadSAM2Model`
> L39: - `OpenShotDeepFilterNetDenoiseAudio` (file-path based audio denoise -> FLAC path)
> L40: - `OpenShotLavaSRSpeechClarity` (LavaSR speech runner -> FLAC path)

## 星数曲线

```mermaid
xychart-beta
    title "OpenShot/OpenShot-ComfyUI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 16 --> 19
    line [17, 18, 18]
```

2026-10-18 17 → 2026-10-31 18（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `bd6282d042ed` · [字段定义](../../DATASET.md)*
