# hunmeng2012/Pojia-Ultimate

⭐ 4 · PowerShell · MIT · 推送 2026-11-23 · [GitHub](https://github.com/hunmeng2012/Pojia-Ultimate) · [官网](https://www.hunmeng.icu/) · 个人维护 · 中文 README

**国产无审查大模型 API 中转服务，OpenAI 兼容接入**

提供多个模型 ID（pojia-pro/fast/coder/writer/re/vision）的 API 中转站，统一走 OpenAI Chat Completions 协议，支持 SSE 流式、Function Calling、JSON Mode 与 /v1/embeddings。用户在站点注册后拿 API Key，将现有 OpenAI SDK 的 base_url 改为中转地址即可使用；也提供 Cherry Studio、Chatbox、SillyTavern 等图形客户端的接入步骤。计费为体验包/日卡/月卡/定制档位。用户也可在群内获取权重与部署脚本自行部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 6 个模型 ID，统一走 OpenAI Chat Completions 协议
- 支持 SSE 流式、Function Calling、JSON Mode 与 embeddings 接口
- 兼容 LangChain/LlamaIndex/Dify/FastGPT/OneAPI（README 自述）
- 多线路负载均衡与断流重连（README 自述）

## 适用场景

- 把现有 OpenAI SDK 项目切换 base_url 接入这些模型
- 在 Cherry Studio、Chatbox、SillyTavern 等客户端中配置使用
- 跑长上下文脚本或高频对话调用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L39: |兼容|自己写适配层|**OpenAI SDK 只改 base_url**|
> L52: > 全部统一走 OpenAI Chat Completions 协议，`model` 字段换名即换模型。
> L114: - ✅ 兼容 LangChain / LlamaIndex / Dify / FastGPT / OneAPI

## 星数曲线

```mermaid
xychart-beta
    title "hunmeng2012/Pojia-Ultimate 星数(近 3 点)"
    x-axis ["2026-11-16", "2026-11-22", "2026-11-26"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-16 3 → 2026-11-26 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `33620aa0cbe7` · [字段定义](../../DATASET.md)*
