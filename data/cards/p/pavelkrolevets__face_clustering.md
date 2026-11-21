# pavelkrolevets/face_clustering

⭐ 26 · Python · 推送 2026-11-20 · [GitHub](https://github.com/pavelkrolevets/face_clustering) · 个人维护

**人像照片按相似人脸聚类的三脚本流水线**

由三个脚本组成的 Python 流水线：先用内置 MTCNN 检测并对齐人脸，经预训练 FaceNet 提取 128 维 L2 归一化嵌入；再计算全部嵌入的 N×N 欧氏距离矩阵；最后按最近邻链排序图像并用 KMeans（默认 30 簇）分到各簇目录。README 给出 LFW 数据集（13,233 张图）示例与约 3 GB 磁盘占用，也支持按每人一个子文件夹组织的自有照片。默认簇数偏大时 README 提示需自行调高 n_clusters。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MTCNN 检测对齐 + 预训练 FaceNet 128 维嵌入提取
- 全量 N×N 欧氏距离矩阵计算并落盘为 npy
- 最近邻链排序 + KMeans 聚类，输出按簇分目录的图片副本
- 支持替换为自有照片目录，文件夹名作为人物标签

## 适用场景

- 把一大文件夹人像照片按同一个人分组
- 在 LFW 数据集上复现人脸嵌入与聚类流程
- 整理个人多年照片库中同一人物的照片

## 场景标签

`人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: Sort a large folder of portrait photos into clusters of the same person,
> L11: |1|`export_embeddings.py`|Detects and aligns each face, then extracts a 128-dim FaceNet embedding for it|
> L13: |3|`cluster_faces.py`|Sorts the images into a nearest-neighbor chain, then splits them into KMeans clusters|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `550dfabebadb` · [字段定义](../../DATASET.md)*
