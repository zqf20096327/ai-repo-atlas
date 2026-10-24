# zjunlp/LabVLA

⭐ 107 · Python · MIT · 推送 2026-09-10 · [GitHub](https://github.com/zjunlp/LabVLA) · [官网](https://zjunlp.github.io/LabVLA/) · 组织维护 · 中文 README

**面向科学实验室的视觉-语言-动作机器人基础模型**

LabVLA 基于 Qwen3-VL-4B-Instruct 视觉语言骨干，通过 DiT 流匹配动作专家输出实时机器人控制，训练遵循 π0.5 配方：FAST 动作 token 预训练→流匹配后训练（知识隔离）→任务微调。面向具身智能研究者，提供完整训练/微调/部署代码与 Hugging Face 权重，部署形式为 WebSocket 推理服务器。环境固定为 Python 3.10、CUDA 12.6、PyTorch 2.7.1，训练基准在 80GB A100 上给出，RoboGenesis 数据集尚未发布。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- FAST 动作 token 预训练→流匹配后训练→任务微调的完整训练管线
- DiT 动作专家生成 50 步连续动作块，VLM 与动作专家间停止梯度
- 数据扫描/清洗/统计/预检的 DatasetSchema 数据工具链
- WebSocket 推理服务器部署脚本

## 适用场景

- 科研实验室场景下微调和部署视觉-语言-动作机器人控制
- 在自有机器人数据集上复用训练管线训练 VLA 模型
- 连接机器人或仿真器客户端做评测 rollout

## 场景标签

 · 领域:机器人/具身智能

## 证据(README 行号)

> L38: **LabVLA** turns a **Qwen3-VL-4B-Instruct** vision–language backbone into a real-time robot controller through a **
> L4:  The First Vision-Language-Action Foundation Model for Scientific Laboratories

## 星数曲线

```mermaid
xychart-beta
    title "zjunlp/LabVLA 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 105 --> 108
    line [106, 107, 107]
```

2026-10-18 106 → 2026-10-24 107（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `1e7d77ae5924` · [字段定义](../../DATASET.md)*
