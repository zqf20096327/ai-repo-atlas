# omeregev/click2mask

⭐ 21 · Python · NOASSERTION · 推送 2026-01-22 · [GitHub](https://github.com/omeregev/click2mask) · [官网](https://omeregev.github.io/click2mask/) · 个人维护

**点击定位的图像局部编辑方法：点击处动态生成掩码加对象**

AAAI 2025 论文 Click2Mask 的官方 PyTorch 实现：给定输入图像、一次鼠标点击和文本提示，在扩散过程中动态生成掩码并同时生成要添加的对象，实现自由形式的局部编辑，无需预先分割或手绘掩码。另提出 Edited Alpha-CLIP 评估指标，对无掩码编辑方法提取编辑区域掩码并评估其与提示的对齐度。提供 Hugging Face 在线 Demo、Colab、Gradio 界面与命令行脚本，需下载 1.2GB Alpha-CLIP 检查点。代码基于 Blended Latent Diffusion 与 Stable Diffusion。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 点击+提示即可在扩散过程中动态生成掩码并添加对象
- Edited Alpha-CLIP：提取编辑区域掩码并评估与提示的对齐度
- 提供 Gradio 界面与命令行两种本地运行方式
- Hugging Face 在线 Demo 与 Colab 免安装体验

## 适用场景

- 对图像指定位置添加对象进行局部编辑
- 在浏览器中快速试用点击式图像编辑
- 对无掩码编辑方法做量化评估对比

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: Official PyTorch Implementation for
> L21:  , and a prompt for an added object, a **Mask** is generated dynamically,
> L152: Blended Latent Diffusion and Stable Diffusion, and utilizes AlphaCLIP.

## 星数曲线

```mermaid
xychart-beta
    title "omeregev/click2mask 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a5615c2fe9b7` · [字段定义](../../DATASET.md)*
