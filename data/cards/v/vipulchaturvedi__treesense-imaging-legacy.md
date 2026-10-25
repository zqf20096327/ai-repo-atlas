# vipulchaturvedi/treesense-imaging-legacy

⭐ 42 · Jupyter Notebook · AGPL-3.0 · 推送 2026-09-05 · [GitHub](https://github.com/vipulchaturvedi/treesense-imaging-legacy) · [官网](https://treesense-legacy.vipulchaturvedi.com/) · 个人维护

**卫星/航拍图像自动树木计数与绿地估算的 Web 应用（SIH 原型）**

Smart India Hackathon 2023 的大学原型项目，面向林业伐移地块评估：网站含落地页与仪表盘，提供树木计数、绿覆盖估算、树种识别、最优路径（Dijkstra）与历史数据工具。检测部分使用 YOLO 格式航拍树木数据集与 PyTorch 原型 notebook（阈值分割、训练、路径计算），前端用 React 构建，npm 工作流运行。README 顶部声明本仓库为历史归档版本，新版迁移至 treesense-imaging 仓库维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 基于卫星/航拍图像的树木计数与绿覆盖估算
- 树种识别与两点间最优路径计算（Dijkstra）
- YOLO 格式航拍树木检测数据集与训练 notebook
- 生成地图、报告与可视化数据

## 适用场景

- 开发项目涉及林地转用时的自动树木清点
- 估算指定林区绿覆盖比例并查看历史数据
- 规划林区两点间最优路径

## 场景标签

`目标检测` `图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L12: The project aims to address the challenge of accurately enumerating trees in forest areas earmarked for diversion d
> L17: - **Tree Count:** Allows accurate tree counting within designated forest areas.
> L33: ├── Dataset/             # YOLO format aerial tree detection dataset (train/val/test)

## 星数曲线

```mermaid
xychart-beta
    title "vipulchaturvedi/treesense-imaging-legacy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 41 --> 43
    line [42, 42]
```

2026-10-18 42 → 2026-10-25 42（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `ed31035dcfb5` · [字段定义](../../DATASET.md)*
