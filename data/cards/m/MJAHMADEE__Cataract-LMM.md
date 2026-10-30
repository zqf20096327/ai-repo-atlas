# MJAHMADEE/Cataract-LMM

⭐ 17 · Jupyter Notebook · NOASSERTION · 推送 2026-05-25 · [GitHub](https://github.com/MJAHMADEE/Cataract-LMM) · [官网](https://mjahmadee.github.io/Cataract-LMM/) · 个人维护

**白内障手术视频多任务分析框架：分割/阶段识别/技能评估**

面向手术视频分析的深度学习框架，基于 PyTorch 提供四类任务：手术器械实例分割（YOLOv8/11、Mask R-CNN、SAM/SAM2）、11 阶段手术流程识别（MViT、Swin-T、TeCNO 等）、手术技能评估（TimeSformer、R3D-18 等）及 GPU 加速视频处理。配套公开数据集 Cataract-LMM（Hugging Face），方法发表于 Nature Scientific Data。安装支持 Poetry、Conda、Docker 三种方式，依赖 Python 3.8+、CUDA 11.8+（GPU 加速）与 FFmpeg。代码与数据集均以 CC BY-NC-ND 4.0 发布，禁止商用与衍生分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四任务统一框架：器械分割、阶段识别、技能评估、视频处理
- 模型库给出各任务多模型性能指标（如 YOLOv11 分割 mAP 73.9%，MViT-B 阶段识别准确率 85.7%）
- 配套 Cataract-LMM 公开数据集（Hugging Face），方法发表于 Nature Scientific Data
- 提供 Poetry/Conda/Docker 三种安装方式与 YAML 配置

## 适用场景

- 研究者在白内障手术视频上训练/评测器械分割模型
- 手术流程阶段自动识别与技能客观评估
- 基于公开数据集复现论文基线或开展医学 AI 研究

## 场景标签

`图像视频处理` `目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L30: - **Surgical Instance Segmentation** using YOLO, Mask R-CNN, and SAM architectures
> L31: - **Surgical Phase Recognition** with Video Transformers, 3D CNNs, and temporal models
> L32: - **Surgical Skill Assessment** through multi-modal analysis and performance metrics

## 星数曲线

```mermaid
xychart-beta
    title "MJAHMADEE/Cataract-LMM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-30 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `290789b322a7` · [字段定义](../../DATASET.md)*
