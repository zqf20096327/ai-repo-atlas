# kuhung/minimax-h3-colab-workflow

⭐ 3 · Jupyter Notebook · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/kuhung/minimax-h3-colab-workflow) · [官网](https://kuhung.me) · 个人维护 · 中文 README

**在 Colab 单卡本地运行 MiniMax H3 视频/图像生成的 notebook 工作流**

提供一组 Google Colab Jupyter notebook，用开放权重在单张 L4 24GB GPU 上本地运行 MiniMax H3 视频生成（含 32kHz 立体声）与 MiniMax-H3-Image 文生图/指令编辑，不调用商业 API。含六个工作流（文生视频、图生视频、首尾帧、多模态参考、图像生成编辑、三镜头故事板），通过单通道 CFG=1.0 采样、按 CUDA 版本自动量化选择、T4 GPU 预检与 CLI 批量脚本降低成本与排错。附 L4 实测基准与计费估算。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六个视频/图像生成工作流以 Colab notebook 形式提供，零商业 API 调用
- 单通道 CFG=1.0 采样使 544p 渲染从 315.8s 降至 165.4s
- 按 CUDA 版本自动选择 int8_convrot 或 fp8_scaled 量化
- check_gpu.py 预检阻断不支持的 T4，CLI 支持无头多镜头批量渲染

## 适用场景

- 在 Colab 上低成本生成带立体声音的视频片段
- 从首帧锁定产品/主体外观做图生视频
- 2048×2048 文生图与指令编辑
- 多镜头故事板的批量自动化渲染并缓存到 Google Drive

## 场景标签

`图像生成` `视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: **Run MiniMax H3 (Video + 32kHz Stereo Audio) & MiniMax-H3-Image locally on a single Google Colab L4 24GB GPU — usin
> L37: |**H3-Image Gen & Edit (`v4.0`)**|2048×2048 text-to-image and instruction editing via `sd-cli`|Open in Colab|Pre-ru


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `7fda32a659aa` · [字段定义](../../DATASET.md)*
