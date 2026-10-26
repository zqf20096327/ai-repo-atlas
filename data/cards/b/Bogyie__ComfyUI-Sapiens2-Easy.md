# Bogyie/ComfyUI-Sapiens2-Easy

⭐ 30 · Python · NOASSERTION · 推送 2026-05-04 · [GitHub](https://github.com/Bogyie/ComfyUI-Sapiens2-Easy) · 个人维护 · 中文 README

**在 ComfyUI 中运行 Meta Sapiens2 的人体分析节点包**

将 Meta Sapiens2 模型封装为 ComfyUI 原生节点的适配器：支持人体部位分割、表面法线图、3D pointmap（可导出 points/splats/textured mesh GLB）与姿态估计（BODY_25、DWPose、COCO_18、308 关键点、手部与面部）。所有任务共享同一模型加载流程，自动从 Hugging Face 下载官方权重到 ComfyUI/models/sapiens2/，支持 0.4b–5b 四档模型规模。仓库仅做适配，不训练、不修改、不再分发官方模型；模型权重受 Meta Sapiens2 许可约束。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分割/法线/pointmap/姿态共享统一模型加载器
- pointmap 可导出为 points、splats 或带纹理的 .glb
- 姿态输出覆盖 BODY_25/DWPose/COCO_18/308 关键点/手部/面部
- 自动下载 Hugging Face 官方权重并在本地复用

## 适用场景

- 在 ComfyUI 工作流中对单张人物图像做分割与法线估计
- 从单张图像导出 3D pointmap 或 GLB 网格
- 生成 OpenPose 风格姿态图像与 JSON 供下游工具使用

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L22: **ComfyUI-Sapiens2-Easy** turns Meta Sapiens2 into a small set of ComfyUI-native nodes. Pick a task, model size, an
> L77: This repository is a ComfyUI adapter around Meta Sapiens2. It does not train, modify, or redistribute the official 

## 星数曲线

```mermaid
xychart-beta
    title "Bogyie/ComfyUI-Sapiens2-Easy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 29 --> 31
    line [30, 30]
```

2026-10-18 30 → 2026-10-26 30（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `ccc00cbd5288` · [字段定义](../../DATASET.md)*
