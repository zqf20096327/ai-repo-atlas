# janelia-cellmap/cellmap-segmentation-challenge

⭐ 43 · Python · BSD-3-Clause · 推送 2026-07-10 · [GitHub](https://github.com/janelia-cellmap/cellmap-segmentation-challenge) · [官网](https://janelia-cellmap.github.io/cellmap-segmentation-challenge/) · 组织维护

**面向 CellMap 分割挑战的工具箱：数据下载、训练、预测、后处理与打包提交**

Python 包，为参加 CellMap（Janelia）电镜图像分割挑战提供全流程脚本与 CLI：csc fetch-data 下载 Zarr 格式的标注与 EM 数据（默认约 36.7GB 存储，可选全分辨率约 1.18TB），基于 cellmap-data 包构建；提供 2D/3D 模型训练示例脚本与 csc train/predict/process 命令，支持在 out-of-memory 数组上做预测与后处理（阈值、连通域、watershed 等），可经 neuroglancer 可视化，最后用 csc pack-results 打包并通过在线门户用 GitHub 账号提交。面向参赛的生物图像分割研究者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- csc CLI 覆盖 fetch-data/train/predict/process/visualize/pack-results 全流程
- 基于 cellmap-data 包交互 CellMap 数据格式（OME-NGFF/Zarr）
- 支持 2D/3D 模型训练与 TensorBoard 日志监控
- 预测输出 raw logits/affinities，需 process 脚本转 label volumes 后提交

## 适用场景

- 参加 CellMap 分割挑战，下载训练数据并提交预测结果
- 训练 2D/3D 分割模型并在测试 crop 上预测
- 用 neuroglancer 对比查看 groundtruth 与预测结果

## 场景标签

`目标检测` `模型训练` · 领域:感知与多模态

## 证据(README 行号)

> L88: Example scripts for training 2D and 3D models are provided in the `examples` directory. The scripts are named `trai
> L122: csc predict train_3D.py

## 星数曲线

```mermaid
xychart-beta
    title "janelia-cellmap/cellmap-segmentation-challenge 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 42 --> 44
    line [43, 43]
```

2026-10-18 43 → 2026-10-29 43（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `311ca6feec3a` · [字段定义](../../DATASET.md)*
