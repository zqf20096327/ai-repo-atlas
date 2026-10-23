# Tencent-Hunyuan/Hunyuan3D-Part

⭐ 551 · Python · NOASSERTION · 推送 2025-12-05 · [GitHub](https://github.com/Tencent-Hunyuan/Hunyuan3D-Part) · 组织维护 · 中文 README

**3D 网格部件分割与生成的两段式流水线（P3-SAM + X-Part）**

腾讯混元开源的 3D 部件级处理流水线：整体网格先经 P3-SAM 完成 3D 部件分割，产出语义特征、部件分割与包围盒；再由 X-Part 生成完整部件，实现高保真、结构连贯的形状分解。两组件均有论文、代码、HuggingFace 权重与在线 Demo。当前发布的是 X-Part 的轻量版，完整版在 Hunyuan3D-Studio；X-Part 推荐输入为扫描网格或 AI 生成网格（如 Hunyuan3D V2.5/V3.0），P3-SAM 可处理任意输入网格。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- P3-SAM 输出语义特征、部件分割与部件包围盒
- X-Part 生成完整部件，做高保真形状分解
- 权重与 HuggingFace 在线 Demo 公开提供
- 当前发布为 X-Part 轻量版，完整版在 Hunyuan3D-Studio

## 适用场景

- 把整体 3D 网格拆分为可编辑的语义部件
- 为扫描或 AI 生成的网格做部件级分解
- 3D 内容创作流程中的部件化编辑与再生成

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L7: Our 3D part generation pipeline contains two key components, P3-SAM and X-Part. The holistic mesh is fed to part det
> L10: ### P3-SAM： Native 3D part Segmentation.
> L19: ### X-Part： high-fidelity and structure-coherent shape decomposition

## 星数曲线

```mermaid
xychart-beta
    title "Tencent-Hunyuan/Hunyuan3D-Part 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23"]
    y-axis "stars" 547 --> 552
    line [548, 549, 548, 551]
```

2026-10-18 548 → 2026-10-23 551（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `a10a06c0413e` · [字段定义](../../DATASET.md)*
