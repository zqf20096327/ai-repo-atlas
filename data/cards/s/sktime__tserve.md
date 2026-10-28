# sktime/tserve

⭐ 19 · Python · BSD-3-Clause · 推送 2026-10-19 · [GitHub](https://github.com/sktime/tserve) · [官网](https://tserve.readthedocs.io/) · 组织维护

**时序基础模型本地推理服务器：加载一次、HTTP 应答预测请求**

TServe 是运行在自有硬件上的本地推理服务器，面向时序预测基础模型（Chronos、TimesFM、Moirai、TTM、TiRex 等 117 个 checkpoint）。它在启动时下载并加载权重常驻内存，之后通过 POST /predict 以 JSON 应答预测请求，切换模型只需改一个字段。以 sktime 预测器统一接口封装各模型家族，每个家族有独立 Docker tag 或 pip extra，分 CPU/GPU 版本。附带浏览器仪表盘、Swagger/ReDoc 文档与 Python 客户端（支持 pandas/polars/pyarrow）。限制：面板与层级化输入不在契约内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 117 个时序基础模型 checkpoint，统一为一套请求接口（past 表 + horizon）
- 权重启动时加载常驻内存，请求只付推理开销
- Docker 镜像与 pip extra 按模型家族分发，分 CPU/GPU tag
- 浏览器仪表盘可上传 CSV 绘制预测，含预测区间

## 适用场景

- 在自有服务器上部署时序预测模型并通过 HTTP/JSON 调用
- 快速对比不同时序基础模型在自有数据上的预测结果
- 把已训练的 sktime 预测器作为服务上线

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8: **Time series serving for foundation models.** TServe loads models such as Chronos, TimesFM, Moirai, TTM, and TiRex 
> L10: Each model family ships its own package, input format, and loading code. sktime wraps them as forecasters with one 
> L21: TServe is a server you run on your own hardware, not a hosted API. How it works · Docker Hub

## 星数曲线

```mermaid
xychart-beta
    title "sktime/tserve 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-28"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-28 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `3881702d279d` · [字段定义](../../DATASET.md)*
