# geekjr/quickai

⭐ 161 · Python · MIT · 推送 2026-02-05 · [GitHub](https://github.com/geekjr/quickai) · 个人维护

**简化多种深度学习模型实验的 Python 库**

QuickAI 是面向快速实验的 Python 机器学习库：把训练与推理流程压缩到 1-2 行代码，自动完成数据加载、预处理、模型定义与训练。支持图像分类（EfficientNet、ResNet、VGG、MobileNet 等）、NLP（GPT-Neo、GPT-J、DistilBERT 的生成/问答/NER/摘要/情感分析）与目标检测（YOLOv4）。依赖 TensorFlow、PyTorch、sklearn 等，提供 pip 安装与 Docker 容器；使用 YOLO 时需当前目录存在 coco.names 文件（不用 YOLO 可为空文件）。GPT-J 6B 支持标注为 BETA。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1-2 行代码完成模型训练/推理（数据加载、预处理、训练自动化）
- 覆盖图像分类、NLP、目标检测三类共数十种模型架构
- 提供 Docker 容器（CPU/GPU 两种运行命令）避免手动配置依赖

## 适用场景

- 在自己的数据集上快速试跑 EfficientNet 等架构对比效果
- 用 GPT-Neo/DistilBERT 快速体验文本生成、问答、摘要等任务
- 通过 Docker 环境免去深度学习框架的配置工作

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L26: architectures. That is where QuickAI came in. It allows for easy experimentation of many model architectures quickl
> L52: all of these steps happens automatically with just 1-2 lines of code.
> L77:  - GPT-NEO 125M(Generation, Inference)

## 星数曲线

```mermaid
xychart-beta
    title "geekjr/quickai 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 160 --> 162
    line [161, 161]
```

2026-10-18 161 → 2026-10-29 161（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6ddcb94750f1` · [字段定义](../../DATASET.md)*
