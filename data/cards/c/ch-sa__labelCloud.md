# ch-sa/labelCloud

⭐ 809 · Python · GPL-3.0 · 推送 2026-05-02 · [GitHub](https://github.com/ch-sa/labelCloud) · [官网](https://ch-sa.github.io/labelCloud/) · 个人维护

**点云 3D 边界框标注工具：为 3D 目标检测制作标签**

基于 Python 的轻量级点云标注桌面工具，提供 picking 与 spanning 两种边界框标注方式及键盘快捷键修正，支持 9 自由度旋转，另可基于边界框生成逐点语义分割标签。导入格式覆盖 pcd/ply/pts/xyzrgb/xyz/KITTI bin 等，导出支持 centroid_rel、centroid_abs、vertices、kitti 等格式，并可通过继承 BaseLabelFormat 扩展导出器。面向计算机视觉数据集构建者，需 Python 3.9-3.12，可 pip 安装或源码运行，附带 CAD 期刊论文（2022）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- picking 与 spanning 两种 3D 边界框标注方式，支持 9 DoF 旋转
- 基于边界框生成逐点语义分割标签（输出 np.int8 数组 bin 文件）
- 多种点云导入格式与 5 种标签导出格式，支持自定义导出器
- pip 安装后可用 --example 附带示例点云启动

## 适用场景

- 为 3D 目标检测模型准备点云训练数据
- 制作 KITTI 等格式的 3D 边界框标签
- 生成基于边界框的逐点语义分割标注

## 场景标签

 · 领域:计算机视觉/数据标注

## 证据(README 行号)

> L6: A lightweight tool for labeling 3D bounding boxes in point clouds.
> L31: labelCloud supports two different ways of labeling (*picking* & *spanning*) as well as multiple mouse and keyboard 
> L69: labelCloud is built for a versatile use and aims at supporting all common point cloud file

## 星数曲线

```mermaid
xychart-beta
    title "ch-sa/labelCloud 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 807 --> 810
    line [808, 809, 809]
```

2026-10-18 808 → 2026-10-30 809（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `070803521725` · [字段定义](../../DATASET.md)*
