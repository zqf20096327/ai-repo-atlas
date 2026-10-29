# RobotecAI/agentic-mobile-manipulator

⭐ 50 · Python · Apache-2.0 · 推送 2026-07-15 · [GitHub](https://github.com/RobotecAI/agentic-mobile-manipulator) · 组织维护

**仓库自主移动操作机器人的端到端演示（ROS 2 仿真）**

Robotec AI 维护的具身智能演示：在 ROS 2 + O3DE 仿真的小型仓库场景中，Robotnik Kairos 移动操作机器人根据人类自然语言指令执行任务，检测泄漏、路径阻塞等异常并响应。多智能体系统在 AMD Ryzen AI 处理器上全本地运行：LFM2-VL 视觉语言模型、gpt-oss-20b 本地 LLM 做规划与对话，推理分布在 CPU、GPU（llama.cpp/Vulkan）与 NPU（FastFlowLM），硬件在环仿真对应真实部署。提供 Docker Compose 快速启动方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言指令驱动的自主仓库操作（感知/推理/对话）
- CPU/GPU/NPU 三路本地推理（llama.cpp/Vulkan、FastFlowLM NPU）
- LFM2-VL + gpt-oss-20b 本地模型栈，全端侧运行
- 硬件在环仿真，面向仿真到实机的迁移

## 适用场景

- 在仿真环境中演示仓库机器人的自然语言任务执行
- 验证 AMD Ryzen AI 平台上端侧具身智能的部署方式
- 参考多智能体编排机器人导航与操作栈的架构

## 场景标签

`多智能体` `多模态` · 领域:Agent 开发

## 证据(README 行号)

> L26: The demonstration features a fully autonomous warehouse robot capable of perception, reasoning, and natural languag
> L43: - Local inference across **CPU, GPU (llama.cpp / Vulkan) and the AMD Ryzen™ AI NPU (FastFlowLM)** — the safety VLM 

## 星数曲线

```mermaid
xychart-beta
    title "RobotecAI/agentic-mobile-manipulator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-29 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `dc01ce7436ef` · [字段定义](../../DATASET.md)*
