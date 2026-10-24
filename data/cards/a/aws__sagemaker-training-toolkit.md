# aws/sagemaker-training-toolkit

⭐ 530 · Python · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/aws/sagemaker-training-toolkit) · 组织维护

**让任意 Docker 容器接入 SageMaker 训练的 Python 工具库**

AWS 官方库，可将训练脚本与依赖封装进 Docker 容器并使其兼容 Amazon SageMaker 训练服务：通过 SAGEMAKER_PROGRAM 环境变量指定入口脚本（支持 Python 与 shell），将超参数作为脚本参数传入，通过 SM_CHANNEL_* 等环境变量暴露数据通道路径，并提供 Environment 对象只读读取容器环境信息。安装方式为在 Dockerfile 中 pip3 install sagemaker-training，也可使用已内置该库的 SageMaker 预构建镜像。给使用 SageMaker 训练 ML 模型的开发者使用，Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以 pip 安装即可将任意 Docker 容器变为 SageMaker 兼容的训练容器
- 超参数自动作为脚本参数传入入口脚本
- 通过环境变量提供训练通道路径等信息，Environment 对象只读读取容器环境
- 支持 Python 与 shell 入口脚本

## 适用场景

- 把自定义训练脚本和依赖打包成容器，在 SageMaker 上启动训练任务
- 通过超参数向训练脚本传参
- 在训练脚本内读取数据通道与容器环境信息

## 场景标签

`模型训练` · 领域:训练与推理

## 证据(README 行号)

> L7: Train machine learning models within a Docker container using Amazon SageMaker.
> L17: The **SageMaker Training Toolkit** can be easily added to any Docker container, making it compatible with SageMaker

## 星数曲线

```mermaid
xychart-beta
    title "aws/sagemaker-training-toolkit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 529 --> 531
    line [530, 530]
```

2026-10-18 530 → 2026-10-24 530（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `82d8feb40bbb` · [字段定义](../../DATASET.md)*
