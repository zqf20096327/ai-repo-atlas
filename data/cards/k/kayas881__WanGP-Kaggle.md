# kayas881/WanGP-Kaggle

⭐ 19 · Jupyter Notebook · 推送 2025-12-30 · [GitHub](https://github.com/kayas881/WanGP-Kaggle) · 个人维护

**在 Kaggle 免费 T4 上运行 WanGP 视频生成模型的笔记本**

面向无本地 GPU 用户的 Kaggle notebook：在 Kaggle 免费 Tesla T4（15GB VRAM）上安装并运行 WanGP，通过 Gradio 网页界面使用 Wan 2.2/2.1、Hunyuan Video、LTX Video、Flux、CogVideoX 等多种视频生成模型，支持 Text2Video、Image2Video 等任务。包含 SageAttention、mmgp 显存管理、4 步 Lightning LoRA、ckpts 符号链接到 /tmp（约 73GB 临时存储）等优化。限制：Kaggle 会话最长 9 小时，Gradio 链接约 1 周过期，T4 上单个视频约需 9-15 分钟。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 Kaggle 免费 T4 GPU（15GB VRAM）上运行 WanGP
- 支持 Wan 2.2/2.1、Hunyuan Video、LTX Video、CogVideoX 等多种模型
- mmgp 显存管理与 SageAttention 优化，4 步 Lightning LoRA 预配置
- 自动符号链接 /tmp 提供约 73GB 模型存储

## 适用场景

- 没有本地 GPU 时用 Kaggle 免费算力生成视频
- 通过 Gradio 网页界面切换多种视频模型做文生视频/图生视频
- 低显存环境下借助 offloading 运行大型视频模型

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L3: Run powerful video generation models on Kaggle's free Tesla T4 GPU (15GB VRAM) using WanGP's optimized interface!
> L184: **Note**: This notebook uses the WanGP project by DeepBeepMeep, which provides an optimized interface for running 
> L80: - ✅ Full WanGP installation with all dependencies

## 星数曲线

```mermaid
xychart-beta
    title "kayas881/WanGP-Kaggle 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6fe50dd60bde` · [字段定义](../../DATASET.md)*
