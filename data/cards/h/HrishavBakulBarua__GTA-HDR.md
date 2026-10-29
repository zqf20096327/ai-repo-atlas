# HrishavBakulBarua/GTA-HDR

⭐ 37 · NOASSERTION · 推送 2026-05-03 · [GitHub](https://github.com/HrishavBakulBarua/GTA-HDR) · [官网](https://arxiv.org/abs/2403.17837) · 组织维护

**给 HDR 重建研究者的 LDR→HDR 深度学习数据集（WACV 2025）**

Monash 大学团队发表于 WACV 2025 的论文官方仓库，提出 GTA-HDR 大规模合成数据集：从支持 HDR-10 的游戏 GTA-V 中采样 4 万张真值 HDR 图像（512×512 与 1024×1024），场景覆盖室内/城市/野外、不同时段光照与天气季节；并经变换生成 100 万张多曝光 LDR 图与 4 万张失真 HDR 图。仓库汇总 HDR 重建模型、相关数据集对比表与实验结果。数据集需填写协议表邮件申请获取，正式版尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 40K 真值 HDR + 1M LDR + 40K 失真 HDR 图像
- 源自 GTA-V 光线追踪数据的合成采集管线（Script Hook V 采集、Chamfer 相似度去重）
- 覆盖多地点、多光照、多天气季节的场景与图像多样性
- 汇总 8+ 种 HDR 重建模型与 10+ 个 LDR-HDR 数据集的对比表格

## 适用场景

- 训练与评测单张/多曝光 LDR 到 HDR 的重建模型
- 开展无参考 HDR 图像质量评估研究（真值与失真 HDR 配对）
- 对比现有 LDR-HDR 数据集的规模与多样性

## 场景标签

 · 领域:计算摄影/计算机视觉

## 证据(README 行号)

> L11: This page contains all the Datasets and Code bases (experiments and evaluations) involved in experimenting and esta
> L59: a) GTA-HDR is a large-scale (i.e., 40K ground truth HDR images) synthetic dataset sampled from the GTA-V video game
> L104: dataset amounts to a total of 40K × 25 = 1M LDR, 40K HDR, and 40K distorted HDR images.

## 星数曲线

```mermaid
xychart-beta
    title "HrishavBakulBarua/GTA-HDR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-29 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `84566d4ff012` · [字段定义](../../DATASET.md)*
