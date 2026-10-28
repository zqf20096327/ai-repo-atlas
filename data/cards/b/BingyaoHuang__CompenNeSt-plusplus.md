# BingyaoHuang/CompenNeSt-plusplus

⭐ 25 · Python · NOASSERTION · 推送 2025-12-15 · [GitHub](https://github.com/BingyaoHuang/CompenNeSt-plusplus) · 个人维护

**投影仪补偿研究代码：端到端学习几何+光度校正**

TPAMI 2022 论文 CompenNeSt++ 的 PyTorch 实现，面向计算摄影与投影-相机（procam）研究者。系统将投影光传输分解为 WarpingNet（几何校正）与 CompenNeSt（光度补偿）两个网络端到端训练，无需结构光额外步骤与补偿图真值；提供预训练版本（仅 8 张图、约 3 分钟训练）。需 PyTorch 兼容 GPU、Python 3.7、PyTorch 1.2.0，配套基准数据集约 11GB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- WarpingNet + CompenNeSt 端到端联合训练几何与光度补偿
- 预训练版本仅需 8 张图像与约 3 分钟训练
- 提供全补偿与光度补偿基准数据集（20/24 setups）
- 训练过程经 visdom 在浏览器可视化

## 适用场景

- 复现 TPAMI 投影补偿实验与消融研究
- 在自己的投影表面上应用 CompenNeSt++ 生成补偿图像
- 作为投影补偿研究的基准对比方法

## 场景标签

`图像视频处理` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L6: PyTorch implementation of [CompenNeSt++ (TPAMI)][1], a journal extension of [CompenNet (CVPR'19)][5] and [CompenNet+
> L20: ## Learning-based formulation
> L33: * PyTorch compatible GPU

## 星数曲线

```mermaid
xychart-beta
    title "BingyaoHuang/CompenNeSt-plusplus 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `57f1ce882880` · [字段定义](../../DATASET.md)*
