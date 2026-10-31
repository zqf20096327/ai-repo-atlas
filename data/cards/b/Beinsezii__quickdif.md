# Beinsezii/quickdif

⭐ 15 · Python · GPL-3.0 · 推送 2026-10-12 · [GitHub](https://github.com/Beinsezii/quickdif) · 个人维护

**面向多种 Diffusers 模型的命令行图像生成工具**

基于 Diffusers 的 Python CLI 推理脚本，支持 AuraFlow、FLUX、Stable Diffusion 系列、SDXL 等多种模型格式，提供文本生成图像与图像转换、多 LoRA 融合、1-8 位量化、PAG 引导、参数网格迭代等生成参数。安装仅支持 Python 3.11+ 的 pip 方式，可选 venv 或以 Python 模块形式使用。明确不含 ControlNet、Inpaint、服务端 API 与一键安装器，MacOS/MPS 与 Intel OneAPI 可能无法正常工作。面向偏好命令行的本地图像生成用户。

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

- 验证支持 AuraFlow/FLUX/SD 系列/SDXL 等多种 Diffusers 模型
- 基于 peft 的多 LoRA 融合与 1-8 位量化
- 模块化采样器/调度器与参数网格迭代生成
- 可从 JSON/TOML/PNG 加载生成设置

## 适用场景

- 在命令行本地运行多种 Diffusers 模型生成图像
- 用多 LoRA 融合与量化控制生成过程
- 批量迭代参数生成对比网格图

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L2: Quick and easy CLI inference that just works™ for a variety of Diffusers models
> L22:  * Features all of the most common generation parameters

## 星数曲线

```mermaid
xychart-beta
    title "Beinsezii/quickdif 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `8cf83a675435` · [字段定义](../../DATASET.md)*
