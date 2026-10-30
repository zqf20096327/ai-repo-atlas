# dreamrec/ComfyUI-Pixal3D

⭐ 28 · Python · NOASSERTION · 推送 2026-05-14 · [GitHub](https://github.com/dreamrec/ComfyUI-Pixal3D) · 个人维护 · 中文 README

**Pixal3D 的 ComfyUI 自定义节点：Windows 上单图生成 PBR 3D 网格**

将腾讯 Pixal3D（SIGGRAPH 2026 单图到 PBR 纹理 3D 管线）封装为 ComfyUI 自定义节点，面向 Windows 10/11 + NVIDIA RTX 30/40/50 用户，在 ComfyUI 主 Python 环境内独立运行，无需额外 worker 环境；也可复用 ComfyUI-TRELLIS2 的 pixi 环境。install.py 自动克隆上游代码、安装依赖并打 Windows 补丁；首次排队时从 HuggingFace 下载约 26 GB 模型权重。限制：上游许可为学术/非商业且禁止在欧盟使用，AMD/Intel GPU 不支持，需 16 GB 以上显存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单图生成带 PBR 纹理的 GLB 网格（RTX 5090 约 3-5 分钟）
- 在 ComfyUI 主 .venv 内独立运行，install.py 自动处理依赖与 Windows 补丁
- 内置 4 档显存/质量配置，10-32 GB 显存峰值可调
- 可选输出 OBJ + MTL，支持外部抠图（RMBG-2.0/SAM）替代内置 BiRefNet

## 适用场景

- 在 ComfyUI 工作流中把单张图片转成带 PBR 纹理的 3D 模型
- 生成可直接导入 Blender / Three.js 的 GLB 资产
- 在 16 GB 显存显卡上用低显存模式跑 1024 分辨率管线

## 场景标签

 · 领域:3D 生成/AI 内容工具链

## 证据(README 行号)

> L14: ComfyUI custom node for **Pixal3D** — Tencent's SIGGRAPH 2026 single-image to PBR-textured-3D pipeline — on **Windo
> L83: The only one you need is **`Pixal3D: Image to Mesh`**. Drop in an image, queue, get a GLB.

## 星数曲线

```mermaid
xychart-beta
    title "dreamrec/ComfyUI-Pixal3D 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-30 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `fff0b6e43c74` · [字段定义](../../DATASET.md)*
