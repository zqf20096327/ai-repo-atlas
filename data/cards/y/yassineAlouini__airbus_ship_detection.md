# yassineAlouini/airbus_ship_detection

⭐ 15 · Python · 推送 2026-10-04 · [GitHub](https://github.com/yassineAlouini/airbus_ship_detection) · 个人维护

**Kaggle Airbus 船只检测竞赛的个人解决方案代码**

对 2018 年 Kaggle Airbus 船只检测竞赛的个人解题仓库：原始 2018 代码保留在 asd/ 目录，2026 年更新在 modern/ 目录下提供基于 PyTorch 的现代方案，分五个阶段：U-Net（EfficientNetV2-S 编码器）分割、DINOv2 ViT 有船/无船门控、按船只尺寸的误差分析、小船微调与伪标注。README 说明数据下载解压、提交方式，并记录了类别不平衡（空提交得 0.847 分）与测试集泄漏等竞赛事实。面向参与该竞赛或学习实例分割的科研/开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- modern/ 五阶段流程：U-Net 分割、ViT 门控、误差诊断、小船微调、伪标注
- 2018 原始代码 asd/ 保留不变供参考
- 提供数据下载、解压与 Kaggle 提交的命令说明

## 适用场景

- 复现或学习 Airbus 船只检测竞赛的解法
- 参考卫星图像实例分割与类别不平衡处理
- 了解竞赛中的数据泄漏与场景重叠分析做法

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L2: > submission, and documents a modern PyTorch solution in `modern/`. Its best late submission scores
> L7: > | `airbus_modern.py` | Stage 1: U-Net (EfficientNetV2-S) with a ship/no-ship head and a border channel, F2-tuned p

## 星数曲线

```mermaid
xychart-beta
    title "yassineAlouini/airbus_ship_detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `555cfeaf8827` · [字段定义](../../DATASET.md)*
