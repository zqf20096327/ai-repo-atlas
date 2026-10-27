# Climatik-Project/Climatik-Project

⭐ 38 · Go · Apache-2.0 · 推送 2026-03-19 · [GitHub](https://github.com/Climatik-Project/Climatik-Project) · 组织维护

**Kubernetes 功耗上限算子：按功率约束调度与伸缩 LLM 推理服务**

面向数据中心的 Kubernetes 自定义算子，通过 CRD 指定服务器与机架级功耗上限，利用 KEDA 按功率约束伸缩 LLM 推理部署，Kepler 监测 CPU/GPU 功耗，并结合机架感知调度降低散热需求。架构含 Controller（监测并给出建议）、Webhook（执行软硬件功耗调节）、Forecast Model（预测负载与功耗），内置功率超订与性能功耗比优化示例策略，支持先以纯观测/推荐模式运行再渐进自动化。LLM 推理服务本身由 KServe、vLLM 等系统部署管理，本算子仅影响其伸缩行为。安装需克隆仓库、配置 .env、安装 Python 依赖并通过 make 部署 CRD。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CRD 声明功耗上限，KEDA 驱动 LLM 推理部署伸缩
- Controller/Webhook/Forecast Model 三组件架构
- 机架级热管理与机架感知调度
- 内置功率超订与性能功耗比优化示例策略

## 适用场景

- 数据中心在功率与散热约束下管理 LLM 推理负载
- 先以观测与推荐模式评估功耗策略再逐步自动化
- 通过机架感知调度降低机房冷却需求

## 场景标签

 · 领域:云原生/数据中心能效管理

## 证据(README 行号)

> L5: The purpose of this project is to create a scalable and power-efficient Large Language Model (LLM) inference service
> L163: It's important to note that the power capping operator only installs the necessary CRDs and operators, and allows 
> L165: KServe and vLLM. The power capping operator will only affect the scaling behavior of these services to reach the

## 星数曲线

```mermaid
xychart-beta
    title "Climatik-Project/Climatik-Project 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-27 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `2ccd9ce0088a` · [字段定义](../../DATASET.md)*
