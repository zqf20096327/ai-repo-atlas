# ubonpartners/yolo-dpar

⭐ 10 · Python · AGPL-3.0 · 推送 2026-06-14 · [GitHub](https://github.com/ubonpartners/yolo-dpar) · 组织维护

**单次前向同时输出检测/姿态/属性/ReID/人脸质量的 YOLO 模型库**

基于 Ultralytics 分支构建的多任务 YOLO 模型仓库：单次前向传播输出 5 类检测、17/5 点关键点、每人的二元属性、80 维 L2 归一化 ReID 嵌入与人脸质量分数，省去多模型串行流水线。提供 DP/DPA/DPAR/DPARF 系列权重（Git LFS）、 webcam/视频 demo 查看器与基准测试脚本；依赖 ubon26 分支的 ultralytics。属性标注使用视觉 LLM 自动化完成，附带 Dataset Processor 训练数据流水线说明。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单次前向输出检测、关键点、属性、ReID 嵌入与 FIQA 质量分数
- 属性头与检测头共享特征，参数开销 <0.2%
- FiLM 调制 MLP 适配器训练 ReID 分支后融合回主干
- 自带 demo 查看器与多模型基准测试脚本

## 适用场景

- 行人检测同时获取姿态、属性与跨镜重识别嵌入
- 按人脸质量分数过滤送入人脸嵌入模型的低质量裁剪
- 对 DPA/DPAR 与官方 YOLO 检查点做统一基准对比

## 场景标签

`目标检测` `人脸识别` · 领域:感知与多模态

## 证据(README 行号)

> L3: **One-pass YOLO26 models that jointly do detection + pose/keypoints + attributes + ReID embeddings + face image qual
> L5: Most pipelines do: **detect → crop → run pose model → run attribute model → run ReID model → run face quality model*
> L29: - **Detection**: 5 classes — `person`, `face`, `vehicle`, `animal`, `weapon`


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `76d020736c82` · [字段定义](../../DATASET.md)*
