# noname9006/LlamaToaster

⭐ 15 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/noname9006/LlamaToaster) · [官网](https://llamatoaster.com) · 个人维护

**llama.cpp 参数扫描基准测试平台：测出本机最优配置并共享结果**

面向 llama.cpp 用户的基准测试系统：worker 在被测机器上用 llama-bench/llama-server 扫描 -ngl、context、batch、--n-cpu-moe、投机解码等参数组合，记录测量结果并给出可直接用于自己推理命令行的配置。附带按 sha256 索引的约 400 万 Hugging Face GGUF 文件索引与共享结果库，可用自然语言向 AI 助手查询累积数据。提供 llamatoaster.com 托管实例，也可完整自托管：Fastify+SQLite 服务端、React 前端、pull-only worker；worker 仅发起出站 HTTPS。AI 助手面板需自行配置 AI_API_KEY 等环境变量，未配置时仅显示未配置。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- worker 用 llama-bench/llama-server 扫描参数空间并记录测量结果
- 约 400 万 GGUF 文件按 sha256 内容哈希索引
- 共享结果库 + AI 助手以自然语言查询聚合数据
- worker 仅出站 HTTPS 连接，无需端口转发；支持 GitHub OAuth 多用户与自托管无登录模式

## 适用场景

- 在自己的 GPU/CPU 机器上找到 llama.cpp 最优运行参数
- 把多台机器的基准结果汇总对比
- 自托管一套团队内的推理性能测试平台

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: machine, and it sweeps the parameter space with `llama-bench` /
> L23: - **An AI assistant that reads the numbers so you don't have to.** Instead of

## 星数曲线

```mermaid
xychart-beta
    title "noname9006/LlamaToaster 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `288d49d7b139` · [字段定义](../../DATASET.md)*
