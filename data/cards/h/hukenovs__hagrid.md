# hukenovs/hagrid

⭐ 1,083 · Python · 推送 2026-10-30 · [GitHub](https://github.com/hukenovs/hagrid) · [官网](https://arxiv.org/abs/2206.08219) · 组织维护

**大规模手部手势识别图像数据集 HaGRIDv2（108万张，33类）**

面向手部手势识别（HGR）系统训练的图像数据集：HaGRIDv2 含 1,086,158 张 FullHD RGB 图像（1.5T），分 33 类手势及独立 no_gesture 类，按 user_id 划分 train/val/test；来自 65,977 名受试者，含室内多变光照等条件。标注含 COCO 格式包围盒、MediaPipe 手部关键点及 FairFace/MiVOLO 自动标注的人口学元信息，并提供 YOLO/COCO 转换脚本、预训练检测与分类模型训练测试代码及动态手势识别算法链接。数据通过链接或 python 脚本下载。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1,086,158 张 FullHD 图像、33 类手势 + no_gesture 类
- COCO 格式包围盒、MediaPipe 关键点、年龄/性别/种族元信息标注
- 提供 YOLO/COCO 标注转换脚本与预训练基线模型
- 另有 512px 轻量版（119.4GB）与动态手势识别算法仓库

## 适用场景

- 训练视频会议/智能家居/车载场景的手势检测或分类模型
- 做手部检测或全帧手势分类的基线实验
- 利用人口学元信息做数据分布分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L5: We introduce a large image dataset **HaGRIDv2** (**HA**nd **G**esture **R**ecognition **I**mage **D**ataset) for han
> L7: HaGRIDv2 size is **1.5T** and dataset contains **1,086,158** FullHD RGB images divided into **33** classes of gestur


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-01 · 置信度 high · 依据 README sha `d15d9633519a` · [字段定义](../../DATASET.md)*
