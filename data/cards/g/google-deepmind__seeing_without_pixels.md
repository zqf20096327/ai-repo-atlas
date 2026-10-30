# google-deepmind/seeing_without_pixels

⭐ 16 · Python · Apache-2.0 · 推送 2026-07-17 · [GitHub](https://github.com/google-deepmind/seeing_without_pixels) · 组织维护

**仅凭相机轨迹（无像素）做视频文本检索的模型代码**

CVPR 2026 论文 Seeing without Pixels 的官方代码：CamFormer 是作用于相机位姿序列的四层 Transformer，将位姿序列映射为运动嵌入，与冻结的 CLIP 文本编码器做对比学习训练；推理与评测仅使用相机位姿轨迹，不使用视频帧。仓库提供预训练代码与五选一检索评测，覆盖 Ego-Exo4D（Aria 眼动轨迹）、DynPose-100K（外参轨迹）与 Nymeria 零样本迁移。提供预计算特征与 checkpoint 下载，可无 GPU 复现检索指标。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 仅以相机 3D 轨迹为输入，不使用视频帧
- 四层 Transformer + 冻结 CLIP 文本编码器的对比轨迹-文本训练
- 提供预计算检索特征，可无 GPU 复现结果
- 支持 Ego-Exo4D / DynPose-100K 训练评测与 Nymeria 零样本迁移

## 适用场景

- 复现论文中基于相机轨迹的视频文本检索结果
- 使用 checkpoint 对相机轨迹数据做零样本检索评测
- 在自有序列数据上预训练/微调 CamFormer

## 场景标签

`模型训练` `微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L13: Our paper shows that camera trajectories carry surprisingly rich semantic information. CamFormer takes only the cam
> L21: The code operates on camera-pose trajectories only; no video frames are used.

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/seeing_without_pixels 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `79646c2f932a` · [字段定义](../../DATASET.md)*
