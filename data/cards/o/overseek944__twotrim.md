# overseek944/twotrim

⭐ 31 · Python · Apache-2.0 · 推送 2026-04-13 · [GitHub](https://github.com/overseek944/twotrim) · [官网](https://twotrim.com) · 个人维护

**面向 LLM API 的提示词压缩中间件（代理/SDK）**

部署在应用与 LLM API 之间的反向代理，也可作为 Python SDK 原生调用，在发送前压缩提示词以降低 token 消耗。机制包括：基于 LongLLMLingua 的抽取式策略、all-MiniLM-L6-v2 语义分块打分、按最终用户查询做互信息剪枝、以及 Lost-in-the-Middle 事实重排；全程在本地 CPU 运行。提供 lossless/balanced/aggressive 三档压缩模式，RAG/QA 场景自动切换为仅抽取式压缩。README 附有自测基准数据，也披露了极端多跳 RAG 数据集上的准确率下降为已知限制。支持 OpenAI 格式，Claude/Gemini 需在后面再接 LiteLLM 做格式转换。

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

- 反向代理或 Python SDK 两种接入方式，应用侧零改动
- 三档压缩模式：lossless（纯格式清理）/ balanced（语义删除冗余）/ aggressive（约 65% 削减）
- 本地 CPU 运行，处理耗时低于 100 毫秒
- RAG/QA 场景自动切换为抽取式压缩以避免事实问答中的幻觉

## 适用场景

- 在高 token 消耗的 LLM 应用前部署代理以降低 API 成本
- 在 Python 后端中以 SDK 方式本地压缩后再调用 OpenAI
- 压缩长文档（如会议记录）上下文再发送给 LLM

## 场景标签

`模型网关` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L11: TwoTrim is an ultra-lightweight, mathematically robust prompt compression middleware. It sits between your applicat
> L17: TwoTrim is built on a simple philosophy: **Zero Code Refactoring**. You can deploy it as an invisible proxy server,

## 星数曲线

```mermaid
xychart-beta
    title "overseek944/twotrim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 30 --> 32
    line [31, 31]
```

2026-10-18 31 → 2026-10-29 31（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `cc5bc970888b` · [字段定义](../../DATASET.md)*
