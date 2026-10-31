# programasweights/compile-by-training

⭐ 18 · Python · MIT · 推送 2026-10-24 · [GitHub](https://github.com/programasweights/compile-by-training) · [官网](https://programasweights.com/playground?compiler=paw-ft-bs48) · 组织维护

**把自然语言函数描述编译为可本地运行的神经程序（.paw）**

面向开发者的训练式编译器：先用快速 PAW 编译器初始化神经程序，再由教师模型（默认 OpenAI 系列，可自定义配额）生成任务示例，微调 0.6B 本地解释器，产出可复用的 .paw 函数，此后推理在本地运行、无需再调教师模型。需要 Python 3.10+、uv 与 OpenAI API key；默认配置面向约 40 GB 显存的加速器，小设备需调低 micro-batch 或开梯度检查点。附 NeurIPS 论文引用信息。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 教师模型生成示例 + 微调小型解释器的编译流程
- 产出的 .paw 函数本地推理，不再调用教师模型
- 教师选择、配额等可通过命令行自定义
- 支持缓存 mapper 资产与教师合成结果以复用

## 适用场景

- 把一段功能描述编译成可复用的本地推理函数
- 在小模型上以本地权重替代持续调用大模型 API
- 研究训练式编译与 Program-as-Weights 编程范式

## 场景标签

`微调` · 领域:训练与推理

## 证据(README 行号)

> L5: Compile by Training uses teacher models to generate examples, finetunes a small PAW interpreter, and produces a `.pa
> L31: The program downloads the shared 0.6B interpreter once, then runs locally. A PAW API key is optional; setting `PAW_
> L53: 1. Compile the specification once with the fast PAW compiler to initialize the neural program.

## 星数曲线

```mermaid
xychart-beta
    title "programasweights/compile-by-training 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-31 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 mid · 依据 README sha `b69e00a96b0e` · [字段定义](../../DATASET.md)*
