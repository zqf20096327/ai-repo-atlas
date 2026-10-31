# lucataco/open-source-higgsfield

⭐ 20 · Python · Apache-2.0 · 推送 2026-10-30 · [GitHub](https://github.com/lucataco/open-source-higgsfield) · 个人维护

**本地 ComfyUI 视频角色替换工具：保持运镜与画面换演员**

在本地 stock ComfyUI 上用开放权重模型（SAM 3.1、FLUX 3 Image Klein、SCAIL-2）将视频中表演者替换为新角色，保留原运镜、场景、音频与分辨率。流程为 ffmpeg 抽帧、SAM 3.1 跟踪与重识别、FLUX 3 生成首帧锚定身份、按 81 帧分段做 WanSCAILToVideo 替换并做 QC，最后合成回原画面。模型需约 50 GB 显存，FLUX 3 为门控仓库且限非商用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SAM 3.1 跟踪+重识别的 follow-cam 虚拟摄像机策略，仅重绘表演者区域
- FLUX 3 Image Klein 首帧锚定角色身份（四选项）
- 81 帧分段生成、接缝 QC 与断点续跑
- 仅用 ComfyUI 核心节点，无自定义节点包或封闭 API

## 适用场景

- 影视/VFX 场景中把已拍镜头里的表演者换成新角色
- 在本地用开放权重复现商业换角工具的效果
- 长镜头（约 30 秒）的 AI 换角后期制作

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L8: Body Double recasts the performer in a video as a new character. Their motion, the camera move, the rest of the shot
> L9: and the original audio stay. It runs locally on stock ComfyUI with open-weights models (SAM 3.1, FLUX 3 Image Klein
> L10: and SCAIL-2), and it's an open alternative to Higgsfield Genjutsu.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e9e8e8ef517f` · [字段定义](../../DATASET.md)*
