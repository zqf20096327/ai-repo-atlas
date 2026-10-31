# jeankassio/ComfyUI-AceStep_SFT

⭐ 64 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/jeankassio/ComfyUI-AceStep_SFT) · [官网](https://somora.media) · 个人维护

**ComfyUI 节点套件：运行 AceStep 1.5 SFT 音乐生成模型**

为 ComfyUI 实现音乐生成模型 AceStep 1.5 SFT（监督微调版）的模块化节点套件，从官方 AceStep 工作流出发，扩展条件控制与质量选项：可选参考音频加载器、APG 引导模式（含 apg_denoised / 联合投影）、timbre_cls_token 修正、LM codes 强度、FP32 调度构建、guidance_rescale 与 RMS 上限等实验参数，并对齐官方 Gradio 管线的默认采样设置。附带 ScragVAE 可选解码器对比与两处 ComfyUI 核心修复（更新 ComfyUI 可能被覆盖）。供在 ComfyUI 中运行与调参该模型的用户使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实现 AceStep 1.5 SFT 全流程：生成、Cover/Remix、Repaint 任务节点
- APG 引导模式扩展（apg_denoised、联合通道投影、RMS 上限）与 timbre 修正 token
- 默认采样对齐官方 Gradio 管线（jkass_quality 采样器、ace_step 调度、FP32）
- 可选参考音频加载与 ScragVAE 解码器对比流程

## 适用场景

- 在 ComfyUI 中用 AceStep 1.5 SFT 生成或翻唱/重混音乐
- 固定种子逐参数对比音质实验（引导模式、LM codes 强度、VAE）
- 用参考音频控制音色进行音乐生成

## 场景标签

 · 领域:生成式音频/音乐生成

## 证据(README 行号)

> L6: A modular node suite for ComfyUI that implements **AceStep 1.5 SFT** (Supervised Fine-Tuning), a state-of-the-art mu
> L63: Reference: ACE-Step 1.5 at ca1e85f, checked against both Gradio controls and SFT `generate_audio`.

## 星数曲线

```mermaid
xychart-beta
    title "jeankassio/ComfyUI-AceStep_SFT 星数(近 5 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25", "2026-10-26", "2026-10-31"]
    y-axis "stars" 60 --> 65
    line [61, 62, 63, 64, 64]
```

2026-10-18 61 → 2026-10-31 64（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `447cb440518d` · [字段定义](../../DATASET.md)*
