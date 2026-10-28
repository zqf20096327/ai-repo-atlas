# JINO-ROHIT/tachyon

⭐ 48 · Python · MIT · 推送 2026-04-15 · [GitHub](https://github.com/JINO-ROHIT/tachyon) · 个人维护

**面向消费级硬件的 LLM 推理引擎**

基于 PyTorch 的 LLM 推理引擎，定位在消费级硬件（如 RTX 4060 Ti 16GB）上运行。提供请求级 kv cache 开关、continuous batching（decode 步批量执行并回收完成请求）、小批量 prefill 以避免 OOM、向量化操作、prefix caching 等机制。支持以约 3 行代码调用引擎生成文本，并可启动 OpenAI 兼容服务器，用 openai 库调用模型。附带 benchmark 脚本与延迟/吞吐对比数据。目前实现 llama 3 系列模型，paged attention 等仍在 to-do 中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- continuous batching：decode 步批量执行、完成请求即时回收
- prefix caching 复用共享 system prompt / few-shot 的 prefill 计算
- OpenAI 兼容 API 服务器
- 请求级 kv cache 开关与批量 prefill 防 OOM

## 适用场景

- 在消费级 GPU 上本地运行 Llama 3 模型推理
- 以 OpenAI 兼容接口对外提供推理服务
- 对比不同 batching 与缓存策略的吞吐表现

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: a LLM inference engine to run on consumer hardware.
> L35: You can spin up the server and then use the `openai` library to invoke the model as well -

## 星数曲线

```mermaid
xychart-beta
    title "JINO-ROHIT/tachyon 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-28 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `fac1816b1e9f` · [字段定义](../../DATASET.md)*
