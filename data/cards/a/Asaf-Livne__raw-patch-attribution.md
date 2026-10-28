# Asaf-Livne/raw-patch-attribution

⭐ 36 · Python · MIT · 推送 2026-09-22 · [GitHub](https://github.com/Asaf-Livne/raw-patch-attribution) · [官网](https://asaf-livne.github.io/RPA/) · 组织维护

**黑盒图像溯源 CNN：仅凭像素判定生成图像的来源模型**

特拉维夫大学团队发布的 Raw-Patch Attribution（RPA）研究代码：用约 600 万参数的轻量 CNN，把图像切成 64×64 重叠 patch 逐块打分，再经 overlap 校正的加权平均聚合为图像级标签，在 25/27 个生成器的 DRAGON 与 OpenFake 基准上做闭集归因。仅依赖图像本身，不需要生成器权重、VAE 或提示词，支持 64²到 4096² 分辨率不重训。同一骨干还支持开集拒识、无监督模型谱系聚类与少样本线性头适配。提供 pip 安装、预训练 checkpoint（各约 25MB）、训练/评测/适配脚本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 约 6M 参数 CNN 做黑盒模型归因，仅需图像无需生成器权重
- 64²到 4096² 分辨率不变，推理成本与候选模型数无关
- 开集拒识、无监督模型谱系聚类、少样本线性头适配共用同一骨干
- 发布 DRAGON(25类)/OpenFake(27类) 预训练 checkpoint

## 适用场景

- 判定一张 AI 生成图像出自哪个文生图模型
- 拒识训练中未见过的生成器（开集归因）
- 通过少量标注样本把新生成器纳入已有归因模型
- 无监督聚类分析生成模型之间的谱系关系

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L12: *Attribute an image to the model that generated it — from raw pixels, with a ~6M-parameter CNN.*
> L26: The rapid proliferation of generative models raises the **model attribution**
> L27: problem: given only an image, can we determine which model produced it?

## 星数曲线

```mermaid
xychart-beta
    title "Asaf-Livne/raw-patch-attribution 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `b40423c1ad60` · [字段定义](../../DATASET.md)*
