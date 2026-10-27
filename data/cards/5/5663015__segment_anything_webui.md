# 5663015/segment_anything_webui

⭐ 81 · Python · 推送 2026-08-02 · [GitHub](https://github.com/5663015/segment_anything_webui) · 个人维护

**基于 Gradio 的 Segment Anything 分割模型网页界面**

为 Meta 的 Segment Anything Model（SAM）提供 Gradio 网页界面，支持图像与视频分割，可通过点提示和文本提示生成分割掩码；文本提示路径结合 OWL-ViT 权重进行开放词汇检测后分割。用户 git clone 本仓库、安装 segment-anything、下载 SAM 与 OWL-ViT 权重放入 checkpoints 目录后运行 app.py 启动。默认模型为 vit_b，可在 CPU 上运行，默认设备为 cpu。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持点提示与文本提示的 SAM 图像分割
- 支持视频分割
- 文本提示路径结合 Google OWL-ViT 权重
- 默认 vit_b 模型可在 CPU 上运行

## 适用场景

- 在网页界面里用点或文本提示对图像做分割
- 对视频执行分割
- 本地无需 GPU 体验 SAM 分割效果

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L3: This project is based on **Segment Anything Model** by Meta. The UI is based on Gradio.
> L41: **Note：** Default model is `vit_b`，the demo can run on CPU. Default device is `cpu`。

## 星数曲线

```mermaid
xychart-beta
    title "5663015/segment_anything_webui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 80 --> 82
    line [81, 81]
```

2026-10-18 81 → 2026-10-27 81（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `87e6997f5de9` · [字段定义](../../DATASET.md)*
