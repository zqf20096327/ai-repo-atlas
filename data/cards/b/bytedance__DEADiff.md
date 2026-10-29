# bytedance/DEADiff

⭐ 278 · Python · Apache-2.0 · 推送 2026-09-16 · [GitHub](https://github.com/bytedance/DEADiff) · 组织维护 · 中文 README

**风格化文生图扩散模型：按参考图风格生成新图像**

CVPR 2024 论文 DEADiff 的官方实现，由中科大与字节跳动人员完成。提供推理代码与预训练模型：给定参考图像与文本提示，生成体现参考风格的新图像；支持结合 ControlNet（Canny/深度引导）的风格迁移，控制生成图像的空间布局。通过 conda 环境 + pip 安装，运行 Gradio 应用推理；模型权重从 Hugging Face 下载。仅限个人/研究/非商业用途，训练数据尚未发布。

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

- 参考图风格 + 文本提示的文生图生成（512x512）
- 结合 ControlNet 的 Canny/深度引导风格迁移
- 提供 Gradio 推理应用与预训练模型权重

## 适用场景

- 用参考图风格生成符合文本描述的新图像
- 在边缘或深度结构约束下做风格迁移
- 复现 CVPR 2024 论文的推理结果

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: # DEADiff: An Efficient Stylization Diffusion Model with Disentangled Representations (CVPR 2024 Highlight)
> L15: **TL;DR:** We propose DEADiff, a generic method facilitating the synthesis of novel images that embody the style of

## 星数曲线

```mermaid
xychart-beta
    title "bytedance/DEADiff 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 277 --> 279
    line [278, 278]
```

2026-10-18 278 → 2026-10-29 278（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `07d40e481766` · [字段定义](../../DATASET.md)*
