# Cognitive-AI-Systems/MAPF-GPT-DDG

⭐ 68 · Python · MIT · 推送 2026-02-21 · [GitHub](https://github.com/Cognitive-AI-Systems/MAPF-GPT-DDG) · [官网](https://sites.google.com/view/mapf-gpt-ddg) · 组织维护

**基于模仿学习的去中心化多智能体路径规划求解器（IROS-2025）**

在 MAPF-GPT 基础上引入 Delta Data Generation（DDG）微调方法：训练中检测现有模型难以求解的困难实例，由专家求解后将观测-动作对加入训练集，属无奖励的主动学习路线。提供示例脚本、POGEMA 基准评测、1B 训练数据集（Hugging Face）下载与训练脚本；支持 2M/6M/85M 模型，架构与原 MAPF-GPT 兼容可直接加载其权重，训练采用 DDP 多 GPU。推荐 GPU 加速，小模型可 CPU 运行，Apple Silicon 可用 mps 设备。

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

- DDG 微调：训练中自动采集困难实例的专家数据增补训练集
- 兼容原 MAPF-GPT 权重（2M/6M/85M 自动从 Hugging Face 下载）
- POGEMA 基准评测脚本，输出成功率/SoC 与 SVG 动画
- 训练支持 DDP 多 GPU，可选 standard/ddg/dagger 三种数据采集模式

## 适用场景

- 在 POGEMA 基准地图上评测学习式 MAPF 求解器
- 复现论文的 DDG 主动微调训练流程
- 对比 DDG 与经典 DAgger 数据采集方法

## 场景标签

`微调` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L41: To test MAPF-GPT-DDG, you can simply run the `example.py` script. By default, it uses the MAPF-GPT-DDG-2M model, bu
> L74: To train MAPF-GPT-DDG, we utilized the 1B dataset generated to train MAPF-GPT. It can be downloaded from Hugging Fa
> L78: To train MAPF-GPT from scratch or fine-tune the existing weights, you can use the `train.py` script. By providing i

## 星数曲线

```mermaid
xychart-beta
    title "Cognitive-AI-Systems/MAPF-GPT-DDG 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-28 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `74323667e33d` · [字段定义](../../DATASET.md)*
