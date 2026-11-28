# DDharm007/mars-terrain-ai

⭐ 5 · Jupyter Notebook · NOASSERTION · 推送 2026-11-23 · [GitHub](https://github.com/DDharm007/mars-terrain-ai) · 个人维护

**火星地形图像分割与地形情报分析研究平台**

基于 NASA/JPL AI4MARS 数据集（2,326 对图像-掩码）训练的火星地表语义分割平台，提供 DeepLabV3+ 与 U-Net 两类 PyTorch 模型，输出 Soil/Bedrock/Sand/Big Rock 四类分割，并附带地形情报引擎（类别占比、连通区域、置信度、熵、JSON 报告）。前端为 FastAPI + React 任务控制台，含 6 个路由页面。README 明确声明其 2D 语义感知结果不验证火星车物理安全性或可通行性；训练权重因体积不入 Git，需本地放置 .pth 文件方可实时推理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 在 526 帧 JPL 专家测试集上给出 mIoU/Dice/像素精度等基准指标
- 按 MSL SCLK 时间戳做防泄漏时序聚类数据划分
- 地形情报引擎生成结构化 JSON 报告与 9 宫格诊断图
- Windows 一键启动器自动检查依赖、端口与 CUDA/CPU 回退

## 适用场景

- 对火星车地表图像做四类地物语义分割
- 查看跨火星车（MSL/MER）域偏移评估结果
- 生成分割结果的地形组成与置信度分析报告

## 场景标签

`目标检测` `科研工具` · 领域:学习与行业

## 证据(README 行号)

> L16: > **Important:** MANGAL DRISHTI is a **2D semantic perception and terrain intelligence research platform** trained 
> L21: MANGAL DRISHTI (**Mars Autonomous Navigation, Geospatial Analysis & Learning**) is an end-to-end computer vision, q
> L29: 2. **Semantic Segmentation Models (PyTorch + AMP)**:


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `bf0d7b7e9721` · [字段定义](../../DATASET.md)*
