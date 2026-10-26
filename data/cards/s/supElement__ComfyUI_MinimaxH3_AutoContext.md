# supElement/ComfyUI_MinimaxH3_AutoContext

⭐ 36 · Python · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/supElement/ComfyUI_MinimaxH3_AutoContext) · 个人维护 · 中文 README

**ComfyUI 长视频生成节点：MiniMax H3 分段推理突破显存限制**

面向 ComfyUI 用户的 MiniMax H3 视频生成自定义节点集。将长视频按帧拆分为多段独立推理，通过段间 Latent 锚定（续接帧）实现衔接，使峰值显存只取决于单段长度；配套提示词时间轴切片（Clip_Tag/timeline/sequential/global 四种模式）、参考素材智能过滤、二次采样、接缝修正与三段式面部修复等节点。支持 latent 分段缓存与断点续推（目录级上限默认 32GB 自动清理）。提供 git clone 手动安装与 ComfyUI Manager 两种安装方式，另有 classic 旧版分支。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分段推理 + 段间续接锚定，峰值显存只取决于单段长度
- 提示词时间轴四种模式（Clip_Tag/timeline/sequential/global）自动切分对齐
- latent 分段缓存支持推理中断后跳过已推理分段
- 接缝修正（色彩/运动/闪帧）与 YOLO 检测驱动的面部修复节点链

## 适用场景

- 显存有限时生成超长时长的 MiniMax H3 视频
- 按时间轴或标签让提示词分段对应视频内容节奏
- 低清一采后接高清二采并修复段间接缝
- 对长视频中的人脸做检测、精修与贴回

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L6: 一键式 MiniMax H3 长视频自动化生成节点：**分段推理 + 段间续接锚定 + 提示词时间轴切片 + 二次采样（二采）+ 接缝修正 + 面部修复**。
> L61: |**Minimax_H3_AutoContext_Sampler**|主节点：分段推理 + 续接锚定 + 采样（一采/二采共用）|

## 星数曲线

```mermaid
xychart-beta
    title "supElement/ComfyUI_MinimaxH3_AutoContext 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-26 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `f7b8e1486423` · [字段定义](../../DATASET.md)*
