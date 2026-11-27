# ReSerendipity/SeedVR2-Turbo

⭐ 20 · Python · Apache-2.0 · 推送 2026-11-26 · [GitHub](https://github.com/ReSerendipity/SeedVR2-Turbo) · [官网](https://reserendipity.github.io/SeedVR2-Turbo/) · 个人维护 · 中文 README

**本地视频与图像超分 Web 应用，上传即修复、数据不出机**

把 SeedVR2 单步扩散修复模型包装为独立本地 Web 应用：上传图片或视频即可执行超分辨率与细节增强，数据全程留在本机，不依赖 ComfyUI 或外部推理服务。提供 3B/7B/7B-Sharp 三档模型与多种量化变体，通过 GPU Block Swap 降低显存占用（3B FP8 自 8 GB 起步），支持文件夹批量扫描与断点续跑。对外分发为 Tauri v2 Windows 单文件安装包，开发者可源码或 Docker 运行；附 Agent CLI 供脚本调用。需 NVIDIA CUDA GPU，不支持纯 CPU 推理；视频修复需自行安装 FFmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地推理的图片/视频超分辨率，数据不出本机
- 3B/7B/7B-Sharp 三档模型，FP8/FP16 及多种量化变体（不兼容 GGUF）
- GPU Block Swap 动态换入换出 Transformer 块，3B FP8 8 GB 显存起步
- Agent CLI 提供 JSON 输出与语义退出码，供脚本与 AI agent 调用

## 适用场景

- 本地修复老照片或低分辨率图片，不上传云端
- 对视频素材批量做超分辨率增强并断点续跑
- 在显存有限的 GPU 上通过 FP8 与 BlockSwap 运行大模型修复

## 场景标签

`图像视频处理` `模型量化` · 领域:感知与多模态

## 证据(README 行号)

> L23: SeedVR2-Lite 把字节跳动 Seed 团队与南洋理工大学 S-Lab 联合开源的 SeedVR2 单步扩散修复模型，包装成一个**独立运行的本地 Web 应用**：上传一张图片或一段视频，即可完成超分辨率与细节增强，数据
> L29: - **视频与图像修复**：基于单步扩散模型的超分辨率与细节增强，本地推理、数据不出机器。

## 星数曲线

```mermaid
xychart-beta
    title "ReSerendipity/SeedVR2-Turbo 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-11-26 20 → 2026-11-27 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `289cfe804b0e` · [字段定义](../../DATASET.md)*
