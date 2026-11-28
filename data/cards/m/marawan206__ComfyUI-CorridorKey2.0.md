# marawan206/ComfyUI-CorridorKey2.0

⭐ 3 · Python · NOASSERTION · 推送 2026-11-02 · [GitHub](https://github.com/marawan206/ComfyUI-CorridorKey2.0) · 个人维护

**为 ComfyUI 提供绿幕抠像模型 CorridorKey 2.0 的非官方节点包**

将 Corridor Digital 的神经网络绿/蓝幕抠像模型 CorridorKey 2.0 接入 ComfyUI 的自定义节点集：支持整段视频时序一致抠像、任意帧 alpha 提示与双向传播、深度/法线/语义/运动特征查看、matte 清理与合成，并可在用户自己的镜头上 LoRA 微调。非官方集成，与 Corridor Digital 无隶属关系；提供 ComfyUI Manager、手动 git clone、Windows portable 三种安装途径；模型文件（约 5.1 GB）首次运行时自动下载。需 NVIDIA RTX 30 系以上 GPU（约 4 GB VRAM 至 1440p，微调 6-8 GB），Apple Silicon 为实验性支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Basic/Advanced 两种抠像节点，支持关键帧 alpha 提示与时间前后双向传播
- 附带 Depth & Normals、Semantic Identity、Motion Tracking 等特征节点
- Matte Refine、Despill、Composite（含 light wrap）后处理节点不触发模型重跑
- 可在自有镜头上微调 LoRA，含 alpha/边缘带/时间一致性等训练损失

## 适用场景

- 在 ComfyUI 中对整段绿幕/蓝幕素材做时序一致的抠像
- 用 alpha 提示修正复杂镜头（道具、多人、遮挡屏幕色）的抠像结果
- 为绿幕镜头生成深度、法线、语义与运动跟踪特征
- 用自己的素材微调专属 LoRA 以提升抠像质量

## 场景标签

`图像视频处理` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L3: ComfyUI nodes for **CorridorKey 2.0**, Corridor Digital's
> L26: |**Keying**|**CorridorKey 2.0 (Basic)** works out of the box: clip in, foreground, alpha and RGBA out. **CorridorKe
> L39: - An NVIDIA GPU, RTX 30-series or newer. CorridorKey 2.0 needs about 4 GB of VRAM for footage up to 1440p and

## 星数曲线

```mermaid
xychart-beta
    title "marawan206/ComfyUI-CorridorKey2.0 星数(近 2 点)"
    x-axis ["2026-10-29", "2026-11-28"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-10-29 3 → 2026-11-28 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `86e37ca59d32` · [字段定义](../../DATASET.md)*
