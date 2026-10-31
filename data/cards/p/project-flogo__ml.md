# project-flogo/ml

⭐ 14 · Go · BSD-3-Clause · 推送 2025-12-05 · [GitHub](https://github.com/project-flogo/ml) · 组织维护

**Flogo 的机器学习推理活动模块：在流应用中运行 TensorFlow 模型**

Project Flogo 的 ML 扩展仓库，提供推理（Inference）活动，采用框架化设计以便扩展不同 ML 库，目前仅实现 TensorFlow 1.X（基于 Golang API）。只支持运行时推理，不支持训练，训练需在 Python 中完成并导出 SavedModel 格式。要求开发机与目标机上安装对应平台架构的 TensorFlow 动态库。模型输入支持 zip 归档或目录形式，输出为含 scores/classes 的 map。附带图像识别、流式异常检测等示例应用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 推理活动支持以框架化方式扩展 ML 库，当前实现 TensorFlow 1.X
- 读取 SavedModel 格式（zip 归档或目录），输出 scores/classes 映射
- 仅做运行时推理，训练需在 Python 中完成后导出
- 附带 CNN、图像识别 REST API、流式异常检测等示例

## 适用场景

- 在 Flogo 流应用中嵌入 TensorFlow 模型做推理
- 构建提供图像识别 REST API 的应用
- 对流式数据做 DNN/自编码器异常检测

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: As the name suggests, this project-flogo/ml repo is intended to contain all the modules for Flogo that is tied to ma
> L10: The Inference activity is built in such a way as to allow multiple ML libraries to be called. Each library is calle
> L14: First and foremost, Flogo supports inferencing TensorFlow models, it does not support training of models using inco

## 星数曲线

```mermaid
xychart-beta
    title "project-flogo/ml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `4619e4147bde` · [字段定义](../../DATASET.md)*
