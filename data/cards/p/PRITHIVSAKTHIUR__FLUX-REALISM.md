# PRITHIVSAKTHIUR/FLUX-REALISM

⭐ 21 · Python · Apache-2.0 · 推送 2026-05-22 · [GitHub](https://github.com/PRITHIVSAKTHIUR/FLUX-REALISM) · [官网](https://huggingface.co/spaces/prithivMLmods/FLUX-REALISM) · 个人维护

**双 FLUX 模型写实现实风格图像生成应用（Gradio 网页）**

基于 FLUX.1-Krea-dev 与 FLUX.1-dev + 写实现风格 LoRA（Flux-Super-Realism-LoRA）的双管线文生图应用，提供 Gradio 网页界面。内置画质预设（4K/8K）自动改写提示词、负向提示词扩展、预览用 taef1 VAE 与成品用 Krea VAE 切换、去噪循环中的迭代图像流式输出，支持最高 2048x2048 分辨率与 ZIP 批量导出。需 CUDA GPU，通过 pip 或 uv 本地运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 双模型工作区：Krea-dev 快速迭代与 dev+写实 LoRA 精修管线
- 内置画质预设自动改写提示词（Ultra HD 4K、8K Cinematic）
- 去噪循环钩子实现的迭代图像流式反馈与双 VAE 切换
- 最高 2048px 尺寸控制、种子随机化与 ZIP 批量导出

## 适用场景

- 本地生成写实风格文生图作品
- 对比快速迭代与高细节两条管线的出图效果
- 研究写实 LoRA 与 VAE 切换对出图质量的影响

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: FLUX-REALISM is an experimental, advanced image generation application designed to provide highly realistic image sy
> L9: * **Dual-Model Inference:** Seamlessly alternate between the fast, iteration-friendly flux.1-krea-dev pipeline and t

## 星数曲线

```mermaid
xychart-beta
    title "PRITHIVSAKTHIUR/FLUX-REALISM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `5b2b8a9166bc` · [字段定义](../../DATASET.md)*
