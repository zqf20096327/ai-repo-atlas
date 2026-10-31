# malthee/evolutionary-diffusion

⭐ 16 · Jupyter Notebook · MIT · 推送 2026-10-24 · [GitHub](https://github.com/malthee/evolutionary-diffusion) · 个人维护

**用进化算法优化扩散模型嵌入的图像/音频生成研究库**

将遗传算法、岛屿GA、NSGA、Sep-CMA 等进化计算方法应用于扩散模型的提示嵌入空间，通过优化嵌入向量来最大化美学评分（LAION Aesthetics Predictor V2/V2.5）、CLIP-Score/CLIP-IQA 指标、规避 AI 图像检测器（SDXL detector/SSP/DIRE）以及优化 Audiobox 音频美学。图像生成支持 SDXL 与 SD 嵌入，音频支持 AudioLDM 的 CLAP 嵌入空间。提供 Colab notebook、本地 pip 安装、Azure 云端 campaign 工作流与 uv 锁定环境。面向使用 Python 与 Jupyter 的研究者，模型自动下载带哈希校验，依赖验证于 Python 3.12/3.13，支持 CUDA 与 MPS。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在提示嵌入空间运行 GA/岛屿GA/NSGA/Sep-CMA 等进化算法
- 内置 LAION 美学、CLIP-Score/CLIP-IQA、AI 检测规避（SSP/DIRE）等多种评估器
- 音频路径支持 AudioLDM 的 CLAP 嵌入与 Audiobox Aesthetics 优化
- 模型自动下载带哈希校验与 TLS 验证，支持 CUDA 和 MPS

## 适用场景

- 优化提示嵌入以生成高美学评分的图像
- 研究生成图像对 AI 检测器的规避能力
- 用进化算法探索嵌入空间与艺术家风格混合

## 场景标签

`图像生成` `科研工具` · 领域:内容生成

## 证据(README 行号)

> L5: * 🎨 Aesthetics Maximization/Minimization using LAION Aesthetics Predictor V2
> L6: * 📊 Multi-Objective Optimization with CLIP-IQA metrics
> L115: Current supported creators working in the prompt embedding space:

## 星数曲线

```mermaid
xychart-beta
    title "malthee/evolutionary-diffusion 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `afc72de9e305` · [字段定义](../../DATASET.md)*
