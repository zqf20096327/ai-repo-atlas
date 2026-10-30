# notAI-tech/fastDeploy

⭐ 106 · Python · MIT · 推送 2026-02-10 · [GitHub](https://github.com/notAI-tech/fastDeploy) · 组织维护

**以最少代码将 Python 推理管道部署为微服务的框架**

面向深度学习/机器学习推理管道的部署框架：用户将现有推理代码写成 recipe，fastDeploy 以消费者-生产者架构（sqlite 队列）将其作为 REST 服务运行，无需修改推理代码。开箱提供并发输入自动批处理、Prometheus 监控指标、dockerfile 自动生成与 Kubernetes 健康检查支持；预测循环与推理端点分离，可独立扩展。适用场景为单条输入、推理耗时 >50ms、可从批处理获益的模型；不适合 IO 密集或非阻塞外部调用的场景。提供 pip 安装与 Python/curl/Node.js 客户端查询方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 并发输入自动批处理，无需修改现有推理代码
- sqlite 队列连接预测循环与推理端点，可独立扩展
- Prometheus 监控指标暴露
- 自动生成 dockerfile 与 Kubernetes 健康检查

## 适用场景

- 把现有 PyTorch 推理管道包装成内部 REST 微服务
- 对用户搜索输入、图像分类等单条请求做自动批处理
- 将模型前后处理与业务逻辑拆分为独立服务

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L2: #### easy and performant micro-services for Python Deep Learning inference pipelines
> L4: - Deploy any python inference pipeline with minimal extra code

## 星数曲线

```mermaid
xychart-beta
    title "notAI-tech/fastDeploy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 105 --> 107
    line [106, 106]
```

2026-10-18 106 → 2026-10-30 106（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `3e16a3044fd4` · [字段定义](../../DATASET.md)*
