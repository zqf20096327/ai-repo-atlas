# Baro7ue/comllm-edge-scheduler

⭐ 3 · Jupyter Notebook · Apache-2.0 · 推送 2026-11-15 · [GitHub](https://github.com/Baro7ue/comllm-edge-scheduler) · 个人维护 · 中文 README

**在 Jetson 上用 0.5B LLM 做 55ms 级任务卸载调度器**

基于论文 COMLLM（arXiv:2604.07148）的独立复现与部署项目：将 LoRA 微调的 Qwen2.5-0.5B/1.5B 以 GGUF 格式经 llama.cpp (CUDA) 部署在 Jetson Orin Nano 8GB 上，对终端产生的计算任务输出本地执行或卸载至 3–11 个边缘服务器的决策，部署形态下单次决策 p50 为 55.0 ms。环境节点实时模拟终端、上行链路与服务器并经以太网请求决策，决策耗时计入任务时延；调度器节点与网络为真实，终端与服务器为模拟。提供模拟器与闭环实验脚本，README 给出各结果的来源运行记录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LoRA 微调的 Qwen2.5-0.5B 经 llama.cpp (CUDA) 部署在 Jetson Orin Nano
- 部署形态下单次决策 p50 55.0 ms、p99 72.0 ms（500 请求实测）
- 超载时回退到 one-step 公式的 shedding 策略，支持 20 终端、1.0% 丢弃
- 提供模拟器、开放环三套测试集与 Colab/Jetson 闭环对比实验

## 适用场景

- 在 Jetson 边缘设备上部署小型 LLM 做实时卸载决策
- 复现论文 COMLLM 的任务卸载调度并对比不同教师公式
- 研究移动边缘计算中决策时延对任务截止期的影响

## 场景标签

`微调` `推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L11: 1.5B are LoRA-fine-tuned on soft labels from the paper's one-step cost formula and served by llama.cpp
> L12: (CUDA) with a compact prompt and a one-token answer. An environment node simulates the terminals, the
> L14: decision takes counts toward the task's delay. Terminals and servers are simulated; the scheduler node

## 星数曲线

```mermaid
xychart-beta
    title "Baro7ue/comllm-edge-scheduler 星数(近 2 点)"
    x-axis ["2026-11-19", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-19 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `5aa6205bfa7d` · [字段定义](../../DATASET.md)*
