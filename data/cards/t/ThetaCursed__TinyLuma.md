# ThetaCursed/TinyLuma

⭐ 48 · Rust · AGPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/ThetaCursed/TinyLuma) · 个人维护

**面向 AI 生成图像的原生轻量后期处理与批量编辑器**

纯 Rust + egui 构建的独立桌面图像后期处理工具，专为润饰 Stable Diffusion、Midjourney、Flux、ComfyUI 生成的图像设计：提供 Oklab 感知色彩分级（16 项非破坏性控制）、.cube 3D LUT 库（子文件夹分类、搜索、收藏、强度混合）、针对 AI '塑料皮肤'纹理调校的 Detail Engine、批量处理与 Preset to All、裁剪/污点修复/白平衡工具。可选择性保留或清除 PNG 中的工作流元数据（tEXt/zTXt/iTXt/eXIf），导出 PNG/JPEG/WebP。单文件原生可执行程序约 8MB，Windows x64 提供预编译 zip（含 9 个 LUT），也可用 cargo 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Oklab 感知色彩分级与 Bradford 色适应，16 项非破坏性控制
- .cube 3D LUT 库：分类、搜索、收藏、0-100% 强度混合
- ComfyUI/A1111 元数据可选保留（工作流完整回传）或完全清除
- 针对 AI 纹理调校的 Clarity/Texture/Sharpen 算法与批量工作流

## 适用场景

- 对 Midjourney/Flux/ComfyUI 生图批量调色并套用统一 LUT 预设
- 编辑后仍想保留工作流元数据以便回 ComfyUI/A1111 复现
- 导出前去净 prompt、模型、LoRA 等生成信息保护隐私

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: **Lightweight, native post-processor and batch editor for AI-generated images.**
> L18: **TinyLuma** is a fast, standalone desktop photo editor designed specifically for finishing AI-generated artwork an

## 星数曲线

```mermaid
xychart-beta
    title "ThetaCursed/TinyLuma 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-31"]
    y-axis "stars" 46 --> 49
    line [47, 48, 48]
```

2026-10-18 47 → 2026-10-31 48（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `727320b12f41` · [字段定义](../../DATASET.md)*
