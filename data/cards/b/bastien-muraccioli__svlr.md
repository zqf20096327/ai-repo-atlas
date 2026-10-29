# bastien-muraccioli/svlr

⭐ 17 · Python · MIT · 推送 2026-01-22 · [GitHub](https://github.com/bastien-muraccioli/svlr) · [官网](https://scalable-visual-language-robotics.github.io/) · 组织维护

**免训练的多模型视觉-语言机器人控制框架，消费级 GPU 可运行**

面向机器人开发者的模块化框架：组合 VLM（Mini-InternVL）、零样本图像分割（CLIPSeg）、LLM（Phi-3-mini，HuggingFace/OpenAI 可选）与句向量相似度模型，从摄像头图像与自然语言指令生成机器人动作序列，通过 socket 发给控制器（默认 UR10 + ROS Noetic + Robotiq 夹爪，可自定义机器人）。默认 HuggingFace LLM 以 4bit 量化运行以适配消费级 GPU。提供仿真模式可无实体机器人调试，conda 环境安装，扩展机器人/动作/模型需修改 JSON 与源码文件。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VLM+零样本分割+LLM+句相似度的多模型流水线，无需训练
- HuggingFace LLM 默认 4bit 量化，面向消费级 GPU
- 仿真模式（--simulation）可无实体机器人运行与测试
- 可通过 JSON + Python 文件扩展新机器人与新动作

## 适用场景

- 用自然语言指令控制机械臂完成抓放等动作
- 在无实体机器人条件下用仿真图像调试视觉-语言控制流程
- 为自有机器人接入多模型感知与指令理解

## 场景标签

`多模态` · 领域:感知与多模态

## 证据(README 行号)

> L18: A modular framework for controlling robots using visual and language inputs, based on multi-model approach.
> L20: Utilizes a Visual Language Model (VLM), zero-shot image segmentation, a Large Language Model (LLM), and a sentence 

## 星数曲线

```mermaid
xychart-beta
    title "bastien-muraccioli/svlr 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 16 --> 18
    line [17, 17]
```

2026-10-18 17 → 2026-10-29 17（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `f2966465d0bf` · [字段定义](../../DATASET.md)*
