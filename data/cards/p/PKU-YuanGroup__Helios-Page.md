# PKU-YuanGroup/Helios-Page

⭐ 25 · HTML · 推送 2026-07-27 · [GitHub](https://github.com/PKU-YuanGroup/Helios-Page) · [官网](https://pku-yuangroup.github.io/Helios-Page) · 组织维护 · 中文 README

**14B 实时长视频生成模型：单 H100 上 19.5 FPS 合成分钟级视频**

北京大学团队的视频生成模型官方实现，提供 Helios-Base/Mid/Distilled 三个 14B 权重（架构相同，采样策略与蒸馏程度不同），支持文生视频、图生视频、视频转视频与交互式生成。采用自回归按块（每块 33 帧）生成，官方报告在不使用常见防漂移策略与标准加速技术的情况下，单张 H100 达 19.5 FPS、单张昇腾 NPU 约 10 FPS。支持 Group Offloading（约 6GB 显存）与多卡上下文并行（Ulysses/Ring/Unified Attention），并有 Diffusers、vLLM-Omni、SGLang-Diffusion 的 Day-0 接入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单张 H100 达 19.5 FPS 的分钟级视频生成（NPU 约 10 FPS）
- Helios-Base/Mid/Distilled 三个 14B 模型权重开放下载（HuggingFace/ModelScope）
- Group Offloading 将显存占用降至约 6GB，并支持多卡上下文并行
- Day-0 支持 Diffusers / vLLM-Omni / SGLang-Diffusion / 昇腾 NPU

## 适用场景

- 从文本或图像生成长达分钟级的视频内容
- 在消费级显存上运行 14B 视频生成模型
- 交互式实时视频生成应用

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L19: This repository is the official implementation of Helios, which is a breakthrough video generation model that achie
> L50: * `[2026.03.04]` 🔥 We've released the training/inference code and weights of **Helios-Base**, **Helios-Mid** and **

## 星数曲线

```mermaid
xychart-beta
    title "PKU-YuanGroup/Helios-Page 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-30 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `91f6c56c27b2` · [字段定义](../../DATASET.md)*
