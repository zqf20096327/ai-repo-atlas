# Arbhh/XCcv_Multi-functional-Platform

⭐ 3 · Python · AGPL-3.0 · 推送 2026-11-24 · [GitHub](https://github.com/Arbhh/XCcv_Multi-functional-Platform) · 个人维护 · 中文 README

**给工业视觉从业者的离线标注训练部署一体化桌面平台**

面向工业视觉场景的离线桌面端深度学习平台，覆盖数据标注（集成 labelme，含基于 SAM/EfficientSAM 的智能标注）、五类任务 14 种内置模型的训练、测试评估（阈值调节、复盘分组、A/B 比对）、FastAPI HTTP 推理服务部署，另附结构化剪枝与 TensorRT 导出的模型工具、57 算子的流程图编排模块与泊松融合缺陷样本合成工具。全程本地运行，数据不出内网；需 Python 3.11 与 Windows 10/11，GPU 可选；模型权重与示例数据不随仓库分发，需按发布方许可自行获取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 标注、训练、测试、部署全流程覆盖，桌面 UI 操作
- 五类任务 14 种内置模型（分类/检测/分割/异常检测/OCR）
- 57 个内置算子的流程图可视化编排，支持 .xvap 打包
- 结构化通道剪枝与 TensorRT 引擎导出工具

## 适用场景

- 在产线内网离线完成缺陷检测模型从标注到部署
- 用 SAM 智能标注加速工业图像标注
- 用流程图编排 AI 与传统视觉算子组成检测链路
- 通过剪枝和 TensorRT 导出降低产线推理开销

## 场景标签

`图像视频处理` `目标检测` `OCR` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: XCcv 是一个面向工业视觉场景的**离线桌面端**多功能深度学习视觉平台，全量开源。
> L24: |训练平台|项目制管理；**五类任务 14 种内置模型**（分类 / 检测 / 分割 / 无监督与少样本异常检测 PatchCore、CIF、SubspaceAD / OCR CRNN，含 ResNet / MobileNetV3

## 星数曲线

```mermaid
xychart-beta
    title "Arbhh/XCcv_Multi-functional-Platform 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-25 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `a28c40a4ac67` · [字段定义](../../DATASET.md)*
